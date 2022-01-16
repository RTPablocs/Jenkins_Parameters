pipeline {
  agent any
  stages {
    stage('Greet') {
      steps {
        sh """
                        #/bin/bash
                        node main.js ${params.Name}
                        
                        """
      }
    }

    stage('Parallel') {
      parallel {
        stage('Parallel A') {
          steps {
            echo 'Parallel A'
          }
        }

        stage('Parallel B') {
          steps {
            echo 'Parallel B'
          }
        }

      }
    }

  }
  parameters {
    string(name: 'Name', description: 'Name parameter')
  }
}