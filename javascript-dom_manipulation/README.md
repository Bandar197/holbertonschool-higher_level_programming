# JavaScript DOM Manipulation

Holberton School project covering browser-side JavaScript, DOM selection and
updates, user events, and asynchronous HTTP requests using the Fetch API.

## Requirements

- Run scripts in Chrome 57 or later.
- Follow JavaScript semistandard style (semicolons required, no `var`).
- Load each script using the corresponding HTML example in the project.
- All DOM updates occur without reloading the page.

## Tasks

| File | Task | Description |
| --- | --- | --- |
| `0-script.js` | Color Me | Color the header red on script execution. |
| `1-script.js` | Click and turn red | Color the header red after a click. |
| `2-script.js` | Add `.red` class | Add a CSS class to the header after a click. |
| `3-script.js` | Toggle classes | Switch between `red` and `green` header classes. |
| `4-script.js` | List of elements | Append a new `li` element on each click. |
| `5-script.js` | Change the text | Update the header text on click. |
| `6-script.js` | Star wars character | Fetch and display a Star Wars character name. |
| `7-script.js` | Star Wars movies | Fetch and display movie titles in a list. |
| `8-script.js` | Say Hello! | Fetch a French translation after the DOM loads. |

## Testing

Open the corresponding `N-main.html` example supplied in the Holberton project
using a web browser. Check the page before and after the specified interaction.
The last three tasks require access to their respective public HTTP endpoints.

**Note:** `8-script.js` waits for `DOMContentLoaded`, so it also works when
included in the document's `<head>` element.
