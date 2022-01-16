pipeline {
    agent any
    parameters {
        string(name: 'Name', description:'Name parameter')
    }
    stages {
        stage('Greet'){
            steps {
                echo "Hello: ${params.Name}"
            }
        }
    }
}