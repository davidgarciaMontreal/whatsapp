pipeline {
  agent any
  stages {
    stage('pre-phase') {
      parallel {
        stage('pre-phase') {
          steps {
            sh '''pwd
echo "hello"
ls -tlrh'''
          }
        }
        stage('pre-phase2') {
          steps {
            sleep 10
          }
        }
      }
    }
    stage('test-phase') {
      steps {
        sh 'echo "testing"'
      }
    }
  }
}