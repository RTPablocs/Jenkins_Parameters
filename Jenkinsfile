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

      parallel {

        stage('Stage A') {
          steps {
            echo 'Paralel A Message'
          }
        }

        stage('Stage B') {
          steps {
            echo 'Paralel A Message'
          }
        }

      }
    }
        }
  parameters {
    string(name: 'Name', description: 'Name parameter')
  }
}