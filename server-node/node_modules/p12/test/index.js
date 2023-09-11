var p12 = require('./../index.js');
p12('app证书.p12','1')
    .then(function (value) {
        console.log(value);
    })
    .catch(function (error) {
        console.log(error);
    });