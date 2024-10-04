# Database

Database configuration is in `.env`

## Switch DB Driver

1. Update the `DB_*` variables in `.env`
2. Create database
3. Run application's [database migrations](https://laravel.com/docs/11.x/migrations)
    ```console
    php artisan migrate
    ```

## Migrations

[Documentation](https://laravel.com/docs/11.x/migrations)

Create and modify tables

Ensures the same database structure exists everywhere that application runs

## Cursor

Avoid loading everything into memory with a [database cursor](https://laravel.com/docs/eloquent#cursors)