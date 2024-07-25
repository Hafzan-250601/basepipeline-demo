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
        sh 'trivy image --no-progress --exit-code 0 --severity HIGH,CRITICAL -o results.json devopsapps'
      }
    }
    stage('Pass Finding to SecurityHub') {
      steps {
        sh 'pip3 install boto3 json datetime--break-system-packages'
        sh 'python3 securityhub-parser.py'
      }
    }
  }
}
