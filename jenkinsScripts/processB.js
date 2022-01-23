const paramA = process.argv[2]

const { exec } = require('child_process');

const paramA = process.argv[2]

if (paramA%2 == 0){
    exec('export STAGE_TWO=false')
} else {
    exec('export STAGE_TWO=true')
}

