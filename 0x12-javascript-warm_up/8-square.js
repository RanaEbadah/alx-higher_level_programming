#!/usr/bin/node
if (isNaN(process.argv[2]))
    console.log('Missing size');
else {
    let str = '';
    for (let y = Number(process.argv[2]); y > 0; y--) {
        for (let x = Number(process.argv[2]); x > 0; x--) {
            str = str + 'X';
        }
        console.log(str);
        str = '';
    }
}
