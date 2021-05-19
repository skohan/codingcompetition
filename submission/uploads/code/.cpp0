#include <iostream>
#include <bits/stdc++.h>

using namespace std;

#define ull unsigned long long
#define ll long long
#define nl "\n"
#define INTBITS 32
#define kickstartoutput cout << "Case #" << tc << ": "
const int mod = 1000000007;

int smalla = 97;
int biga = 65;

class Foo
{

    bool first_done, second_done;

public:
    Foo()
    {
        this->first_done = false;
        this->second_done = false;
    }

    void first()
    {
        cout << "FIRST" << nl;
        this->first_done = true;
    }

    void second()
    {
        ll i = 0;
        while (!this->first_done)
            i++;
        // cout << "IN LOOP" << nl;
        // printSecond() outputs "second". Do not change or remove this line.
        cout << "SECOND" << nl;
        this->second_done = true;
    }

    void third()
    {
        ll i = 0;
        while (!this->second_done)
            i++;
        // printThird() outputs "third". Do not change or remove this line.
        cout << "THIRD" << nl;
    }
};

int main()
{

    // ios_base::sync_with_stdio(false);
    // cin.tie(NULL);
    Foo foo = Foo();

    // thread t1([](Foo *foo){foo->first();}, &foo);
    // thread t2([](Foo *foo){foo->second();}, &foo);
    // thread t3([](Foo *foo){foo->third();}, &foo);

    // t1.join();
    // t2.join();
    // t3.join();

    int i = 0;
    while (++i < 1000000)
        ;
    cout << "HERE " << i << nl;
    return 0;
}
