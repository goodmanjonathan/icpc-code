import java.util.Scanner;

public class Coins {
    public static void main(String[] args) {
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
}
