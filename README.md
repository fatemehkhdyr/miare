# miare

Evaluation task for miare backend developer.

Use the following commands to run:  
`python manage.py makemigrations `  
`python manage.py migrate `  
`python manage.py runserver `  
or using docker:  
`docker build -t miare:latest .`  
`docker run -d -p 8000:8000 --name miare_server miare:latest`