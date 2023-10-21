vector<int> arr;
    int n,val,a,b,c;
    cin>>n;
    
    for(int i=0;i<n;i++){
        cin>>val;
        arr.push_back(val);
    }
    cin>>a>>b>>c;
    arr.erase(arr.begin()+ --a);
    arr.erase(arr.begin()+ --b , arr.begin()+ --c);
    
    cout<<arr.size()<<endl;
    for(int i:arr){
        cout<<i<<" ";
    }