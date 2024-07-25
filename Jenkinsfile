pipeline {
  agent any
  options {
    buildDiscarder(logRotator(numToKeepStr: '5'))
  }
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