var a = 10;
var b = 20;
// console.log(a+b);   //30
// console.log(a-b);   //-10
// console.log(a*b);   //200
// console.log(a/b);   // .5
// console.log("Pankaj Kapoor");
// console.log("I am Corporate Trainer");

var fname = "Pankaj";
var lname = "Kapoor";

// console.log(fname +" "+ lname);  // concatenation

// conditional statement
// a = 30;
// b = 20;
// if(a<b) //false
// {
//     console.log("a is smaller");
// }
// else
// {
//     console.log("b is smaller");
// }

// Javascript is loosely
// a= 10;
// a = "pankaj"
// a = true;
// console.log( typeof a);

// typed lanuage
// int a = 10;
// string name = "Jonathan"

// 1. while loop
// 2. do while loop
// 3. for loop

// var i = 1; // initalization
// do {
//   console.log("Jonathan ", i);
//   i = i + 1; // Increment
// } while (i >= 10);
// // condition to stop loop

// for(var i=1;i<=10;i++)
// console.log("Jonathan ", i);

// array
var arr = [2, 4, 6, 8, 9];
// console.log(arr);
// arr.push("Yanic");
// console.log(arr);
// arr.unshift("Pankaj");
// console.log(arr);
// arr.pop();
// console.log(arr);
// arr.shift();
// console.log(arr);
// console.log(arr.length);

// for (var i = 0; i < arr.length; i++) console.log(arr[i]);

// [2,4,6,8,9]

// callback is a function that is used as argument inside another function
// arr.forEach(function displayArr(i){        // ES5 (EcmaScript)
//     console.log(i*2);
// });

// Object
// JSON  : It becomes communication stadard between client - Server
// (JavaScript Object Notation)
// XML

var emp1 = {
  name: "Aric",
  email: "aric@abc.com",
  mobile: 083499847589,
  age: 30,
  address: "new york",
};

// console.log(emp1);
// console.log(emp1.address);


var arrobje = [
  { name: "Sara", email: "sara@abc.com",   mobile: 97348957,  age: 21,  address: "congo",   },
  { name: "Aric", email: "aric@abc.com",   mobile: 083499847589, age: 30,  address: "new york",  },
];

arrobje.forEach((i) => {
    console.log(i.name + " from " + i.address) ;
   
});