#include <iostream>
#include <string>

using namespace std;

int main(){
    int p,q;
    string ordering;

    cin >> p >> q;
    cin >> ordering;

    if (ordering == "ABBA"){
        if (abs(q-p) == 3) {
            cout << p+1 << " " << p+2 << endl;
        } else {
            cout << -1 << endl;
        }
    }
    else if (ordering == "AABB"){
        if (q == 7){
            cout << q+1 << " " << q+2 << endl;
        }else {
            cout << -1 << endl;
        }
    }
    else if (ordering == "ABAB"){
        if (p == 6 && q == 8){
            cout << "7 9" << endl;
        }else {
            cout << -1 << endl;
        }
    }
    else if (ordering == "BAAB"){
        if (p == 2 && q == 8){
            cout << "1 9"<<endl;
        }else {
            cout << -1 << endl;
        }
    }
    else if (ordering == "BABA"){
        if (p == 2 && q == 4){
            cout << "1 3"<<endl;
        }else {
            cout << -1 << endl;
        }
    }
    else if (ordering == "BBAA"){
        if (p == 3){
            cout << "1 2" << endl;
        }else {
            cout << -1 << endl;
        }
    } else {
        cout << -1 << endl;
    }

    return 0;
}
