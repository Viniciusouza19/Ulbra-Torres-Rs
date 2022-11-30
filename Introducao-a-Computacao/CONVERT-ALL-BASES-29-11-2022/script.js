const numberToHexLetter = (x) =>{
    switch(x){
        case 10:
            return "A";
        case 11:
            return "B";
        case 12:
            return "C";
        case 13:
            return "D";
        case 14:
            return "E";
        case 15:
            return "F";
        default:
            return x;
    }
}
const hexLetterForNumber = (x) => {
    switch(x.toUpperCase()){
        case "A":
            return 10;
        case "B":
            return 11;
        case "C":
            return 12;
        case "D":
            return 13;
        case "E":
            return 14;
        case "F":
            return 15;
        default:
            return x;
    }
}

const toDecimal = (number,base) => {
    let decimal = 0;
    let power = 0;
    for(let i = number.length - 1; i >= 0; i--){
        if(base == 16){
            decimal += hexLetterForNumber(number[i]) * Math.pow(base, power);
        }else{
            decimal += number[i] * Math.pow(base, power);
        }
        power++;
    }
    return decimal;
}

const decToAllBases = (decimal, base) =>{
    var conversion = "";
    if(decimal == 0){
        return 0;
    }
    while(decimal > 0){ 
        if(decimal % base == 0){
            conversion = "0" + conversion;
        }
        else {
            result = decimal % base
            conversion = numberToHexLetter(result) + conversion;
        }

        decimal = Math.floor(decimal / base);
    }

    return conversion;
}

const binToAllBases = (bin, base) => {
    return decToAllBases(toDecimal(bin, 2), base);
}

const hexToAllBases = (hex, base) => {
    if (base == 16){
        return numberToHexLetter(hex.toUpperCase());
    }
    return decToAllBases(toDecimal(hex, 16), base);
}

const octToAllBases = (oct, base) => {
    return decToAllBases(toDecimal(oct, 8), base);
}


