#include <cmath>
#include <cstring>
#include <iostream>
#include <sstream>
#include <string>

int main() {

  int test_cases;
  std::cin >> test_cases;
  int val;

  int count = 0;
  while (count < test_cases) {
    std::cin >> val;
    if (val == 1)
      std::cout << "1" << std::endl;
    else if (val == 2)
      std::cout << "2" << std::endl;
    else if (val == 3)
      std::cout << "6" << std::endl;
    else if (val == 4)
      std::cout << "4" << std::endl;
    else
      std::cout << "0" << std::endl;
    count += 1;
  }
}