# Simple Personal Site

Create your personal website in minutes! Follow instructions below to set up.

## Table of Contents

<!-- MarkdownTOC -->

- [Get started](#get-started)
- [Configure](#configure)
	- [Configure site](#configure-site)
	- [SSL Certificate](#ssl-certificate)
- [Install](#install)
	- [Install with Docker](#install-with-docker)
- [Manage content](#manage-content)
- [License](#license)

<!-- /MarkdownTOC -->

## Get started

- If you don't have a VPS already, get one. You can get one from [DigitalOcean (referral link)](https://m.do.co/c/4409c0c26a9c) for as low as $5/month.
- If you don't have a domain name, get one.
- SSH into your VPS and install all updates.
- Clone this project and enter project directory.
```bash
git clone https://github.com/chrisx8/simple-personal-site.git
cd simple-personal-site
```

## Configure

### Configure site

- Generate a strong password [here](https://strongpasswordgenerator.com/) for database. Save it, as you'll need it during the setup process.
- Create your site config file.
```bash
cp simple_personal_site/site_config.example.py simple_personal_site/site_config.py
```
- Edit it with your favorite text editor (such as `vim` or `nano`). Please read descriptions in the file.<br>
  Enter `postgres://personalsite:YOUR_PASSWORD@db:5432/personalsite` for the database URL if you're installing with Docker.
- Generate your own icons [here](https://realfavicongenerator.net). Download the generated Favicon package.
- Unzip the downloaded package, and upload everything to `simple-personal-site/static/icons/` with an SFTP client (such as Filezilla or WinSCP), replacing ALL existing placeholder icon files.
- Upload a logo (in `.png` format) to `simple-personal-site/static/images/`, replacing the existing `logo.png`

### SSL Certificate

- Get a free SSL certificate [here](https://www.sslforfree.com). Select `Manually Verify Domain (DNS)` as the validation method.
- Create a folder for certificates and set permission
```bash
mkdir ~/ssl
chmod 700 ~/ssl
```
- Put the certificate at `~/ssl/cert.pem`, and put the private key at `~/ssl/key.pem`

## Install

### Install with Docker

- [Install Docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/#upgrade-docker-ce-1).
- [Install Docker Compose](https://docs.docker.com/compose/install/)
- Make sure you're corrently in the project directory `simple-personal-site/`.
- Open `docker/docker-compose.yml` with a text editor, such as `nano` or `vim`, and the password you generated earlier in `POSTGRES_PASSWORD`
- Build images.
```bash
docker-compose -f docker/docker-compose.yml build
```
- Run Docker container.
```bash
docker-compose -f docker/docker-compose.yml up -d
```
- Create an admin account.
```bash
docker exec -it personal-site python3 manage.py createsuperuser
```

## Manage content

- Make sure port 80 and 443 are allowed in firewall settings.
- Access the management portal at `https://URL/manage/`
- Navigate to your VPS's IP or URL in a browser. You'll be prompted to enter the management portal.
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

Copyright (C) 2018 [Chris Xiao](https://github.com/chrisx8)
