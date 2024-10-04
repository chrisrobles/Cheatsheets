# Laravel Artisan

## Start Local Development Server

`php artisan serve`

Application accessible at `https://localhost:8000`

## Create Model, Migration, and Controller Quick

`php artisan make:model`
- -mrc: model, migration, and resource controller
  - `app/Models/my-model.php`
  - `database/migrations/<timestamp>_create_my-model_table.php`
  - `app/Http/Controllers/ChirpController.php`
- -help: see all available options

## Show All Routes

`php artisan route:list`

## Show All Tables

`php artisan db:show`

## Show Table Details

`php artisan db:table users`

## Migrate Database

`php artisan migrate`

### Rebuild database from scratch

`php artisan migrate:fresh`

## Tinker

[Documentation](https://laravel.com/docs/11.x/artisan#tinker)

A REPL for PHP code in your Laravel application

`php artisan tinker`

## Make

### Model Policy

`php artisan make:policy ChirpPolicy --model=Chirp`

### Notification

`php artisan make:notification NewChirp`

### Event

`php artisan make:event ChirpCreated`

### Listener

`php artisan make:listener SendChirpCreatedNotifications --event=ChirpCreated`

## Begin Processing Queued Jobs

`php artisan queue:work`