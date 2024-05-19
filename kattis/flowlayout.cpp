#include <iostream>
using namespace std;

int main() {
  int maxWidth;
  cin >> maxWidth;
  while (maxWidth != 0) {
    int totalWidth = 0;
    int totalHeight = 0;
    int thisRowHeight = 0;
    int thisRowWidth = 0;
    int thisWidth;
    int thisHeight;

    while (true) {
      cin >> thisWidth;
      cin >> thisHeight;
      if (thisWidth == -1) {
        // then thisHeight is also 0
        totalHeight += thisRowHeight;
        if (totalWidth < thisRowWidth) totalWidth = thisRowWidth;
        cin >> maxWidth;
        if (maxWidth == 0) { // Then we're done and don't want a newLine
          cout << totalWidth << " x " << totalHeight;
          return 0;
        }
        cout << totalWidth << " x " << totalHeight << endl;
        thisRowHeight = 0;
        thisRowWidth = 0;
        totalHeight = 0;
        totalWidth = 0;
        break;
      }
      // Need to consider two cases: goes on a new row, and stays on this row

      // Stays on this row:
      if (thisRowWidth + thisWidth <= maxWidth) {
        thisRowWidth += thisWidth;
        if (thisHeight > thisRowHeight) thisRowHeight = thisHeight;
      }
      else {
        totalHeight += thisRowHeight;
        if (totalWidth < thisRowWidth) totalWidth = thisRowWidth;
        thisRowHeight = thisHeight;
        thisRowWidth = thisWidth;
      }
    }
  }


}