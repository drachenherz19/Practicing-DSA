#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t; cin>>t;
   while(t>0)
   { 
    int a,b,c=0;
    cin>>a>>b;
    c=a+b;
    if(c<3)
    {
        cout<<"1"<<endl;
    }
    else if ((c>=3)&&(c<=10))
    {
        cout<<"2"<<endl;
    }
    else if ((c>=11)&&(c<=60))
    {
        cout<<"3"<<endl;
    }
    else
    {
        cout<<"4"<<endl;
    }
    
    t--;
   }
   
    return 0;
}