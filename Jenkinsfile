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
        sh 'trivy image -f json -o results.json --no-progress --exit-code 0 --severity HIGH,CRITICAL devopsapps'
        sh 'cat results.json'
      }
    }
  }
}
