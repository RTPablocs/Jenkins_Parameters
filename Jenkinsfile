pipeline {
    agent any
    parameters {
        string(name: 'Name', description:'Name parameter')
    }
    stages {
        stage('Greet'){
            steps {
                sh """
                #/bin/bash
                node main.js ${params.Name}
                
                """
            }
        }
    }
}