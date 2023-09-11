# Import .p12 file into Mac OS

## Notice
- Only work on Mac OS
- Sync

## Usage

```sh
$ npm install p12 --save
```

```sh
var p12 = require('p12');
p12('PATH-TO-YOUR-.p12-FILE')
    .then(function (value) {
        console.log(value);
    })
    .catch(function (error) {
        console.log(error);
    });
```