# Laravel

## Install and Create Project

Do manually or use a [starter kit](https://laravel.com/docs/11.x/starter-kits)

Manually
1. Download PHP and Composer
   - (optional) Use [Laravel Herd](https://herd.laravel.com) for quick start 
2. Create Laravel project
   - `composer create-project laravel/laravel example-app`
   - or globally install [Laravel installer](https://github.com/laravel/installer)
      ```console
      composer global require laravel/installer
      laravel new example-app
      ```
   - or use [Herd](https://herd.laravel.com/docs/1/getting-started/sites)
      ```console
      cd ~/Herd
      laravel new my-new-site
      cd my-new-site
      herd open
      herd edit
      ```
3. Launch Local Server 
   - using Laravel Artisan's `serve` command and access at `https://localhost:8000`
   ```console
   cd example-app
   php artisan serve
   ```

## Docker & Laravel Sail

Use [Laravel Sail](https://laravel.com/docs/11.x/sail) to run Laravel project using Docker

Sail provides a way to run PHP, Artisan, Composer, and Node commands

```console
./vendor/bin/sail php --version
./vendor/bin/sail artisan --version
./vendor/bin/sail composer --version
./vendor/bin/sail npm --version

# or sail php --version (if you have the )
```

