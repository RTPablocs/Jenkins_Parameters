pipeline {
  agent any

  stages {
    stage('A'){
      steps {
        sh """
          #/bin/bash
          python3 jenkinsScripts/processA.py ${params.A}
        """
      }
    }
    stage('B'){
      steps {
        sh """
          #/bin/bash
          python3 jenkinsScripts/processB.py ${params.B}
        """
      }
    }
    stage('Result'){
      steps {
        sh """
          #/bin/bash
          python3 jenkinsScripts/result.py
        """
      }
    }
    

  }
  parameters {
    string(name: 'A', description: 'A parameter')
    string(name: 'B', description: 'B parameter')
  }
}