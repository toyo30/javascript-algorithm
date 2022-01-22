function solution(items) {
    let answer = [];

    // for(let i of items) {
    //     console.log(i);
    // }


    // for (let i = 1; i < items.length; i++) {
    //     if(answer[answer.length - 1] < items[i]) answer.push(items[i]);
    //     else if(answer[0] >= items[i]) answer.unshift(items[i]);
    // }


    for(let i = 0; i < items.length; i++) {
        for(let j = i + 1; j < items.length; i++) {
            if(items[i] > items[j]) {
                let value = items.splice(i, 1);
                items.splice(j, 0, value);                
            }

        }

    }


    // items.forEach(function(item, index) {
    //     console.log(i);
        
    // });


    console.log(items);
    return items;

}






console.log('1234');






let arr = [13, 5, 11, 7, 23, 15];
console.log(solution(arr));



