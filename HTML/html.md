# HTML

Hyper-Text Markup Language

## Boilerplate

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Animals Around the World</title>
    </head>
    <body>
        <p>Hello, World!</p>
    </body>
</html>
```

## Syntax

`<p></p>`
- Opening and closing tags for the p element

`<p class="bears">`
- class is an *attribute*

## CSS

### Style Tag

`<style>background-color: red;</style>`

### Link Tag

`<link href=”style.css” rel=”stylesheet” type=”text/css”>`

### Inline

`<h1 style=”color: blue; margin-left: 30px;”>This is the heading text</h1>`


## Fonts

fonts.google.com

`<link href=”https://fonts.googleapis.com/css?family=Roboto:400,300,500,100” rel=”stylesheet” type=”text/css”>`

## Common Elements Example

Example of headings, paragraphs, Links, Lists, Comments, Images

```html
<html>
  <body>
    <h1>The Brown Bear</h1>/*biggest header*/
    <h6>A Deadly Animal</h6>/*smallest header*/
    <a href="https://en.wikipedia.org/wiki/Brown_bear" target="_blank">Learn More</a><!-- Open a link in a new tab-->
    <p>The following are subspecies of bears:</p>
    <ul>
      <li>Arctos</li>
      <li>Collarus</li>
      <li>Horriblis</li>
      <li>Nelsoni(extinct)</li>
    </ul>

    <p>The following countries have the largest populations<br />of brown bears:</p>
    <ol start=”10” type=”1” reversed=”reversed”>
      <li>Russia</li>
      <li>United States</li>
      <li>Canada</li>
    </ol><!-- This will print a list starting at 10 and descending by one --> 
  
    <!-- How to wrap a link around an image element -->
    <a href="https://en.wikipedia.org/wiki/Brown_bear">
      <img src="https://s3.amazonaws.com/codecademy-content/courses/web-101/web101-image_brownbear.jpg" alt="A brown bear in a forest" width=”104” height=”142” />
    </a>
  </body>
</html>
```

## ID

Unique to one element

`<p id="biggestBear">Idk what the biggest bear</p>`

## Classes

For multiple elements that should share the same styling, classes can be used to label them.

```html
<h1 class="science">Scientist Discovers Important Cure</h1>
<h1 class="science">New Study Reveals The Importance of Sleep</h1>
```


## Line Breaks

`<br>`

Does not need a closing tag

## Horizontal Rules

<hr>

Requires no closing tag

Puts a horizontal line across the page

## Abbreviation

<abbr title=”Laugh out loud”>LOL</abbr>

## Buttons

<button>Click Me</button>

### Attributes

- type=”button”/”reset”/”submit”
- name="myName"
- value=”text”

### Link button (w/ bootstrap)

`<a class="btn btn-primary" href="google.com">Go to Google</a>`

## Forms

```html
<form action="/action_page.php">
  First name: <input type="text" name="FirstName" value="Mickey"><br>

  Last name: <input type="text" name="LastName" value="Mouse"><br>

  <input type="submit" value="Submit">
  <!-- or -->
  <button type="submit">Submit</button>
</form>
```

### Label

```html
<label for="first_name">First Name</label><br>
<input type="text" id="first_name" name="personName" />
```

### Select Input

```html
<select>
 <option value=”red” selected=”selected”>Red</option>
 <option value=”yellow”>Yellow</option>
</select>
```

## Images

`<img src=”dog.jpeg” alt=”A picture of a dog” height=”100” width=”52” align=”top” border=”3”>`

## Format Tags

```html
<em>Emphasized text</em><br>

<strong>Strong text</strong><br>

<code>A piece of computer code</code><br>

<samp>Sample output from a computer program</samp><br>

<kbd>Keyboard input</kbd><br>

<var>Variable</var>

<b> - Bold text

<strong> - Important text

<i> - Italic text

<em> - Emphasized text

<mark> - Marked text

<small> - Small text

<del> - Deleted text

<ins> - Inserted text

<sub> - Subscript text

<sup> - Superscript text

<p><b>I will be displayed bold</b></p>
```

## Displaying webpages within a webpage

<iframe src=”URL” style=”border:3px solid blue;” height=”200” width”400”></iframe>


## Tables

```html
<table>
<!-- td stands for table data and having two data points in one row results in a table with two columns and one row -->
<!-- tr stands for table row(has an affect on display and code -->
<!-- th stands for table header(has no visual effect) -->
  <thead>
    <tr>
      <th></th>
      <th>Number</th>
      <th>Type</th>
    </tr> <!-- This is a row --> 
  </thead>
  <tbody>
    <tr>
      <td>info</td>
      <td>14</td>
      <td>Package</td>
    </tr>
    <tr>
      <td colspan=”2”>This will span two columns</td>
      <td rowspan=”2”>This will span two rows</td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <td>Total</td>
      <td>14</td>
    </tr>
  </tfoot>
</table>
```