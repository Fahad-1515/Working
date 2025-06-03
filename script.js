const person = {
  firstName: "WCypher",
  age: "23",
  isEmployed: false,
  sayHello: function () {
    console.log("hi");
  },
  eat: () => console.log("he is eating"),
};

for (var prop of Object.keys(person)) {
  console.log(`${prop}: ${person[prop]}`);
}
