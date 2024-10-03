#include <iostream>
#include <string>
#include <set>

using namespace std;

int main(){

    int m,n;
    int target, current;
    int i,j, l, u;
    cin >> m;
    cin >> n; 
    int clusters[m];
    string output = "No";

    // Getting in values
    for (i = 0; i < m; i++) {
        cin >> target;
        clusters[i] = target;
    }
    // for (int i = 0; i <m; i++) {
    //     cout << clusters[i] << " | ";
    // }
    // cout << endl;

    // Performing test cases
    for (i = 0; i < n; i++) {
        // cout << "Start of test case " << i << endl;
        cin >> target;
        // cout << "Just did cin" << endl;
        l = -1;
        u = m;
        current=0;
        // cout << "l, u: " << l << " " << u << endl;
        while (l < m-1) {
            l += 1;
            current += clusters[l];
            if (current >= target) break;
        }
        // cout << "Finished first while" << endl;
        if (current < target) {
            cout << "No" << endl;
            continue;
        } else if (current == target) {
            // cout << "l: " << l << ", u: " << u << endl;
            cout << "Yes" << endl;
            continue;
        }
        // cout << "About to loop back down" << endl;

        // Looping i back down
        output = "No";
        while (l >= -1 and u > l) {
            // cout << "In down loop, l: " << l << ", u: " << u << ", current: " << current << ", target: " << target << endl;
            if (current == target) {
                // cout << "l: " << l << ", u: " << u << endl;
                output = "Yes";
                break;
            }
            else if (current < target) {
                u -= 1;
                current += clusters[u];
            }
            else {
                if (l == -1) break;
                current -= clusters[l];
                l -= 1;
            }
        }
        // cout << "Done looping back donw" << endl;
        cout << output << endl;
    }



    /*
    int clustersFront[m];
    int clustersBack[m];
    std::set<int> vals;
    vals.insert(0);

    for (i = 0; i < m; i++) {
        cin >> temp;
        clustersFront[i] = temp;
        clustersBack[i] = temp;
    }
    vals.insert(clustersFront[0]);
    vals.insert(clustersBack[0]);
    for (i = 1; i < m; i++) {
        clustersFront[i] += clustersFront[i-1];
        vals.insert(clustersFront[i]);
    }
    for (i = m-2; i >=0; i--) {
        clustersBack[i] += clustersBack[i+1];
        vals.insert(clustersBack[i]);
    }

    for (i = 0; i < m; i++) {
        for (j = m-1; j > i; j--) {
            vals.insert(clustersFront[i] + clustersBack[j]); 
        }
    }

    for (i = 0; i < n; i++) {
        cin >> temp;
        if (vals.count(temp)) cout << "Yes" << endl;
        else cout << "No" << endl;
    }
    */

    return 0;
}

/*
5 5
2 8 1 3 3
2
10
5
17
1
*/