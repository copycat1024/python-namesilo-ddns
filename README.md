# python-namesilo-ddns
Simple DNS updater for NameSilo using NameSilo's API. Written in Python 3.

### About
This program is a Python script used to automatically update your DNS records on NameSilo's nameserver using their API.

### Installation and Usage

#### Usage

The script will automatically configurate the DNS record of your domain names on NameSilo nameservers to point at the public IP of the machine it is ran on.

Example:
- Domain name: `'mysite.com'`
- Subdomain: `['www', 'api', 'blog']`
- Public IP: 22.22.22.22

Before:

| Type   | Value                  | Hosts            |
|--------|------------------------|------------------|
| CNAME  | `'api.othersite.com'`  |`'api.mysite.com'`|
| A      | 33.33.33.33            |`'www.mysite.com'`|

After:

| Type   | Value                  | Hosts             |
|--------|------------------------|-------------------|
| A      | 22.22.22.22            |`'api.mysite.com'` |
| A      | 22.22.22.22            |`'www.mysite.com'` |
| A      | 22.22.22.22            |`'blog.mysite.com'`|

#### Installation
This program is designed to run on Debian 9 "Stretch".

1. Install Python 3, pip and venv
On Debian:
```bash
apt install python3  python3-pip  python3-venv
```

2. Clone the repository and run setup.sh
```bash
git clone https://github.com/copycat1024/python-namesilo-ddns.git ddns
cd ddns
chmod +x setup.sh
./setup.sh
```

3. Create config.py
A file named `config.py` needs to be created in the repository directory to hold configuration data for the script. A file name `config.demo.py` is as a demo format file for the config file. You can copy this file into `config.py` and use your favorite text editor to edit it. The file contain three parameters:

* Your api key, which can be obtained from https://www.namesilo.com/account_api.php
* Your domain name, such as `'example.com'`
* A list of host names to be managed for your domain name, such as `['www', 'api', 'blog']`

4. Run run.sh to execute the program
```bash
./run.sh
```
