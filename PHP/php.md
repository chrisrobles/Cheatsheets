# PHP

## Superglobals

Variables related to the request from the client

- `$GLOBALS`
- `$_SERVER`
- `$_GET`
  - query parameters from the URL
- `$_POST`
  - variables passed from a form submission using the "POST" method
  - variables are stored in the headers of the HTTP request instead of URL
- `$_FILES`
- `$_COOKIE`
- `$_SESSION`
- `$_REQUEST`
  - contains `$_GET`, `$_POST`, `$_COOKIE`
- `$_ENV`