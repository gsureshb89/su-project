#!/bin/bash
sudo cp -rf herodashboard_server.conf /etc/nginx/conf.d
chmod 710 /var/lib/jenkins/workspace/django-cicd
sudo ln -s /etc/nginx/sites-available /etc/nginx/sites-enabled
sudo nginx -t

sudo systemctl start nginx
sudo systemctl enable nginx

echo "Nginx started"

sudo systemctl status nginx

