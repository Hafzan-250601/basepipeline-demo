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
    stage('Scan image using Trivy') {
      steps {
        sh '''
        trivy image --no-progress --severity HIGH,CRITICAL devopsapps-frontend
        '''
      }
    }
    stage('Scan image using Snyk Container') {
      steps {
        snykSecurity(
          snykInstallation: 'SnykImageScanning',
          snykTokenId: 'organization-snyk-api-token',
        )
      }
    }
  }
}
