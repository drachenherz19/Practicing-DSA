#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t; cin>>t;
   while(t>0)
   { 
    int e,k,n=0,fac=0;
    cin>>e>>k;
   
    while(e)
    {
     e = floor(e/k);
     fac++;
    } 
    cout<<fac<<endl;
   
   
    t--;
   }
   
   
    return 0;
}
    