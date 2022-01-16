pipeline {
    agent any
    parameters {
        string(name: 'Name', defaultValue:'Pepe', description:'Name parameter')
    }
    stages {
        stage('Greet'){
            steps {
                echo "Hello: ${params.Name}"
            }
        }
    }
}