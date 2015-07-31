function takeANumber(line,name)
{
  line.push(name);
  console.log("You are number " + line.length);
  return line.length;
}

function nowServing(line)
{
  console.log("Now serving " + line.splice(0,1));
}

function spot(line, name)
{
  for(var i = 0; i < line.length; i++)
  {
    if(line[i] == name)
    {
      //console.log(i + 1);
      return i+1;
    }
  }
  console.log("You ain't in line.");
}

var position = takeANumber(["mik", "bry", "linh", "max"]);
