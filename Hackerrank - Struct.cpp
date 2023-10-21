#include<bits/stdc++.h>
using namespace std;
struct Solution{
    int age;
    string f_name;
    string l_name;
    int std;
    
    void set_data(int x,string fname,string lname,int Std){
        age = x;
        f_name = fname;
        l_name = lname;
        std = Std;
    }
    void show_data(){
        cout << age << " " << f_name <<" "<<l_name <<" "<<std;
        
        
    }
};
int  main(){
    Solution s;
    int x;
    string f_name,l_name;
    int k;
    cin >> x >> f_name >> l_name >> k;
    s.set_data(x,f_name,l_name,k);
    s.show_data();
    return 0;
}