#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int* stringToCode(string s) {
    int len = s.length();
    int* arr = new int[len];

    for (int i = 0; i < len; i++) {
        if (s.at(i) >= 'a' && s.at(i) <= 'z') {
            arr[i] = (1 + s.at(i) - 'a');
        }
        else arr[i] = 0;
    }

    return arr;

}

const string codeToString(int* arr, int len) {
    string s = "";

    for (int i = 0; i < len; i++) {
        if (arr[i] == 0) {
            s.push_back(' ');
        }
        else {
            s.push_back('a' - 1 + arr[i]);
        }
    }

    return s;

}

int main(int argc, char *argv[]) {

    int reps;
    string type;
    string input;
    int* codeArray;
    int len;

    cin >> reps;

    for (int r = 0; r < reps; r++) {
        cin >> type;
        cin.ignore(1); // remove space
        getline(cin, input);
        codeArray = stringToCode(input);
        len = input.length();

        if (type == "e") {
            for (int i = 1; i < len; i++) {
                codeArray[i] += codeArray[i-1];
            }
            for (int i = 1; i < len; i++) {
                codeArray[i] %= 27;
            }
            cout << codeToString(codeArray, len) << endl;
        }

        if (type == "d") {
            for (int i = len-1; i > 0; i--) {
                codeArray[i] -= codeArray[i-1];
            }
            for (int i = 1; i < len; i++) {
                codeArray[i] %= 27;
                if (codeArray[i] < 0) codeArray[i] += 27;
            }
            cout << codeToString(codeArray, len) << endl;
        }

        delete codeArray;
    }

    return 0;

}