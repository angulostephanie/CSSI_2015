var isRobAwesome = "yas";
var colorOfRobsShirt = "yellow";

console.log("Hello World!");
console.log("What's cooking good looking?");
console.log("You better like pugs");
console.log("Do I like pugs? " + isRobAwesome);

function checkout(item1, item2, coupon)
{
  var subtotal = item1 + item2;
  subtotal = subtotal * (1 -coupon);
  var total = subtotal * (1.095);
  total = Math.round(total * 100)/100;
  return total;

}

function goToLunch(name)
{
  alert("Lunch time!");
  alert("Close your computer, " + name);
  console.log("LET'S EAT FOOD");
}

function roll()
{
  var die = Math.ceil((Math.random()*6));
  return die;
}

function rollBoth()
{
  var firstRoll = roll();
  var secondRoll = roll();
  console.log("First round = " + firstRoll +
  " Second roll = " + secondRoll);
}


function howAmIDoing(gpa, isFootballPlayer, needGradSchool)
{
if (gpa >= 4.0)
  {
  alert("I'm friggin awesome");
  }
  else if (gpa >= 3.0 && needGradSchool)
  {
    console.log("Better get a job");
  }
    else if (gpa >= 3.0)
    {
      alert("Not too shabby");
    }
      else if(isFootballPlayer == true)
        {
          alert("I'm happy either way");
        }
        else {
          alert("Crap! Better study");
        }
}

var myArr = new Array();
myArr = ["Hikes", "Runs", "Coding", "Eating",
"Hanging out", "Exploring", "Netflix"];
var fruits = new Array();
fruits = ["Apples", "Oranges", "Pears",
"Bananas"];

var numbers = [2, 3, 5, 7, 11, 13, 17, 23];
var i = 0;
while(i < numbers.length)
{
  numbers[i] = numbers[i] + 1;
  i++;
}


function multByTwo(arr)
{
  var arr = [1, 5, 9, 10, 23, 36]
  /*
  var i = 0;
  while(i < arr.length)
  {
    arr[i] = arr[i]*2;
    i++;
  }
  return arr;
  */
  for(var i = 0; i < arr.length; i++)
  {
    arr[i] = arr[i] * 42;
    console.log(arr[i]);
  }
  return arr;
}

function
