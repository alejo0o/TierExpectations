var Person = {
  printName: function (){
    console.log(`My name is ${this.name} and I am ${this.age} years old.`)
  }
}

var alejo = Object.create(Person)

alejo.name = "Alejandro"
alejo.age = "24"

alejo.printName()
//My name is Alejandro and I am 24 years old.
