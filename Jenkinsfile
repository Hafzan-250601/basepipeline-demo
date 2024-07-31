pipeline {
  agent any
  stages {
    stage('Build Frontend') {
      steps {
        sh '''
        cd DevopsClassFront
        docker build -t devopsapps-frontend .
        '''
      }
    }
    stage('Build Backend') {
      steps {
        sh '''
        cd DevopsClass
        docker build -t devopsapps-backend .
        '''
      }
    }
    stage('Scan image and upload findings to SecurityHub') {
      steps {
        sh '''
        trivy image --no-progress --severity HIGH,CRITICAL devopsapps-frontend
        '''
      }
    }
stage('Scan image using Snyk') {
      steps {
        echo 'Testing...'
        snykSecurity(
          snykInstallation: 'SnykImageScanning',
          snykTokenId: 'organization-snyk-api-token'
        )
      }
    }
  }
}
