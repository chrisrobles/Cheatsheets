# Javascript

`<script src="js/main.js"></script>`

## Console Log

```js
//interpolation
console.log("... " + variable + " ending element");
console.log(`${value} is the value`);
console.log("...", value, "ending element");
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

`confirm("Ready?");//creates a pop up box with an ok and cancel button`

### Prompt

`prompt("What is your name?");//creates a pop up with an input field`

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

"chris’s \nhouse" //new line operator

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

Simple Function
```js
function myFunc(myParam) {
  // ...
}
```

Anonymous Function
```js
(myParam) => {
  // ...
}

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

## Error

### Error Handling

```js
try {

} catch(error) {

}
```

### Custom Error

Create a custom error object that can be thrown

```js
console.log(Error('Custom error message'));
// or 
let myError = new Error('Custom error message');
```

### Throw Error

Stops a program from running

```js
throw Error('Something wrong happened');
```

