const paramA = process.argv[2]

if (paramA%2 == 0){
    process.env.STAGE_TWO = false
} else {
    process.env.STAGE_TWO = true
}

