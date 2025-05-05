function func1(){
    let x = 100;
    function func2(){
       console.log(x)
    }
    return func2    //func1 only return func2
}
let result = func1() //first this function is called   
result()   //here func2 is called which is stored in result and this help to print x=100