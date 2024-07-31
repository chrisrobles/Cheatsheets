# CSS

## Syntax Example

```css
h1, p {
  font-size: 42px;
}
/*
selector {
  property: value;
}
*/
```
^ = CSS Rule

property + value = css declaration

## Selectors

- #*ID* { }= element with *ID* name
- .*CLASS* *ELEMENT*{ } = *ELEMENT*'s within *CLASS* name elements
- *ELEMENT*.*CLASS*{ } = *ELEMENT* that have a class name of *CLASS*
- *CLASS*,*ELEMENT*{ } = both *CLASS* and *ELEMENT*

## Color

[Named colors](http://www.colors.commutercreative.com/grid/

- color: green;
- color: rgb(54, 74, 101);
- color: hsl(350, 58.8%, 42.0%);
- color: #AA8EB5;
- color: #FFF;

### Opacity

rgba(54, 74, 101, .5)= .5 it’s opacity 

## Background

background-image: url(“*INSERT URL*”);

background-repeat: repeat(default/x and y) / repeat-x(repeat along the x) / repeat-y(repeat along the y) / no-repeat(will not repeat at all);

when a background image is not repeated you can do this: background-position: …;

left top

center top

right top

left center

center center

right center

left bottom

center bottom

right bottom

background: url(“#”) no-repeat right center;

background: cover/contain;

background-attachment: scroll/fixed; (for whether the background image scrolls with the page)

background-image: -webkit-linear-gradient(#FFD194, #BC1324);

## Style everything

```css
* {

}
```
= universal selector

## Properties priority

```css
p {
  color: red;
}
p { /* Takes priority */
  color: blue;
}
```

## Fonts and Text

- font-family: Georgia, Garamond, serif/sans-serif;
- font-size: 100%; = 16px
- font-weight: 100; OR font-weight: bold;
- font-style: italic;
- Text-align: center/justify (justify will have a complete square block of text like in magazines);
- text-decoration: overline/line-through/underline/none;
- text-indent: 10px; (sets the amount of indent of the first line)
- text-shadow: 5px 2px red; (*the position of the horizontal shadow* *the position of the vertical shadow* *the color of the shadow*)
- font-variant: normal/small-caps; (HELLO EARTH)
- text-transform: uppercase;
- Line-height: 1.7em; (space between lines)
- Letter-spacing: 0.02em (space between characters)
- word-spacing: 0.05em; (space between words)
- direction: ltr/rtl;

### Import fonts

```html
<head>
  <link href="https://fonts.googleapis.com/css?family=Raleway" type="text/css" rel="stylesheet">
</head>
```
or
```css
h1 {
  font-family: Raleway, Georgia, serif;
}
```

## Inherit vs Initial

- initial Sets this property to its default value. Read about initial 
- inherit Inherits this property from its parent element. Read about inherit

## Border

`border: *width* *style* *color*;`

### Width

`border-width:`
- `thin/medium/thick;`
- `5px 10px 5px 10px; /* *top* *right* *bottom* *left* */`
- `5px 10px; /* *top & bottom* *left & right* */`
- `border-left-width: 4px;`

### Styles

`border-style:`

- solid =  border is a solid line.
- dashed =  border is a series of lines or dashes.
- dotted =  border is a series of square dots.
- double =  border is two solid black lines.
- groove =  border is a groove (or carving).
- inset =  border appears to cut into the screen.
- outset =  border appears to pop out of the screen.
- ridge =  border appears as a picture frame.
- hidden or none - no border.

### Color

- `border-color: red;`

### Radius

border-radius: 5px; (box with rounded corners)

border-radius: *box height*/100%; (perfect circle)

## Margin & Padding Properties

The space between the contents of a box and the borders of a box is known as padding.

padding: 10px; (puts 10 pixels between the space between the content of the paragraph (the text) and the box borders, on all four sides)

margin/padding: 5px 10px 5px 10px;

margin/padding: 5px 10px; (same as above)

margin-top/padding-top: 10px;

The margin refers to the space directly outside of the box.

margin: 20px;

When the margin property is set to auto (margin: auto;), the element being styled will center in the page. In order to center an element, a width must be set for that element. Otherwise, the width of the div will be automatically set to the full width of its containing element, like the <body>, for example.

### Resetting margin & padding

```css
* {
margin: 0;
padding: 0;
}/*resets the margin and padding from whatever the user-agent would set it to*/
```

## Inline vs. Block-level Elements

ALL HTML ELEMENTS ARE EITHER INLINE OR BLOCK-LEVEL

Inline elements- elements that display inline with text, without disrupting the flow of the text (like links).

Block-level elements- elements that use an entire line of space in a web page and disrupt the natural flow of text. Mos of the common HTML elements are block-level elements(headings,paragraphs,divs)

display: inline(changes block-level to inline) / block(changes inline to block-level) / inline-block(changes block-level to inline, but retain the features of a block-level) / none(removes it from the page completely instead of making it invisible);

## Hide

- Hide it but still take up space on the page
  - `visibility: hidden/visible;`
- Hide it and dont take up space on the page
  - `display: none;`

## Box-sizing

`box-sizing:`

- content-box Default. The width and height properties (and min/max properties) includes only the content. Border, padding, or margin are not included 
- border-box The width and height properties (and min/max properties) includes content, padding and border, but not the margin 

## Offsetting (top,left…)

Offset properties move an element’s position:

top - moves the element down. (top: 10px; adds 10px to the top of the element)

bottom - moves the element up. (bottom: 10px; move the element up 10px)

left - moves the element right from the left.

right - moves the element left. (right: 10px; moves the element 10px from the left)


## Position

`position: …;`

<https://www.w3schools.com/cssref/playit.asp?filename=playcss_position>

static- the default value(to the left)

relative- the elements move from its static position. (moves from where it would be if it were static)

absolute- the offset properties move the element from the top left corner of the container

fixed- the element will remain fixed to its position no matter where the user scrolls on the page.


## Visual Priority (z-index)

z-index controls how far back or how far forward an element should appear on the web page. z-index: *insert number*; /*the higher the number the more precedence it will take.

z-index does not work on static elements, so set it to relative.


## Float

float: left/right;

left- moves the element as far left as possible

right- moves the element as far left as possible

FLOATED ELEMENTS MUST HAVE A SPECIFIED WIDTH


## Clear

The `clear:` property specifies how elements should behave when they bump into each other on the page. It can take on one of the following values:

left — the left side of the element will not touch any other element within the same containing element, so it will move to the left if it bumps into another element on the left after the other element floats.

right — the right side of the element will not touch any other element within the same containing element.

both — neither side of the element will touch any other element within the same containing element.

none — the element can touch either side.

## Overflow

The overflow property controls what happens to content when it spills, or overflows, outside of its box. It can be set to one of the following values:

hidden - when set to this value, any content that overflows be hidden from view.

scroll - when set to this value, a scrollbar will be added to the element's box so that the rest of the content can be viewed by scrolling.

## Formatting Tables
```css
table {

border: 1px solid black;

font-family: Arial, sans-serif;

text-align: center;

height:

left:

margin:

overflow-y:

position:

width:

}

th, td {

background:

color:

font-family:

font-size:

font-weight:

letter-spacing:

text-transform:

}

thead th{

background:

color:

font-family:

}

tr {
 background:

border-bottom:

}
```

## Outline-style Property

The formatting of the outline will not affect the element’s dimensions. The outline is found outside the border.

outline-style:...;

dotted - Defines a dotted outline

dashed - Defines a dashed outline

solid - Defines a solid outline

double - Defines a double outline

groove - Defines a 3D grooved outline. The effect depends on the outline-color value

ridge - Defines a 3D ridged outline. The effect depends on the outline-color value

inset - Defines a 3D inset outline. The effect depends on the outline-color value

outset - Defines a 3D outset outline. The effect depends on the outline-color value

none - Defines no outline

hidden - Defines a hidden outline

outline-color: red;

outline-width: 5px;

outline: 5px ridge red;

## Styling Links

a:hover

a - class selector

:hover - describes the state the link is in

a:link{color: red;} - a normal, unvisited link

a:visited{color: green;} - a link the user has visited

a:hover - a link when the user mouses over it

a:active - a link the moment it is clicked