// P127 5-8
#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

const int MAX_COL = 50;

void print(const string &s, int length, char extra)
{
    cout << s;
    for (int i = 0; i < length - s.length(); i++)
    {
        cout << extra;
    }
}

int main()
{
    int n;
    cin >> n;
    vector<string> words;

    int M = 0;
    for (int i = 0; i < n; i++)
    {
        string tmp;
        cin >> tmp;
        if (tmp.length() > M)
        {
            M = tmp.length();
        }
        words.push_back(tmp);
    }

    sort(words.begin(), words.end());

    int col = int((double)(MAX_COL + 2) / (M + 2));
    int row = int((double)(n - 1) / col) + 1;

    for (int r = 0; r < row; r++)
    {
        for (int c = 0; c < col; c++)
        {
            if (c * row + r >= n)
            {
                continue;
            }
            int index = c * row + r;
            if (c == col - 1)
            {
                print(words.at(index), M, ' ');
            }
            else
            {
                print(words.at(index), M + 2, ' ');
            }
        }
        cout << endl;
    }

    cin >> n;
    return 0;
}