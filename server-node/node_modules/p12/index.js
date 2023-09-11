'use strict';
module.exports = p12;
function p12(input,pwd){
    return new Promise(function (resolve, reject) {
        const path = input;
        //security import app证书.p12 -k ~/Library/Keychains/login.keychain -P 1 -T /usr/bin/codesign
        const reg = new RegExp("(\/Users\/.*?\/).*");
        const root = __dirname.match(reg)[1];

        const spawn = require('child_process').spawn;
        const p12Import = spawn('security', ['import', path, '-k', `${root}Library/Keychains/login.keychain`, '-P', pwd, '-T', '/usr/bin/codesign']);

        p12Import.stdout.on('data', (data) => {
            console.log(`stdout: ${data}`);
        });

        p12Import.stderr.on('data', (data) => {
            reject(`stderr: ${data}`);
        });

        p12Import.on('close', (code) => {
            resolve(`child process exited with code ${code}`);
        });
    });
};


