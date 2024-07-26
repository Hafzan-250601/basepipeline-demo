pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh '''
        cd DevopsClassFront
        docker build -t devopsapps .
        '''
      }
    }
    stage('Scan') {
      steps {
        sh '''
        cd trivy
        trivy image --format template --template "@contrib/asff.tpl" -o report.asff --severity HIGH,CRITICAL devopsapps
        '''
      }
    }
    stage('Upload Findings to SecurityHub') {
      steps {
        sh '''
        cat report.asff | jq \'.Findings\'
        aws securityhub batch-import-findings --findings report.asff
        '''
        }
      }
    }
  }
