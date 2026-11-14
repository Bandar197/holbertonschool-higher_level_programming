# JavaScript - Warm up

Holberton School JavaScript warm-up exercises, intended for Node.js 14.

## Requirements

- JavaScript files begin with `#!/usr/bin/node` and are executable.
- Follow semistandard (v16) formatting and use semicolons.
- Do not use `var`.

## Tasks

| File | Purpose |
| --- | --- |
| `0-javascript_is_amazing.js` | Print a constant |
| `1-multi_languages.js` | Print three lines |
| `2-arguments.js` | Report the number of arguments |
| `3-value_argument.js` | Print the first argument |
| `4-concat.js` | Combine two arguments into a sentence |
| `5-to_integer.js` | Convert an argument to an integer |
| `6-multi_languages_loop.js` | Print language lines with a loop |
| `7-multi_c.js` | Repeat a line a specified number of times |
| `8-square.js` | Print an X-filled square |
| `9-add.js` | Add two command-line integers |
| `10-factorial.js` | Compute a factorial recursively |
| `11-second_biggest.js` | Find the second largest input integer |
| `12-object.js` | Update an object property |
| `13-add.js` | Export an addition function |

## Run

```sh
./0-javascript_is_amazing.js
./9-add.js 13 89
node 13-add.js
```

To use the exported function:

```js
const add = require('./13-add').add;
console.log(add(3, 5));
```
