pipeline {
  agent any

  stages {
    stage('A'){
      steps {
        sh """
          #/bin/bash
          node jenkinsScripts/processA.js ${params.A}
        """
      }
    }
    stage('B'){
      steps {
        sh """
          #/bin/bash
          node jenkinsScripts/processB.js ${params.B}
        """
      }
    }
    stage('Result'){
      steps {
        sh """
          #/bin/bash
          node jenkinsScripts/result.js
        """
      }
    }
    

  }
  parameters {
    string(name: 'A', description: 'A parameter')
    string(name: 'B', description: 'B parameter')
  }
}