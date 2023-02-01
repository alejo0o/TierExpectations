var Person = {
  printName: function () {
    console.log(`My name is ${this.name} and I am ${this.age} years old.`);
  },
};

var SoftwareDeveloper = Object.create(Person);
SoftwareDeveloper.presentation = function () {
  console.log(
    `Hello World! I'm ${this.name} and I'm a ${this.area} developer.`
  );
};
SoftwareDeveloper.printName = function () {
  console.log("Polymorphism simulation")
};

var alejoDeveloper = Object.create(SoftwareDeveloper);
alejoDeveloper.name = "Alejandro";
alejoDeveloper.area = "Full stack";

console.log(alejoDeveloper.presentation());
//Hello World! I'm Alejandro and I'm a Full stack developer.
// We can simulate subclasses using prototypal delegation, Person is the main class and SoftwareDeveloper the subclass
console.log(alejoDeveloper.printName())
// Polymorphism simulation
console.log(Object.getOwnPropertyNames(alejoDeveloper))
// ['name', 'area']
console.log(alejoDeveloper.hasOwnProperty('age'))
// false because this is a property from Person
console.log(alejoDeveloper.hasOwnProperty('area'))
// true because this is a property from SoftwareDeveloper
console.log(Object.getPrototypeOf(alejoDeveloper).hasOwnProperty("presentation"));
// true because this comes from SoftwareDeveloper (parent)
