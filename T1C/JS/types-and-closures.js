function initApp() {
  const name = "Alejandro"; // string
  const age = 24; //int
  const maritalStatus = null; // null
  const gender = undefined; // undefined
  const country = false; // boolean

  function displayInfo() {
    const person = {
      name,
      age,
      maritalStatus,
      gender,
      country,
    }; // object
    console.log(`Hi my name is ${person.name} I am ${age} years old.`);
    // closure gives us access to outter variables like age name ...
    // displayInfo is the inner function, a closure
  }
  displayInfo();
}

initApp();
