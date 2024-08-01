# Apache

Open-source HTTP Server

## Check if module is installed

`$ dpkg -s libapache2-mod-wsgi`

## Check Loaded Modules

`$ apache2ctl -t -D DUMP_MODULES`

## httpd.conf



### mod_wsgi

[Installation](https://modwsgi.readthedocs.io/en/develop/installation.html)

mod_wsgi operates in 1 of 2 modes

1. embedded mode
2. daemon mode

Consult the [mod_wsgi](https://wsgi.readthedocs.io/en/latest/) documentation to determine which mode is right for your setup

#### embedded mode

- embed Python within Apache and loads Python code into memory when server starts
- code stays in memory throughout life of Apache process
- similar to mod_perl
- **significant performance gains**

#### daemon mode

Daemon
: program that runs in the background to handle tasks 

- spawns an independent daemon process that handles requests
- can run as a different user than the web server
  - potential **improved security**
- daemon process can be restarted without restarting apache web server
  - potential **better seamless codebase refresh**

