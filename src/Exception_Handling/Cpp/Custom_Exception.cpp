# include <iostream>
using namespace std;

/* Cpp does not handle exception like conventional oop languages */

void func(){
    throw "Custom Exception";
}

int main(){

    try{
        func();
    }catch(const char *message){
        cout << message << endl;
    }

    return 0;
}