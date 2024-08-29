# Javascript

`<script src="js/main.js"></script>`

## Console Log

```js
console.log(“...” + variable + “ending element”);//interpolation

console.log(“...”, “ending element”);
```

## Variables

let myVar = ...
- Scoped to the block they are in (if statement, function, for loop, ...)
- Cant be redeclared in the same scope

var myVar = ...
- Scoped to the function its declared in or globally scoped if not inside a function
- Can be redeclared in the same scope

### Check type

```js
if(typeof num === "Number")
      this._numberOfStudents = num;
    else
      console.log("Invalid input: numberOfStudents must be set to a Number.")
```

## Dialog

### Confirm

`confirm(“Ready?”);//creates a pop up box with an ok and cancel button`

### Prompt

`prompt(“What is your name?”);//creates a pop up with an input field`

## Condition Statements

```js
if (condition) {
}

else if (condition) {
}

else {
}
```

## Inline operators \

'chris\’s house' //escaping

“chris’s \nhouse” //new line operator

## Switch statement

```js
var moonPhase = 'full';
switch (moonPhase) {
  case 'full':
    console.log('Howwwwlll!!');
    break;
  case 'mostly full':
    console.log("Arms and legs are getting hairier");
    break;
  case 'mostly new':
    console.log("Back on two feet");
    break;
  default:
    console.log('Invalid moon phase');
    break;
}
```

## Functions

```js
var orderCount = 0;
function takeOrder(topping, crustType) {
  console.log('Order: ' + crustType + ' pizza topped with ' + topping);
  orderCount = orderCount + 1;
}
```

## Arrays & Strings

```js
var bucketList = ['jump', 'run', 'sleep'];
var listItem = bucketList[2];
```
- adding to an array will return the length

### add

`bucketList.push('dance');`

### Remove Multiple Elements

`var removedItem = bucketList.splice(startingIndex, numberOfItemsToRemove);`

### Copy

`var bucketListCopy = bucketList.slice();`

### Substring

`“word”.substring(x, y);//x = where you start chopping y=where you stop(doesn’t include)`

### Filter

Foreach item in collection, keep it if it matches condition
```js
const getDataByRole = role => {
  return salaryData.filter(obj => obj.role === role);
}
```

### Map

Foreach item in collection, apply same function
```js
const allSalaries = salaryData.map(obj => obj.salary);
```

## Loops

### For & Foreach Statement
```js
var vacationSpots= ['LA', 'Hawaii', 'France'];

// For
for (var i = 0; i < vacationSpots.length; i++) {
  console.log('I would love to visit ' + vacationSpots[i]);
}

// Foreach
vacationSpots.forEach(function(spot) {
  console.log('I would love to visit ' + spot);
});
// Foreach (one line)
vacationSpots.forEach(spot => console.log('I would love to visit '+ spot));
```

### While Statement

```js
var cards = ['Diamond', 'Spade', 'Heart', 'Club'];

var currentCard = 'Heart';
while (currentCard !== 'Spade') {
  console.log(currentCard);
  var randomNumber = Math.floor(Math.random() * 4);
  currentCard = cards[randomNumber];
}
alert('Found a Spade!');
```

## Classes

```js
class Dog {
  constructor(name) {
    this._name = name;  // underscores in names means dont access directly
    this._behavior = 0;
  }

  get name() {
    return this._name;
  }
  get behavior() {
    return this._behavior;
  }   

  incrementBehavior() {
    this._behavior ++;
  }
}

const halley = new Dog('Halley');
console.log(halley.name);
```

### Inheritance

```js
class Animal {
  constructor(name) {
    this._name = name;
    this._behavior = 0;
  }
    
  get name() {
    return this._name;
  }
  
  get behavior() {
    return this._behavior;
  }   
    
  incrementBehavior() {
    this._behavior++;
  }
}
class Cat extends Animal {
  constructor(name, usesLitter) {
    super(name); // call parent constructor (must be first line in constructor)
    this._usesLitter = usesLitter;
  }
  get usesLitter() {
    return this._usesLitter;
  }
}
```

### Static

```js
class Animal {
  constructor(name) {
    this._name = name;
    this._behavior = 0;
  }
    
  static generateName() {
    const names = ['Angel', 'Spike', 'Buffy', 'Willow', 'Tara'];
    const randomNumber = Math.floor(Math.random()*5);
    return names[randomNumber];
  }
} 
```

## Random

```js
Math.random() * 50; //Random number between 0 and 49

(Math.random() * (10 - 5) ) + 5; //Random number between 5 and 9

(Math.random() * (10 - 5 + 1) ) + 5; //Random number between 5 and 10

Math.floor(Math.random() * 50); //Rounds down to the nearest whole number
```

## Runtime Environment

Where the program will be executed

Determines globals and how it runs

Most common JS environments:
1. browser
2. Node

### Browser - Front End Applications

Javascript is executed in the browser's runtime environment as a front-end application

Window function built into the browser and any program executed by a browser has access to it
- `window.alert()`
- Data and functions relating to the open browser window

At first, the browser was the only place to execute JS

### Node - Back End Applications

Created for the purpose of executing JS without a browser

Allowed full-stack applications using only JS

Browser environment data values and functions cant be used (ex. `window.alert()`)

Instead, Node has its own runtime environment variables like `process`
- data of the JS file
- Gives back-end applications access to systems not available to a browser front-end application like server's file system, database, and network.
- Examples
  - Access the directory
    - `process.env.PWD`


## Modules

"separation of concerns"

> Reusable code in a file that can be exported then imported into another file

Modular Program
: components can be separated, used individually, and recombined

Example, separating the database logic, server logic, math functions, and date functions of an application into separate files

Pros:
- Debug more easily
- Recycle defined logic
- Privacy
- Clean global namespace

### Browser

[Modules in Browser](https://www.codecademy.com/article/implementing-modules-using-es-6-syntax)

`<script type="module" src="./my-script.js"></script>`

#### Export

```js
//Named Export Syntax
export { resourceToExportA, resourceToExportB };
//or
export const resourceToExportA = (parameter) => {

}
```

Example
```js
/* dom-functions.js */
const toggleHiddenElement = (domElement) => {
    if (domElement.style.display === 'none') {
      domElement.style.display = 'block';
    } else {
      domElement.style.display = 'none';
    }
}

const changeToFunkyColor = (domElement) => {
  const r = Math.random() * 255;
  const g = Math.random() * 255;
  const b = Math.random() * 255;
        
  domElement.style.background = `rgb(${r}, ${g}, ${b})`;
}

export { toggleHiddenElement, changeToFunkyColor };
```

#### Import

`import { resourceToExportA, resourceToExportB } from '/path/to/module.js';`

Example
```js
/* secret-messages.js */
import { toggleHiddenElement, changeToFunkyColor } from '../modules/dom-functions.js';

const buttonElement = document.getElementById('secret-button');
const pElement = document.getElementById('secret-p');

buttonElement.addEventListener('click', () => {
  toggleHiddenElement(pElement);
  changeToFunkyColor(buttonElement);
});
```
##### Renaming Imports

`import { exportedResource as newName } from '/path/to/module'`

#### Default Export and Import

Export a single value to represent the entire module `as default`
- `default` is a reserve identifier that can only be given to a single exported value
- `resources` is an object containing the module's resources
```js
const resources = { 
  valueA, 
  valueB 
}
export default resources
// or export { resources as default };
```

Import
```js
// This will work...
import resources from 'module.js'
// or import { default as resources } from 'module.js'

const { valueA, valueB } = resources;
```

### Node

[Modules in Node](https://www.codecademy.com/courses/learn-intermediate-javascript/articles/implementing-modules-in-node)

#### Export

`module.exports.functionName = function`

Example
```js
/* converters.js */
function celsiusToFahrenheit(celsius) {
  return celsius * (9/5) + 32;
}

module.exports.celsiusToFahrenheit = celsiusToFahrenheit;

module.exports.fahrenheitToCelsius = function(fahrenheit) {
  return (fahrenheit - 32) * (5/9);
};
```

#### Import

`const myImport = require(./myFile.js)`

Example:
```js
/* water-limits.js */
// Import all functions
const converters = require('./converters.js');

// Only Import one function (object destructuring)
const { celsiusToFahrenheit, fahrenheitToCelsius } = require('./converters.js');
// celsiusToFahrenheit(num)

const freezingPointC = 0;
const boilingPointC = 100;

const freezingPointF = converters.celsiusToFahrenheit(freezingPointC);
const boilingPointF = converters.celsiusToFahrenheit(boilingPointC);

console.log(`The freezing point of water in Fahrenheit is ${freezingPointF}`);
console.log(`The boiling point of water in Fahrenheit is ${boilingPointF}`);
```
