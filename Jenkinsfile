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
        sh 'trivy image --no-progress --exit-code 1 --severity HIGH,CRITICAL -o results.json devopsapps'
      }
    }
  }
}
