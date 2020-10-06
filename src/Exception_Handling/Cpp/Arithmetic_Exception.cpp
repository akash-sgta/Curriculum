#include <iostream>
using namespace std;

/* Cpp does not handle exception like conventional oop languages */

int main(){

    int i=10, j;
    float k=0;
    cin >> j;
    try{
        if(j == 0)
            throw "Arithmetic Exception : Division by zero.";
        k = i/j;
    }catch(const char *excep){
        cout << "Exception : " << excep << endl;
    }
    cout << k << endl;

    return 0;
}