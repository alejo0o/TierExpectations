const number = 4;

function foo() {
  if (number % 2 === 0){
    var word = "Hola"
    let word2 = "Mundo"
    const word3 = "!" 
  }
  console.log(word)
  //console.log(word2) is not accesible 
  //console.log(word3) is not accesible
  /* 
    let and const are block scope so they will be accesible
    inside the if, however var is function scope that's why
    we can access it from outside the if block
  */
  
}
