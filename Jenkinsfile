pipeline {
  agent any
  stages {
    stage('Build and install Contrast Assess Agent') {
      steps {
        sh '''
        cd DevopsClassFront
        docker build -t devopsapps-frontend .
        '''
      }
    }
    stage('Scan image using Trivy') {
      steps {
        sh '''
        trivy image --no-progress --severity HIGH,CRITICAL devopsapps-frontend
        '''
      }
    }
    stage('Scan image using Snyk') {
      steps {
        sh '''
        snyk-linux container monitor devopsapps-frontend --org=27b08c82-2fb9-4856-9b83-d2fcc25dcd66
        '''
      }
    }
  }
}
