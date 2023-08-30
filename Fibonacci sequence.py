aterms = int(input("Enter the terms? ")) 
def check(number): 
    if number <=0:
        return"Negative Integer"
    else:
        return"positive Integer"

def FibRec(num):  

   if num <= 1:  

       return num  

   else:  

       return(FibRec(num-1) + FibRec(num-2))  


print(check(aterms))
  
print("Fibonacci sequence:")  

for z in range(aterms):  

       print(FibRec(z))





#Java Script code
var n = prompt("enter number");
  var fun=check(n)
   alert(fun);
function check(n)
{
  if(n <=0)
  {return "Negative Integer"}
  else
  {
    return "positive Integer"
  }
  
}
var x=[];

if (n > 0)
{
  if (n==1)
  {
      x = [0];
      alert(x);
  }
  else if (n==2)
  {
      x=[0,1];
      alert(x);
  }
else{
    x=[0,1];
    while(x.length<n){
    var t =x[x.length-1]+x[x.length-2]
    x.push(t);}
    alert(x);
}
}
