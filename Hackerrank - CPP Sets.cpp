int main() {

int q,x,y;
cin>>q;

set<int> s;
set<int> :: iterator iter;

while(q>0){
    cin>>y>>x;
    q--;

    switch (y) {
        case 1:
        s.insert(x);  
        break;

        case 2:
        s.erase(x);
        break;

        case 3:
        iter = s.find(x);
        if(iter!=s.end()){
            cout<<"Yes"<<endl;
        }
        else {
            cout<<"No"<<endl;
        }
    }
}

return 0;
}