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
    stage('Scan image and upload findings to SecurityHub') {
      steps {
        sh '''
        cd trivy
        trivy image --format template --template "@contrib/asff.tpl" -o report.asff --no-progress --severity HIGH,CRITICAL devopsapps
        cat report.asff | jq \'.Findings\'
        aws securityhub batch-import-findings --findings report.asff
        '''
      }
    }
      }
    }
