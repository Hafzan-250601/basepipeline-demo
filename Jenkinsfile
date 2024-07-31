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
    stage('Scan image and upload findings to SecurityHub') {
      steps {
        sh '''
        trivy image --no-progress --severity HIGH,CRITICAL devopsapps-frontend
        '''
      }
    }
stage('Scan image using Snyk') {
      steps {
        sh '''
        cd DevopsClassFront
        echo 'Testing...'
        snykSecurity(
          snykInstallation: \'SnykImageScanning\',
          snykTokenId: \'organization-snyk-api-token\'
          '''
        )
      }
    }
  }
}
