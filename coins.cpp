#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<int> split_ints(const string& s) {
    vector<int> split;
    const char *begin = s.data();
    size_t len = s.size();
    size_t space_idx;
    
    for (size_t i = 0; i < len;) {
        split.push_back(stoi(begin + i, &space_idx));
        i += space_idx;
    }
    
//    int prev_space = -1;
//
//    if (s.size() == 0)
//        return split; // empty vector
//
//    for (size_t i = s.find(' ', prev_space); i != string::npos; i = s.find(' ', prev_space)) {
//        cout << "i = " << i << '\n';
//        cout << "s = " << s << '\n';
//    
//        split.push_back(s.substr(prev_space + 1, i));
//        prev_space = i;
//    }
    
//    split.push_back(s.substr(prev_space + 1));    
    return split;
}

int main() {
    int case_amt;
    cin >> case_amt;
    cout << case_amt << '\n';
    
    for (int _case = 0; _case < case_amt; ++_case) {
        vector<int> coins;
        int n;
        int q;

        cin >> n >> q;
        cout << n << q << '\n';
        for (int i = 0; i < 11; ++i)
            coins.push_back(0);

        for (int i = 0; i < q; ++i) {         
            string tmp;
            cin >> tmp;
            vector<int> line_info = split_ints(tmp);

            if (line_info[0] == 1) {
                for (int i = line_info[1]; i < line_info[2] + 1; ++i)
                    coins[i % 10] += (i % 10) * line_info[3];
            } else if (line_info[0] == 2) {
                for (int i = line_info[1]; i < line_info[2] + 1; ++i)
                    coins[i % 10] = 0;
            } else if (line_info[0] == 3) {
                int total = 0;
                for (auto value : coins)
                    total += value;
                cout << total << '\n';
            }

        }
    }
}
