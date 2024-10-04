# Models

Interface for interacting with tables in database

[Documentation](https://laravel.com/docs/11.x/eloquent)

[Relationships](https://laravel.com/docs/11.x/eloquent-relationships)

## Mass Assignment

Laravel by default blocks mass assignment

To enable for safe attributes, mark them as "fillable"

```php
class Chirp extends Model
 {
    protected $fillable = [
        'message',  // message enabled for mass-assignment
    ];
 }
```

## Get all Entries

`App\Models\Chirp::all();`

### Pagination

Getting all entries is inefficient, [pagination](https://laravel.com/docs/pagination) helps return a limited amount at a time