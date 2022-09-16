7. 
from test import testEqual

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


testEqual(is_even(8), True)
testEqual(is_even(3), False)

8. 
def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return n % 2 > 0
  

10.
def is_rightangled(a,b,c):

     if abs(c**2 - (a**2 + b**2) < 0.001):

           return "True"

     else:

           return "False"

       

a = float(input("Side 1: "))

b = float(input("Side 2: "))

c = float(input("Side 3: "))

print(is_rightangled(a,b,c))

11.
from test import testEqual

def is_rightangled(a, b, c):
    is_rightangled = False

    if a > b and a > c:
        is_rightangled = abs(b**2 + c**2 - a**2) < 0.001
    elif b > a and b > c:
        is_rightangled = abs(a**2 + c**2 - b**2) < 0.001
    else:
        is_rightangled = abs(a**2 + b**2 - c**2) < 0.001
    return is_rightangled

testEqual(is_rightangled(3.0, 2.0, 2.5), True)
testEqual(is_rightangled(4.0, 12.0, 16.0), False)


Coding bat: 

hello_Name: 
public String helloName(String name) {

  return "Hello " + name + "!";

}

make_out_word: 
  public String makeOutWord(String out, String word) {
    return out.substring(0, 2) + word + out.substring(2);
}

first_two:
  public String firstTwo(String str) {

  int len = str.length();

  if (len < 2)

    return str;

  else

    return str.substring(0,2);

}
