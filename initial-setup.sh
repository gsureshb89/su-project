sudo apt-get-update -y

wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key |sudo gpg --dearmor -o /usr/share/keyrings/jenkins.gpg

sudo sh -c 'echo deb [signed-by=/usr/share/keyrings/jenkins.gpg] http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'

sudo apt update
sudo apt install jenkins


sudo systemctl daemon-reload
sudo systemctl start jenkins

sudo systemctl start nginx
sudo systemctl enable nginx
sudo systemctl enable jenkins
sudo systemctl status jenkins


