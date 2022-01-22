//Math.random()

// 범위를 지정한 난수 생성하기 




//0~1(1은 미포함)  부동소수점의 난수를 생성
let randomNum = Math.random();
//console.log(randomNum);



// 정수인 난수 생성

//Math.random(); Math.floor(); 함수를 함께 사용 
//Math.floor() 함수는 소수점 1번째 자리를 버림하여 정수를 리턴하는 함수입니다.

// Math.round(); 반올림, Math.ceil(); 올림, Math.floor(); 내림 


let ranTenNum = Math.floor(randomNum * 10 + 1);
//console.log(ranTenNum);


// Math.floor(randomNum * 10);  => 0 ~ 9 
// Math.floor(randomNum * 11);  => 0 ~ 10

// Math.floor(randomNum * 10 + 1);  => 1 ~ 10


/*
function rand(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
  }
  
  document.writeln(rand(1, 3));
  document.writeln(rand(77, 88));

*/

/*
function rand(min, max) {
    return Math.floor(Math.random() * (max - min)) + min;
  }
  
  document.writeln(rand(1, 3));
  document.writeln(rand(77, 88));
*/



let num = Math.floor(Math.random() * 1000000000 + 10000);

console.log(num);


num = String(num);
console.log(num);

// let count = 0;
// for(let i = 0; num.length; i++) {
//     count++;
//     let length = num.length - i;
    
//     if(count % 3 == 0) {


//     }
// }



function addDot(num) {
    num = String(num);
    let middle = num.length - 3;

    while(middle > 0) {
        num = num.slice(0, middle) + ',' + num.slice(middle, num.length);
        middle -= 3;
    }

    console.log(num);
}



addDot(293);


