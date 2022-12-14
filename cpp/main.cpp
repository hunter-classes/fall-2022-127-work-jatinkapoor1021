#Both working if and loop and working function done



#include<iostream>
using namespace std;

int absolute(int x)
{
	if(x>0)
	  return x;
	  
	else
	  return -1*x;
}


int main()
{
	cout<<"Hello World! \n";
	
	//working of if
	int a = 10,b=20;
	if(a>b)
	 cout<<"a is greater whose value is "<<a<<"\n";
	else
	 cout<<"b is greater whose value is "<<b<<"\n";
	 
	//working of loops
	int n = 5;
	int sum = 0;
	
	//sum of numbers till n
	for(int i=1;i<=n;i++)
	  sum = sum + i;
	  
	cout<<"Sum of numbers till n is "<<sum<<"\n";
	
	
	int number = -200;
	cout<<"Absolute value of the number is "<<absolute(number)<<"\n";
	
	
	
	
}
