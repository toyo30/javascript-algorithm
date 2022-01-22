











let arr = [13, 5, 11, 7, 23, 15];

//원하는 위치를 뺌. 
let item = arr.splice(2, 1);

console.log(item);
arr.splice(3, 0, item[0]);


console.log(arr);


