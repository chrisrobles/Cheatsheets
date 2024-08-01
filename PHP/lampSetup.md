# LAMP Setup on Debian

To help someone on a Debian based Linux distro (specifically Ubuntu)

## Ubuntu

### Ubuntu vs CentOs

- Ubuntu
  - most popular distro of linux
  - for desktop
  - easy
  - good selection of packages
  - apache2 web server
- CentOs
  - for web servers
  - packages lag behind
  - command line based
  - httpd web server

### Installing Ubuntu

- Use the LTS version of Ubuntu
  - for free support and security updates
- Using bare metal?
  1) rufus.ie
  2) Download to usb
  3) Move ubuntu .iso file to usb ?
- Using a VM?
  - Pros
    - more access to software
    - possible driver problems with Linux
  - Cons
    - performance
    - On a Mac with a VM
      - Use Parallels Desktop

1) Download ubuntu manually
2) Installation Type
    1) Check `Erase disk`
    2) Click `Advanced features...`
    3) Toggle `Use LVM`
        - This makes it easier to mess around with partitions later on
    4) (Optional) Check `Encrypt the new Ubuntu`

## Package Manager

Package manager installs and updates packages from the added repositories

### Composer

Download composer
1) go to "getcomposer.org/download"
2) Scroll down to "Manual Download"
3) Right click the top version and copy link address
4) Open terminal
5) `sudo -i`
6) `wget -O /usr/local/bin/composer https://getcomposer.org/download/2.1.9/composer.phar`
7) `chmod +x /usr/local/bin/composer`
8) `exit`
9) `cd /var/www/html`
10) `composer install` should work
11) `vendor/` folder will have been created if worked

## PHP

### Get version

`php -v`

### Get list of php packages 

`php -m`
`dpkg -l | grep php7.1 | awk '{print $2}' | xargs` on Debian (Ubuntu)

### Download PHP

`sudo apt install php7.1`

### Download PHP Packages

`sudo apt install php7.1-common php7.1-fpm php7.1-gd php7.1-imap php7.1-mbstring php7.1-mysql php7.1-ldap php7.1-mcrypt php7.1-intl php7.1-xml php7.1-xmlrpc php7.1-imagick libapache2-mod-php7.1 libapache2-mod-fcgid -y`

- LDAP is for microsoft access controls
- fpm provides the Fast Process Manager interpreter that runs as a daemon and receives Fast/CGI requests
- mysql connects php to the mysql database
- libapache2-mod-php7.1 provides the php module for the apache web server
- libapache2-mod-fcgid contains a mod_fcgid that starts a number of cgi program instances to handle concurrent requests

### Add the main ppa for php

PPA (Personal Package Archive)
- contains PHP packages with updated versions not available in default repositories

1) google "sury php repo ubuntu"
2) click the link (launchpad.net)
3) copy `sudo add-apt-repository ppa:ondrej/php` from the site
   - "add-apt-repository" Adds to the apt package manager a repository
   - "ppa:ondrej/php" the php  maintained by Ondrej
   - Apt package manager installs and updates packages from the added repositories
4) paste into terminal and run and hit enter when asked

### Configure PHP ini

php.ini = php configuration file

1) `cd /etc/php/7.1/apache2/`
2) `nano php.ini` then `ctrl+w` to find line and change
   1) `memory_limit = 1G` or 2GB
   2) `max_input_vars = 10000`
   3) `max_execution_time = 300`
   4) `post_max_size = 0`
   5) `upload_max_filesize = 1G`

### Enable PHP as apache mod

Make PHP usable by apache2

`a2enmod php7.1`



## Database

MYSQL has become commercial and not as user friendly, MariaDB is a better alternative

### Download MariaDB

`sudo apt install mariadb-server`

#### Download MariaDB according to James (DEPRECATED)

1) Google "mariadb ubuntu repo"
2) Click `Setting up MariaDB Repositories` link
3) Click `Ubuntu`
4) Choose ubuntu version
5) Choose oldest stable version
6) Choose mirror that is geographically closest
7) Copy and paste the `commands to run to install MariaDB`
    - `software-properties-common` lets you run more than one version of things
    - `apt-key adv --fetch-keys` helps verify that what you are downloading is what it says it is
    - `add-apt-repository 'deb ...` downloads MariaDB
8) `sudo apt update` (refreshes the systems knowledge of what packages are out there)
9) `sudo apt install mariadb-server` installs MariaDB
10) `cd` takes to the root directory represented by `~`
11) `nano .my.cnf`
12) Add (8:32 in video)

    ```nano
    [client]
    user=root
    password=YOUR_PASSWORD
    ```

13) Save
14) Do steps 10-13 for your user profile as well
- `13` This allows for us to just type `mysql` in the terminal without having to put user and password every time

### Enable MariaDB to start on Boot

`systemctl enable mariadb` 

### Create User

1) `mariadb`
2) `USE mysql;`
3) `CREATE USER 'christian'@'localhost' IDENTIFIED BY 'YOUR_PASSWORD';`
4) `GRANT ALL PRIVILEGES ON *.* TO 'christian'@'localhost';`
5) `FLUSH PRIVILEGES;`

### Update User Password

`SET PASSWORD FOR 'christian'@'localhost' = PASSWORD('YOUR_PASSWORD');`

### Set Default MySQL Login

1) `cd` (goes to `~`)
2) `nano .my.cnf`
3) Add info
    ```nano
    [client]
    user=root
    password=YOUR_PASSWORD 
    ```

### Download DB

1) mysqldump {DATABASE} --ignore-table={TABLE_NAME} -u {USER} -p | gzip > mydb.sql.gz
2) (optional) scp user@server.name:/path/to /path/to
3) mysql {TABLE} < mydb.sql.gz -u {USER} -p



## Apache Setup

Get websites running on a Linux Desktop

- `apache2.conf`
  - master configuration file
- `sites-available/`
  - all the site related configurations
- `sites-enabled/`
  - symlinks to the sites-available sites that you want enabled
- `mods-available/` and `mods-enabled/` 
  - apache mods
- `conf-available/` and `conf-enabled/`
  - miscellaneous config files

### Configure sites-available / enabled

Create site configuration
1) `sudo -i`
2) `cd /etc/apache2/sites-available`
or `cd /etc/httpd/conf`
3) `mkdir /var/www/mySite`
4) Create a YOUR_SITE.conf file
5) `nano YOUR_SITE.conf` or `nano httpd.conf`
6) Paste in
    ```nano
    <VirtualHost *:80>
        ServerName mySite.local
        ServerAdmin webmaster@localhost
        DocumentRoot /var/www/mySite
        
        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined

        <Location />
            AllowOverride All
            Require all granted
        </Location>
    </VirtualHost>
    <VirtualHost *:443>
        ServerName mySite.local
        ServerAdmin webmaster@localhost
        DocumentRoot /var/www/mySite
        
        SSLEngine On
            SSLCertificateFile /etc/apache2/ssl/certificate.crt
            SSLCertificateKeyFile /etc/apache2/ssl/private.key

        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined

        <Location />
            AllowOverride All
            Require all granted
        </Location>
    </VirtualHost>
    ```
   - Explanation
      - `<VirtualHost *:443>` is website virtual host and the port number to attach it to
         - 80=http 443=https
      - `ServerName mySite.local` domain name
      - `ServerAdmin webmaster@localhost` doesnt matter what email address is put
      - `DocumentRoot /var/www/mySite` the directory apache looks for the files
      - `SSLEngine On` tells apache this is running over https
      - `SSLCertificateFile /etc/apache2/ssl/certificate.crt` need certificate for https
      - `SSLCertificateKeyFile /etc/apache2/ssl/private.key` need key for https
      - `ErrorLog ${APACHE_LOG_DIR}/error.log` where apache log files will go
      - `CustomLog ${APACHE_LOG_DIR}/access.log combined` access log parameter, combined = format of the file
      - `<Location />` location block, specific to apache 2.4 not in 2.2 which is used on LV.Net
      - `AllowOverride All` allows you to override some Apache settings via a .htaccess file you can place in a directory
      - `Require all granted`

Enable site from sites-available
1) `a2dissite 000-default.conf` disable the 000-default site created by apache (dont do if using that site)
2) `a2ensite YOUR_SITE` enables the site by creating the symlink in sites-enabled
3) `sudo service apache2 stop`
4) `sudo service apache2 start` has apache load the new changes
5) `cd /etc/apache2/sites-enabled`
6) `ls -lah` should show the conf files that were enabled
[Configure multiple sites](https://www.liquidweb.com/kb/configure-apache-virtual-hosts-ubuntu-18-04)

### Configure Apache

1) `sudo -i`
2) `cd /etc/apache2`
3) `apachectl configtest` makes sure the configuration is good
   1) If `Invalid Command 'SSLEngine'` error
      1) `apt install mod_ssl` (only on centos)
          1) If `E: dpkg was interrupted`, run `dpkg --configure -a`
4) `a2enmod ssl`
5) `a2enmod rewrite` install rewrite mod
6) `apachectl configtest` not including ssl problems

### Set up SSL Cert

1) `sudo -i`
2) `cd /etc/apache2/`
3) `mkdir ssl`
4) `cd ssl`
5) Google "openssl command to generate self signed certificate and key"
6) Go to stack overflow link
7) Copy something along the lines of
   `openssl req -x509 -newkey rsa:4096 -keyout private.key -out certificate.crt -days 3650 -nodes` -nodes skips the password
8) Paste into terminal and run
     1) `Common Name []: mySite`
9) `apachectl configtest` looking for a "Syntax OK"

### Apache AllowOverride

1) `sudo -i`
2) `cd /etc/apache2`
3) `grep -r AllowOverride *`
4) Make sure all places that say `AllowOverride None` say `AllowOverride All`
   1) `sed -i 's/AllowOverride None/AllowOverride All/g' apache2.conf`
   2) Do the same thing for any files in an enabled folder (sites-enabled,conf-enabled,mods-enabled)

### Configure multiple php versions for each site

[Tutorial](https://www.digitalocean.com/community/tutorials/how-to-run-multiple-php-versions-on-one-server-using-apache-and-php-fpm-on-ubuntu-18-04)
`systemctl enable php7.1-fpm`
`systemctl enable php7.4-fpm`

### Start Apache Server

1) `sudo -i`
2) `systemctl enable apache2` tells system to boot apache2 with boot sequence
3) `service apache2 start` starts apache2 right now
4) `service apache2 restart` just in case apache2 was already running
5) `lsof -i :80` tells us if anything is listening or communicating on port 80
6) `lsof -i :443`
7) Should see apache2 listening on both ports

### Setup system handling of local domain name

1) `sudo -i`
2) `nano /etc/hosts`
   1) Go down to 127.0.0.1
   2) `ctrl+e` to go to end of line
   3) Add mySite `localhost mySite` domain name after localhost and add subsequent urls after mySite



## Linux Utilities

### Install widely used Linux Utilities

1) `sudo -i`
2) `apt install screen curl wget lso`

## Git

### Get Git

1) `sudo -i`
2) `apt install git`
3) `exit`

### Setup ssh key

1) Make sure to be the user, not sudo
2) `ssh-keygen`
3) Put a passphrase in
4) Hit enter through everything else
5) `eval "$(ssh-agent -s)"` Start the ssh-agent
   - [May need to use different command](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?platform=linux#adding-your-ssh-key-to-the-ssh-agent)
6) Add ssh key to ssh-agent
  `ssh-add ~/.ssh/id_ed25519`

### Add key to git labs

1) `cat ~/.ssh/id_ed25519.pub | xclip -selection clipboard` to copy ssh key
   - rsa `cat ~/.ssh/id_rsa.pub | xclip -selection clipboard`
   - Share key only that is in `~/.ssh/id_rsa.pub` file
2) Go to git.lv.net
3) Go to account settings in top right
4) Go to ssh keys
5) Paste in ssh key

### Get code locally

1) Go to project repository on git.lv.net
2) Click clone
3) Copy text under `Clone with SSH`
4) `sudo -i`
5) `mkdir /var/www`
6) `chown christian:christian /var/www`
7) `exit`
8) `cd /var/www`
9) `git clone` then paste in text from git labs

## Symfony

Install

```terminal
wget https://get.symfony.com/cli/installer -O - | bash
```

## PHPStorm

- highlights spelling errors
- matches open and closing braces
- highlights sql code
- show object source from highlight
- Code inspection when right click file and click `Inspect Code...`
- Code completion
  - Show all variables that exist in the scope by typing $
  - show all the static methods by typing self::