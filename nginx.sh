#!/bin/bash
sudo cp -rf app.conf /etc/nginx/sites-available
chmod 710 /var/lib/jenkins/workspace/django-cicd
sudo ln -s /etc/nginx/sites-available /etc/nginx/sites-enabled
sudo nginx -t

sudo systemctl start nginx
sudo systemctl enable nginx

echo "Nginx started"

sudo systemctl status nginx

