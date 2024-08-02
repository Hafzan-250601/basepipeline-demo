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
    stage('Download Latest Contrast Agent') {
      steps {
        contrastAgent profile: 'Contrast-Integration', outputDirectory: env.WORKSPACE, agentType: 'Node'
      }
    }
    stage('Scan image using Trivy') {
      steps {
        sh '''
        trivy image --no-progress --severity HIGH,CRITICAL devopsapps-frontend
        '''
      }
    }
  }
}
