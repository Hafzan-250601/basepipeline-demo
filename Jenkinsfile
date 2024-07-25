pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'docker build -t devopsApps .'
      }
    }
    stage('Scan') {
      steps {
        sh 'trivy devopsApps'
      }
    }
  }
}
