#include <cmath>
#include <cstring>
#include <iostream>
#include <sstream>
#include <string>

using namespace std;

int main(int argc, char *argv[]) {

  string val;
  cin >> val;
  int count = val.length();
  if (count <= 10) {
    int num = stoi(val);
    int curr_val = 1;
    while (num != 1) {
      num = num / curr_val;
      curr_val += 1;
    }
    curr_val -= 1;
    if (curr_val == 0)
      curr_val = 1;
    cout << curr_val << endl;
    return 0;
  }

  double logval = 0;
  int i = 1;
  while (1) {
    logval += log10(i);
    if (val.length() - logval <= 1) {
      cout << i << endl;
      return 0;
    }
    i++;
  }
}