const maxnum = 1000
const minnum = 101
const lowestn = 1000

export function encrypt(key, n, message){
    let text = []
    for (let i = 0; i < message.length; i++){
        let val = message.charCodeAt(i)
        let j = Math.pow(i,key)%n
        text[i] = j
    }
    return text
}
export function decrypt(key, n, message){
    let text = []
    for (i = 0; i < message.length; i++){
        let val = Math.pow(i,key)%n
        let j = String.fromCharCode(val)
        text[i] = j;
    }
    return text.join("")
}

export function generateKeys(){
    let k = 2
    let n = 1
    let p1 = 0
    let p2 = 0
    let nn = 0
    let de = []
    while(is_Prime(k)){
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
    let n = v
    let factors = []
    let i  = 0
    while(n%2 === 0){
        factors[i] = 2
        n = n/2
        i++
    }
    for(let j = 3; parseInt(Math.sqrt(n), 10) +1; j+=2){
        while(n%j === 0){
            factors[i] = j
            n = n/j
            i++
        }
    }
    if(n > 2){
        factors[i] = n
    }
    let d = 1
    for(let k = 0; k < factors.length; k++){
        d*=x
    }
    let e = factors[factors.length - 1]
    d /= e
    console.log('test')
    return [parseInt(d), parseInt(e)]
}
function gcd(a,b){
    return gcd(a,b)
}
function getLargePrime(n){
    let isPrime = false
    let possibleNum = 0;
    while(!isPrime){
        possibleNum = Math.floor(Math.random() * maxnum) + minnum 
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
    for(let i = 3; i < parseInt(Math.pow(number, 0.5) +2); i++){
        if(number %i === 0){
            return false
        }
    }
    return true
}