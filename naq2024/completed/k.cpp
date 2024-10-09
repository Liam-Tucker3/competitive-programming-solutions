#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define fi first
#define se second
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<double, double> pdd;

/* Rhythm Flow*/

int getScore(int n) {
    if (n <= 15 && n >= -15) return 7;
    if (n <= 23 && n >= -23) return 6;
    if (n <= 43 && n >= -43) return 4;
    if (n <= 102 && n >= -102) return 2;
    return 0;
}

int dp(vector<vector<int>> *grid, vector<int> *expected, vector<int> *actual, int n, int m, int nMax, int mMax) {
    // cout << n << ", " << m << endl;
    
    int thisScore, case1, case2;
    // Base Cases
    if (n >= nMax) return 0;
    if (m >= mMax) return 0;

    // Already Calculated
    if (grid->at(n).at(m) != -1) return grid->at(n).at(m);

    // Case 1: equal
    if (expected->at(n) == actual->at(m)) grid->at(n).at(m) = 7 + dp(grid, expected, actual, n+1, m+1, nMax, mMax);

    // Case 2 Button Pressed AFTER
    else if (expected->at(n) < actual->at(m)) {
        thisScore = getScore(actual->at(m) - expected->at(n));
        case1 = thisScore + dp(grid, expected, actual, n+1, m+1, nMax, mMax);
        case2 = dp(grid, expected, actual, n+1, m, nMax, mMax);
        if (case1 > case2) grid->at(n).at(m) = case1;
        else grid->at(n).at(m) = case2;
    }

    // Case 3 Button pressed BEFROE
    else {
        thisScore = getScore(expected->at(n) - actual->at(m));
        case1 = thisScore + dp(grid, expected, actual, n+1, m+1, nMax, mMax);
        case2 = dp(grid, expected, actual, n, m+1, nMax, mMax);
        if (case1 > case2) grid->at(n).at(m) = case1;
        else grid->at(n).at(m) = case2;
    }

    return grid->at(n).at(m);

}



    int n, m, i, temp;
    cin >> n;
    cin >> m;

    // Getting values
    vector<int> *expected = new vector<int>(n);
    for (i = 0; i < n; i++) {
        cin >> temp;
        expected->at(i) = temp;
    }
    vector<int> *actual = new vector<int>(m);
    vector<int> *tempVector = new vector<int>(m);
    for (i = 0; i < m; i++) {
        cin >> temp;
        actual->at(i) = temp;
        tempVector->at(i) = -1;
    }

    vector<vector<int>> *grid = new vector<vector<int>>;
    for (i=0; i < n; i++) {
        grid->push_back(*tempVector);
    }

    // cout << "About to do dp" << endl;
    int result = dp(grid, expected, actual, 0, 0, n, m);
    // cout << "Back from dp" << endl;
    cout << result << endl;


    return 0;
}