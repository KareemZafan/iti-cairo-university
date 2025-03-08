#include <stdio.h>


double add(double a , double b){

 return a + b ; 
}

long abs (long a){
 
  return a > 0 ? a : -a; 
}

int main(){

int a = 10 ; 
int b = 20; 

printf("Hello World"); 
printf("%d + %d = %d" ,a,b,add(a , b));  // 10 + 20 = 30

return 0; 
}
