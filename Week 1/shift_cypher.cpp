#include <bits/stdc++.h>
using namespace std;

float table[150];
void getf()
{
    float x[26] = {8.2, 1.5, 2.8, 4.3, 12.7, 2.2, 2, 6.1, 7, 0.2, 0.8, 4,
                   2.4, 6.7, 7.5, 1.9, 0.1, 6, 6.3, 9.1, 2.8, 1, 2.4, 0.2, 2, 0.1};
    for (int i = 'A'; i <= 'Z'; ++i)
    {
        table[i] = x[i - 'A'];
        
    }
}

string emphasize(string a)
{
    int len = a.size();
    for (int i = 0; i < len; ++i)
    {
        if (a[i] > 'Z')
        {
            a[i] -= 'a' - 'A';
        }
    }
    return a;
}

string encription1(string input, int k)
{
    string b = input;
    int len = input.size();
    for (int i = 0; i < len; ++i)
    {
        if (input[i] <= 'Z' && input[i] >= 'A')
        {
            b[i] = (input[i] + k - 'A') % 26 + 'A';
        }
        else if (input[i] <= 'z' && input[i] >= 'a')
        {
            b[i] = (input[i] + k - 'a') % 26 + 'a';
        }
    }
    return b;
}

int decription1(string output)
{
    string o = emphasize(output);
    int len = 0, ans = 0, l = o.size();
    float minLoss = 10000000;

      for (int i = 0; i < l; ++i)
    {
        if (o[i] <= 'Z' && o[i] >= 'A')
        {
            len++;
        }
    }
    for (int i = 0; i != 26; ++i)
    {
        string input = encription1(o, 26 - i);
        map<char, float> f;

        for (int j = 0; j != len; ++j)
        {
            f[input[j]]++;
        }

        float sum = 0;
        for (int k = 'A'; k <= 'Z'; ++k)
        {
            sum += (f[k]/len * 100 - table[k]) * (f[k] / len * 100- table[k]);
        }

        if (sum < minLoss)
        {
            minLoss = sum;
            ans = i;
        }
    }

    return ans;
}

int main()
{
    string a, b;
    getf();
    a = "The National Education Union (NEU) met the education secretary, Nadhim Zahawi, 
    on Wednesday to challenge him over evidence used to support the government's drive for full academisation 
    by 2030, announced in the schools white paper earlier this week.";
    b = encription1(a, 10);
    cout << decription1(b) << endl;
    return 0;
}