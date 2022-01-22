function solution(arr){
    let answer;
    console.log(arr.length);
    let sum =0;
    for(let k = 0; k<arr.length; k++) {
        sum += arr[k];
    }
    console.log(sum);
    for (let i = 0; i < arr.length; i++){
        if(arr.length == 7) {
            break;
        }
        for (let j = 0; j < arr.length; j++) {
            if( sum - (arr[i] + arr[j]) == 100) {
                arr.pop(arr[i]);
                arr.pop(arr[j]);
                break;
            } 
        }

    }

    answer = arr;
    return answer;
}


let add=[20, 7, 23, 19, 10, 15, 25, 8, 13];
console.log(solution(add));
