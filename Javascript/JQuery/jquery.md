# JQuery

A JS library

```html
<script src='https://code.jquery.com/jquery-3.1.0.min.js'></script>
```

## On Page Load

```js
function main() {
}
$(document).ready(main);
```

## Get element

```js
//JS way
document.getElementsByClassName(‘example-html-class-name’);
//JQuery way
$(‘.example-class-name’); OR $(‘#header’);
```

## Store JQuery Selectors

IT IS COMMON PRACTICE TO NAME VARIABLES THAT HOLD JQUERY SELECTORS WITH A DOLLAR SIGN $

`var $skillset = $(‘.skillset’);`


## JQuery Functions for DOMs

used to manipulate DOM(Document Object Model)

### Hide

`$(‘.skills).hide(); //hide elements, used to make elements fade in`

### Fade

`$(‘.skills).fadeIn(2000); //used on hidden elements to fade in (in milliseconds)`

1000 milliseconds in a second

### Show

`$(‘example-class’).show(); //shows a hidden element`

### Toggle

`$(‘.projects’).toggle(); //toggles whether an element is hidden or shown`

### Toggle Class

`$(‘.projects-button’).toggleClass(‘active’); //will apply the active class to the .projects-button element or remove it if it is already applied to it`

### Slide Toggle

`$(this).next().slideToggle(); // It adds a smooth slide down animation

### Text

`$(this).text(‘Projects Viewed’); //will change the text of our DOM element.`

## Listeners (on)

```js
$(‘projects’).on(‘click/dblclick/mouseenter/mouseleave/keypress/keydown/keyup/submit/focus/blur/scroll/resize/load’,function() {});

//OR

$(‘.projects’).click(function() {

});

//OR

$(‘html’).on(‘click’, ".projects", function() {

});
// use this one when creating html elements after page load
// works because the listener is attached to the html dom and so all .projects inside that have a .click event will execute the function() handler
```

## $(this)

`$(this).toggleClass(‘active’);`

`$(this)` only selects the clicked element so that if there are multiple .projects-button than only the class that is clicked on will be selected
