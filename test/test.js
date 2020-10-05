function printAnswer(answer) {
    if (answer=== true) {
        console.log('The number is even')
    } else {
        console.log('The number is odd')
    }
}

var number = 3
var ans = isEven(number)
printAnswer(ans)

function isEven (num) {
    var answer;
    if (num%2 === 0) {
        answer = true
    } else {
        answer = false
    }
    return answer
}




