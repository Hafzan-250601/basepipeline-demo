pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'sudo usermod -aG docker ubuntu'
        sh 'su - ubuntu'
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
