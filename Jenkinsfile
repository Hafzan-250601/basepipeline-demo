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
        sh 'trivy image --format template --template asff.tpl -o report.asff --severity HIGH,CRITICAL,MEDIUM devopsapps'
      }
    }
    stage('Upload Findings to SecurityHub') {
      steps {
        sh 'cat report.asff'
        sh 'jq . report.asff'
      }
    }
  }
}
