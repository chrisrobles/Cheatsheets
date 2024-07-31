# Javascript

`<script src="js/main.js"></script>`

## Variables

let myVar = ...
- Scoped to the block they are in (if statement, function, for loop, ...)
- Cant be redeclared in the same scope

var myVar = ...
- Scoped to the function its declared in or globally scoped if not inside a function
- Can be redeclared in the same scope

## Console Log
```js
console.log(“...” + variable + “ending element”);//interpolation

console.log(“...”, “ending element”);
```
## Confirm

`confirm(“Ready?”);//creates a pop up box with an ok and cancel button`

## Prompt

`prompt(“What is your name?”);//creates a pop up with an input field`

## Random

```js
Math.random() * 50; //Random number between 0 and 49

(Math.random() * (10 - 5) ) + 5; //Random number between 5 and 9

(Math.random() * (10 - 5 + 1) + 5; //Random number between 5 and 10

Math.floor(Math.random() * 50); //Rounds down to the nearest whole number
```

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

‘chris\’s house’ //escaping

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

## Arrays & Array Functions & String functions

```js
var bucketList = ['jump', 'run', 'sleep'];
var listItem = bucketList[2];
```
- adding to an array will return the length

### Remove Multiple Elements

`var removedItem = bucketList.splice(startingIndex, numberOfItemsToRemove);`

### Copy

`var bucketListCopy = bucketList.slice();`

### For Statement
```js
var vacationSpots= ['LA', 'Hawaii', 'France'];

for (var i = 0; i < vacationSpots.length; i++) {
  console.log('I would love to visit ' + vacationSpots[i]);
}
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

## Substring

`“word”.substring(x, y);//x = where you start chopping y=where you stop(doesn’t include)`
