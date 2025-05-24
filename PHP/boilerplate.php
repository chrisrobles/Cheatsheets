<?php
/**
 *
 * This script sets up a PHP environment for debugging, autoloading classes, and starting a session.
 * It then outputs a simple "Hello, World!" message.
 *
 * Configuration:
 * - Enables the display of errors and startup errors for debugging purposes.
 * - Sets the error reporting level to report all errors.
 *
 * Autoloading:
 * - Registers an autoloader function that includes class files based on the class name.
 *
 * Session:
 * - Starts a new session or resumes an existing session.
 *
 * Output:
 * - Displays a "Hello, World!" message.
 */
// Display errors for debugging
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

// Autoload classes
spl_autoload_register(function ($class_name) {
    include $class_name . '.php';
});

// Start session
session_start();

// Your code starts here
echo "Hello, World!";
/**
 * This section demonstrates a simple example of setting and getting session variables.
 * It also includes a basic example of using an autoloaded class.
 */

// Set a session variable
$_SESSION['username'] = 'JohnDoe';

// Get the session variable
$username = $_SESSION['username'];

// Output the session variable
echo "Username: " . $username;

// Example of using an autoloaded class
// Assuming you have a class named 'User' in 'User.php'
$user = new User();
$user->setName('John Doe');
echo "User Name: " . $user->getName();