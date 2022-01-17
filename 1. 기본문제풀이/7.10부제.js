function solution(a, b) {
    let answer = 0;


    for (let x of b) {
        let strNum = String(x);
        if( String(a) == strNum[strNum.length-1]) {
            answer += 1
        }
    }

    return answer;
}


let num = 3;
let arr = [25, 23, 11, 47, 53, 17, 33];
console.log(solution(num, arr));

console.log(solution(0, [12, 20, 54, 30, 87, 91, 30]));


