
#include <string>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    string x;
    //Convert each number into binary and then use that to print out dots and asterisks
    //asterisk is 1, dot is 0
    cin >> x;
    char digit;
    string binary;
    vector<string> binList;
    for(int i = 0; i < x.length(); i++)
    {
        digit = x[i];
        if(digit == '0')
        {
            binary = "0000";
        }
        else if(digit == '1')
        {
            binary = "0001";
        }
        else if(digit == '2')
        {
            binary = "0010";
        }
        else if(digit == '3')
        {
            binary = "0011";
        }
        else if(digit == '4')
        {
            binary = "0100";
        }
        else if(digit == '5')
        {
            binary = "0101";
        }
        else if(digit == '6')
        {
            binary = "0110";
        }
        else if(digit == '7')
        {
            binary = "0111";
        }
        else if(digit == '8')
        {
            binary = "1000";
        }
        else if(digit == '9')
        {
            binary  = "1001";
        }
        binList.push_back(binary);
    }

    for(int i = 0; i < 4; i++)
    {
        for(int j = 0; j < binList.size(); j++)
        {
        //first element of each string, then second element of each string, etc.
        digit = binList.at(j)[i];
        if(digit == '0')
        {
            if(j == 0 || j == 1)
            {
                cout << ". ";
            }
            else if(j == 2)
            {
                cout << "  . ";
            }
            else
            {
                cout << ".";
            }
            
        }
        else
        {
            if(j == 0 || j == 1)
            {
                cout << "* ";
            }
            else if(j == 2)
            {
                cout << "  * ";
            }
            else
            {
                cout << "*";
            }
            
        }

        }
        cout << endl;
        
    }

}