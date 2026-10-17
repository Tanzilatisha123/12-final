pipeline {
    agent any
   
    stages {
        stage('Run Selenium Tests with pytest') {
            steps {
                echo "Running Selenium Tests using pytest"

                // Install Python dependencies
                bat '"C:\\Users\\Tanzila\\AppData\\Local\\Python\\pythoncore-3.15-64\\python.exe" -m pip install -r requirements.txt'

                // Start Flask app in background
                bat 'start /B "C:\\Users\\Tanzila\\AppData\\Local\\Python\\pythoncore-3.15-64\\python.exe" app.py'

                // Wait a few seconds for the server to start
                bat 'ping 127.0.0.1 -n 5 > nul'

                // Run tests using pytest
                bat '"C:\\Users\\Tanzila\\AppData\\Local\\Python\\pythoncore-3.15-64\\python.exe" -m pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Build Docker Image"
                bat "docker build -t seleniumdemoapp:v1 ."
            }
        }

        stage('Docker Login') {
            steps {
                bat 'docker login -u tanzila123 -p Tan@90105'
            }
        }

        stage('push Docker Image to Docker Hub') {
            steps {
                echo "push Docker Image to Docker Hub"
                bat "docker tag seleniumdemoapp:v1 tanzila123/sample2026:seleniumtestimage"               
                bat "docker push tanzila123/sample2026:seleniumtestimage"
            }
        }

        stage('Deploy to Kubernetes') { 
            steps { 
                bat 'kubectl apply -f deployment.yaml --validate=false' 
                bat 'kubectl apply -f service.yaml' 
            } 
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
    }
}
