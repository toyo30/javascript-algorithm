// function solution(a, b, c, d, e, f, g){
//     let answer = []
//     let sum = 0;
//     let min = 0;
//     let arr_box = [a, b, c, d, e, f, g];
//     let arr = [];

//     for (let i = 0; i < arr_box.length; i++) {
//         if (arr_box[i] % 2 == 1) {
//             arr.push(arr_box[i]);

//         }
//     }
    

//     for (let i = 0; i < arr.length; i++) {
//         sum += arr[i];
//     }
//     min = Math.min.apply(null, arr);
//     answer.push(sum);
//     answer.push(min);


//     return answer;
// }

// console.log(solution(12, 77, 38, 41, 53, 92, 85));

function solution(arr) {
    let answer = [];
    let sum = 0;
    let min = 100;

    for(let x of arr) {
       
        if(x % 2=== 1) {
            console.log(x);
            sum += x;
            if(x < min) min = x;
        }
    }

    answer.push(sum);
    answer.push(min);

    return answer;
}


console.log(solution([12, 77, 38, 41, 53, 92, 85]))


//Math.min만 써도 됨. 

//배열을 쓸때는 Math.min(...arr);   arr[0], arr[1], arr[2], arr[3] ... 이렇게 전게됨. 

//Math.min.apply(null, arr); 첫번재 인자는 this에다가 컨트롤할 수 있는 객체를 사용할 수 있음. 