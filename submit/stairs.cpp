#include <iostream>

using namespace std;

int func(int step)

{

    if (step==1)return 1;

    if (step==2)return 2;

    return func(step-1)+func(step-2);

}



int main()

{

    int n;

    cin >> n;

    cout << func(n);

    return 0;

}