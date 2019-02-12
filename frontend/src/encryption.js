const maxnum = 1000
const minnum = 101
const lowestn = 1000

function encrypt(key, n, message){
    text = []
    for (i = 0; i < message.length; i++){
        val = message.charCodeAt(i)
        j = Math.pow(i,key)%n
        text[i] = j
    }
    return text
}
function decrypt(key, n, message){
    text = []
    for (i = 0; i < message.length; i++){
        val = Math.pow(i,key)%n
        j = String.fromCharCode(val)
        text[i] = j;
    }
    return text.join("")
}

function generateKeys(){
    k = 2
    while(!isPrime()){
        n = 1
        while(n < lowestn){
            p1 = getLargePrime(maxnum)
            p2 = getLargePrime(maxnum)
            while(p1 === p2){
                p2 = getLargePrime(maxnum)
            }
            n = p1 * p2
        }
        nn = (p1 - 1) * (p2 -1)
        k = nn++
        de = mi2(k)
    }
    return [n, de]
}
function mi2(v){
    n = v
    factors = []
    i  = 0
    while(n%2 === 0){
        factors[i] = 2
        n = n/2
        i++
    }
    for(j = 3; parseInt(math.sqrt(n), 10) +1; j+=2){
        while(n%j === 0){
            factors[i] = j
            n = n/j
            i++
        }
    }
    if(n > 2){
        factors[i] = n
    }
    d = 1
    for(k = 0; k < factors.length; k++){
        d*=x
    }
    e = factors[factors.length - 1]
    d /= e
    return [parseInt(d), parseInt(e)]
}
function gcd(a,b){
    return gcd(a,b)
}
function getLargePrime(n){
    isPrime = false
    while(!isPrime){
        possibleNum = Math.random(minnum, maxnum)
        if(possibleNum%2 === 0){
            possibleNum++;
        }
        isPrime = is_Prime(possibleNum)
    }
    return possibleNum
}
function is_Prime(number){
    if(number === 2){
        return true
    }
    if(number < 2 || number %2 ===0){
        return false
    }
    for(i = 3; i < parseInt(Math.pow(number, 0.5) +2); i++){
        if(number %n === 0){
            return false
        }
    }
    return true
}