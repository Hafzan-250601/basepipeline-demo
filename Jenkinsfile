pipeline {
  agent any
  options {
    buildDiscarder(logRotator(numToKeepStr: '5'))
  }
  stages {
    stage('Build') {
      steps {
        sh 'cd /DevopsClassFront'
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