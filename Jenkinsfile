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
        pwd
        ls
        trivy image --format template --template trivy/contrib/asff.tpl -o report.asff --severity HIGH,CRITICAL,MEDIUM devopsapps
        '''
      }
    }
    stage('Upload Findings to SecurityHub') {
      steps {
        sh 'cat report.asff | jq \'.Findings\''
      }
    }
  }
}
