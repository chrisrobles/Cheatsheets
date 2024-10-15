# Bash Shell

## Customize

<https://www.howtogeek.com/307701/how-to-customize-and-colorize-your-bash-prompt/>

## nano

- nano +12 file
  - Goes to line 12

- Go to beginning of line
  - ctrl+a

- Go to end of line
  - ctrl+e

### Configure

<https://www.linuxhowtos.org/System/config_nano.htm>

## Apachectl -k __ (Debian)

apache recommends apachectl -k vs service

stop
: kills all of its threads and exits

graceful (equivalent to service apache2 reload)
: advise it threads to exit when idle, then apache reloads the configuration (it doesn't exit itself)

restart (equivalent to service apache2 stop; service apache2 start)
: kills all of its threads, then the apache reloads the configuration file, rather than killing itself (similar to graceful)

graceful-stop
: like graceful, but instead of reloading the configuration, it will stop responding to new requests

## systemctl vs service

systemctl
- "low-level"
- higher control

service
- "high-level"
- abstracts various service managers
   - service redirects to systemctl on centos7

get loaded php configuration
1) `sudo -i`
2) `php --ini`
3) Get location of `Loaded Configuration File`
4) If there is a cli listed in path, php is loaded for command line interface

## Change cl php version

1) `cd /usr/bin`
2) `php -v`
3) `mv php php` then add x.y version number from step 2
4) `mv phpx.y php`
5) `php -v`

## Check What Is Using Port

```terminal
lsof -i :8000
kill -9 <PID>
```

## Find directory

`find . -type d | grep DIRNAME`

## Permissions

```text
a b  c  d
_ _  _  _
-rw-r--rwx
 420400421
  6  4  7
```
- a: Represents type
  - \- = regular file
  - d = directory
- b: Owner permissions
- c: Group permissions
- d: Other permissions


- rwx
  - read
  - write 
  - execute

## Create File

```touch fileName.sh```

## Find file 

`find . -type f "*.sh"`
- . = current dir
- -type f  = text based file
- *.sh = all files ending in .sh

## mkdir

- Make all the required directories in the path
  `mkdir -p exists/new/new/new`

## MacOS Installing Binaries

Binary = Commands = Executable Files

Enable Global
- `mv file /usr/local/bin/file`

Enable for user (dont require root permissions)
- `mv file ~/.local/bin/file`

```text
The Symfony CLI was installed successfully!

Use it as a local file:
  /Users/chris/.symfony5/bin/symfony

Or add the following line to your shell configuration file:
  export PATH="$HOME/.symfony5/bin:$PATH" # (chris) expires when terminal is closed

Or install it globally on your system:
  mv /Users/chris/.symfony5/bin/symfony /usr/local/bin/symfony #makes executable runnable from anywhere on the system

Then start a new shell and run 'symfony'
```

## Alias

Store shell commands in a variable

`alias sail='sh $([ -f sail ] && echo sail || echo vendor/bin/sail)'`