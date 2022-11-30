const letrasHexa = (x) =>{
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

const toDecimal = (num,base) => {
    let decimal = 0;
    let potencia = 0;
    for(let i = num.length - 1; i >= 0; i--){
        decimal += num[i] * Math.pow(base, potencia);
        potencia++;
    }
    return decimal;
}

const decToAllBases = (decimal, base) =>{
    var conversao = "";
    if(decimal == 0){
        return 0;
    }
    while(decimal > 0){ 
        if(decimal % base == 0){
            conversao = "0" + conversao;
        }
        else {
            result = decimal % base
            conversao = letrasHexa(result) + conversao;
        }

        decimal = Math.floor(decimal / base);
    }

    return conversao;
}

const binToAllBases = (bin, base) => {
    return decToAllBases(toDecimal(bin, 2), base);
}

const hexToAllBases = (hex, base) => {
    return decToAllBases(toDecimal(hex, 16), base);
}

const octToAllBases = (oct, base) => {
    return decToAllBases(toDecimal(oct, 8), base);
}