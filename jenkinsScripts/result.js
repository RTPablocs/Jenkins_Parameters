const paramA = process.env.STAGE_ONE
const paramB = process.env.STAGE_TWO

if (paramA == false || paramB == false) {
    console.log("Alguna de las dos stages ha fallado")
} else if (paramA == false && paramB == false) {
    console.log( "Esto pinta muy mal")
} else {
    console.log( "El proyecto va viento en popa!!!" )
}
