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
        sh 'trivy -f json -o results.json --exit-code 0 --severity HIGH,MEDIUM,LOW --quiet --auto-refresh devopsapps'
      }
    }
    stage('Pass Finding to SecurityHub') {
      steps {
        sh 'pip3 install boto3 --break-system-packages'
        sh 'python3 securityhub-parser.py'
      }
    }
  }
}
