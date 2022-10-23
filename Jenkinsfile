pipeline{
	agent any
	stages{
	stage("Setup virtual environment")
	{
	steps{
		sh '''
		chmod +x envsetup.sh
		./envsetup.sh
		'''		
	}
	}
	stage("Gunicorn Setup")
	{
	steps{
		sh '''
		chmod +x gunicorn.sh
		./gunicorn.sh
		'''
	}
	}
	stage('setup NGINX')
	{
	steps{
		sh '''
		chmod +x nginx.sh
		./nginx.sh
		'''
	}
	}
	}
}
