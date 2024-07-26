pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'docker build -t devopsapps .'
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
        sh 'cat report.asff | jq \'.Findings\''
        script {
          def findings = sh(script: 'cat report.asff', returnStdout: true).trim()
          sh "aws securityhub batch-import-findings --findings '${findings}'"
        }
      }
    }
  }
}
