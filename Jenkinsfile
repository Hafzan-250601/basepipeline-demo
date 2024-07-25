pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'docker build -t devopsapps .'
      }
    }
    stage('Scan') {
      steps {
        sh 'trivy image --format template --template asff.tpl -o report.asff --severity HIGH,CRITICAL,MEDIUM devopsapps'
        sh 'aws securityhub enable-import-findings-for-product --product-arn arn:aws:securityhub:ap-southeast-1::product/aquasecurity/aquasecurity'
      }
    }
    stage('Upload Findings to SecurityHub') {
      steps {
        sh 'cat report.asff | jq \'.Findings\''
        sh 'aws securityhub batch-import-findings --findings report.asff'
      }
    }
  }
}
