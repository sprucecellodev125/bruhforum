---
description: You need to install something tho
---

# Installing software

#### Python and pip

```bash
sudo apt update
sudo apt upgrade
sudo apt install python3 python3-pip build-essential
```

#### MySQL

```bash
sudo apt install mariadb-server mariadb-client
```

#### (Optional, if you use it on Linux VPS or Bare metal)

See [https://www.digitalocean.com/community/tutorials/how-to-deploy-python-wsgi-applications-using-uwsgi-web-server-with-nginx](https://www.digitalocean.com/community/tutorials/how-to-deploy-python-wsgi-applications-using-uwsgi-web-server-with-nginx)

Note: the path of WSGI file is `bruhforum/wsgi.py`
