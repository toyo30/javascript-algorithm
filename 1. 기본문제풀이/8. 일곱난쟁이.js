function solution(arr){
    let answer=arr;
    let sum = 0;
    for(let x = 0; x < arr.length; x++){
        sum += arr[x]
    };

    for(let i=0; i< (arr.length - 1); i++){
        for(let j=i+1; j< arr.length; j++){
            if((sum-(arr[i]+arr[j]))==100){
                arr.splice(j, 1);
                arr.splice(i, 1);
            }
        }
    }
    answer = arr;
    return answer;
}


let add=[20, 7, 23, 19, 10, 15, 25, 8, 13];
console.log(solution(add));
