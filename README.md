# Simple Personal Site

Create your personal website in minutes! Follow instructions below to set up.

## Table of Contents

<!-- MarkdownTOC -->

- [Features](#features)
- [Get started](#get-started)
	- [Configure site](#configure-site)
	- [SSL Certificate](#ssl-certificate)
- [Install](#install)
	- [Install directly](#install-directly)
	- [Install with Docker](#install-with-docker)
- [Manage content](#manage-content)
- [License](#license)

<!-- /MarkdownTOC -->

## Features

- Easy to manage site content 
- Markdown support throughout the site
- Post blog articles
- Create project cards 
- Supports video embed and images in blog articles and project cards
- Contact page with social media links and a message form

## Get started

Clone this project and enter project directory.
```bash
git clone https://github.com/chrisx8/simple-personal-site.git
cd simple-personal-site
```

### Configure site

- Generate a strong password [here](https://strongpasswordgenerator.com/) for database. Save it, as you'll need it during the setup process.
- Create your site config file.
```bash
cp simple_personal_site/site_config.example.py simple_personal_site/site_config.py
```
- Edit it, following instructions in the file.
- Generate your own icons [here](https://realfavicongenerator.net). Download the generated Favicon package.
- Unzip the downloaded package, and upload everything to `simple-personal-site/static/icons/`, replacing ALL existing placeholder icon files.
- Upload a logo (in `.png` format) to `simple-personal-site/static/images/`, replacing the existing `logo.png`

## Install

### Install with Docker

- Make sure you're in the project directory `simple-personal-site/`.
- Make sure you have a database accessible from inside the container  
- Build your image
```bash
docker build -t simple-personal-site .
```
- Run Docker container.
```bash
docker run -d -p 80:8000 -v uploads:/app/uploads/ -v static:/app/static/ --name simple-personal-site simple-personal-site:latest
```
- Create an admin account.
```bash
docker exec -it simple-personal-site python3 manage.py createsuperuser
```
- See `samples/` for sample Nginx configurations and `docker-compose.yml`

### Install directly

- Make sure `python3` and `pip` is installed.
- Make sure you're in the project directory `simple-personal-site/`.
- Install project dependencies.
```bash
# On Ubuntu/Debian
sudo apt-get install python3-dev libmysqlclient-dev
sudo python3 -m pip install -r requirements.txt
# On CentOS
sudo yum install rh-python36-python-devel mariadb-libs
sudo python3 -m pip install -r requirements.txt
```
- Create system service
Create service file with `nano` or another text editor
```bash
sudo nano /etc/systemd/system/multi-user.target.wants/personal-site.service
```
Paste in the following, and edit accordingly
```
[Unit]
Description=Simple Personal Site
After=network.target

[Service]
Type=simple
User=[YOUR USERNAME]
WorkingDirectory=[PROJECT DIRECTORY]
ExecStart=gunicorn simple_personal_site.wsgi:application -b 127.0.0.1:8000
Restart=on-failure

[Install]
WantedBy=multi-user.target
```
- Activate and start service
```bash
sudo systemctl daemon-reload
sudo systemctl enable personal-site
sudo systemctl start personal-site
```
- Create an admin account.
```bash
python3 manage.py createsuperuser
```
- Configure Nginx to reverse-proxy this application with `proxy_pass http://localhost:8000;`. Sample config is available at `samples/nginx/personal-site.conf`.

## Manage content

- Make sure port 80 and 443 are allowed in firewall settings.
- Access the management portal at `/manage/`
- Log in with the admin account you just created.
- Create a homepage by clicking `Add` next to `Homepages` on the management portal. Fill out the About Me section and save.<br>
  **NOTICE: Only the latest homepage object is recognized.**
- Create other items as needed.

**Congratulations! Now you have your personal site!**

## License

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
[GNU General Public License](LICENSE) for more details.

Copyright (C) 2019 [Chris Xiao](https://github.com/chrisx8)
