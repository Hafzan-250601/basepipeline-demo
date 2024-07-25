import json
import boto3
import datetime

# Function to read Trivy findings from a JSON file
def read_trivy_findings(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Function to convert Trivy findings to Security Hub format
def convert_to_securityhub_format(trivy_findings, image_name):
    findings = []
    for finding in trivy_findings.get('Results', []):
        for vulnerability in finding.get('Vulnerabilities', []):
            finding_id = f"{image_name}-{vulnerability['VulnerabilityID']}"
            findings.append({
                'SchemaVersion': '2018-10-08',
                'Id': finding_id,
                'ProductArn': 'arn:aws:securityhub:ap-southeast-1:921704920702:product/921704920702/default',
                'GeneratorId': 'trivy',
                'AwsAccountId': '921704920702',
                'Types': ['Software and Configuration Checks/Vulnerabilities/CVE'],
                'CreatedAt': datetime.datetime.utcnow().isoformat() + 'Z',
                'UpdatedAt': datetime.datetime.utcnow().isoformat() + 'Z',
                'Severity': {
                    'Label': vulnerability['Severity'].upper()
                },
                'Title': vulnerability['Title'],
                'Description': vulnerability['Description'],
                'Resources': [
                    {
                        'Type': 'Container',
                        'Id': image_name,
                        'Partition': 'aws',
                        'Region': 'ap-southeast-1'
                    }
                ],
                'SourceUrl': vulnerability.get('PrimaryURL', ''),
                'ProductFields': {
                    'ProductName': 'Trivy',
                    'ProviderName': 'Aqua Security',
                    'VulnerabilityID': vulnerability['VulnerabilityID']
                }
            })
    return findings

# Function to send findings to AWS Security Hub
def send_findings_to_securityhub(findings):
    client = boto3.client(
        'securityhub',
        region_name='ap-southeast-1',
        aws_access_key_id='AKIA5NGPE6Z7MBBKVKMM ',  # Replace with your access key
        aws_secret_access_key='hryH4e6zgSghmrEADNRmmlYnK3li6vPNCj7R+StF',  # Replace with your secret key
    )
    response = client.batch_import_findings(Findings=findings)
    if response['FailedCount'] > 0:
        print(f"Failed to import {response['FailedCount']} findings")
    else:
        print("Successfully imported findings to Security Hub")

def main():
    file_path = 'results.json'
    image_name = 'devopsapps'
    trivy_findings = read_trivy_findings(file_path)
    securityhub_findings = convert_to_securityhub_format(trivy_findings, image_name)
    send_findings_to_securityhub(securityhub_findings)

if __name__ == '__main__':
    main()
