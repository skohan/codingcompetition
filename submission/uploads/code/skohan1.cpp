#include <bits/stdc++.h>

using namespace std;

typedef unsigned long long ull;
typedef long long ll;

#define nl "\n"

const int mod = 1e9 + 7;

int smalla = 97;
int biga = 65;


void solve()
{
	string s;
	cin >> s;
	int q;
	cin >> q;

	int arr[26][s.size()+1] = {0};
	for(int i = 0; i < 26; i++)
		arr[i][0] = 0;

	int j = 1;

	for(char c: s)
	{
		for(int i = 0; i < 26; i++)
		{
			arr[i][j] = arr[i][j-1];
			if (c-'a' == i)
				arr[i][j]++;
		}
		j++;
	}

	// for(int i = 0; i < 26; i++)
	// {
	// 	cout << (char)('a'+i) << " ";
	// 	for(j = 0; j < s.size()+1; j++)
	// 		cout << arr[i][j] << " ";

	// 	cout << nl;
	// }

	while(q--)
	{
		int l,r;
		cin >> l >> r;

		assert(r <= s.size());

		bool odd = false;
		int len = 0;

		// cout << "L " << l << " R " << r << nl;

		for(int i = 0; i < 26; i++)
		{
			int count = arr[i][r] - arr[i][l-1];

			// cout << count << nl;

			if(count&1) odd = true;

			len += count/2;
		}

		len = 2*len;

		if(odd)
			len++;

		cout << len << nl;
	}
}


int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t = 1;
    // cin>>t;

    int c = 1;

    while(t--)
    {
        // cout << "Case #" << c <<": " ;

        solve();
        c++;
    }
}
