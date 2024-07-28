To enable PHP in Apache add the following to httpd.conf and restart Apache:
    LoadModule php7_module /opt/homebrew/opt/php@7.4/lib/httpd/modules/libphp7.so

    <FilesMatch \.php$>
        SetHandler application/x-httpd-php
    </FilesMatch>

Finally, check DirectoryIndex includes index.php
    DirectoryIndex index.php index.html

The php.ini and php-fpm.ini file can be found in:
    /opt/homebrew/etc/php/7.4/

php@7.4 is keg-only, which means it was not symlinked into /opt/homebrew,
because this is an alternate version of another formula.

If you need to have php@7.4 first in your PATH, run:
  echo 'export PATH="/opt/homebrew/opt/php@7.4/bin:$PATH"' >> ~/.zshrc
  echo 'export PATH="/opt/homebrew/opt/php@7.4/sbin:$PATH"' >> ~/.zshrc

For compilers to find php@7.4 you may need to set:
  export LDFLAGS="-L/opt/homebrew/opt/php@7.4/lib"
  export CPPFLAGS="-I/opt/homebrew/opt/php@7.4/include"

To start shivammathur/php/php@7.4 now and restart at login:
  brew services start shivammathur/php/php@7.4
Or, if you don't want/need a background service you can just run:
  /opt/homebrew/opt/php@7.4/sbin/php-fpm --nodaemonize