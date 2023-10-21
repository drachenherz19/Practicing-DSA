int main() {
    int n;
    //input the size of array
    cin>>n;
    int  arr[n];
  
    //input the array elements
    for(int i=0; i<n; i++){
        cin>>arr[i];
    }
    
    //print reverse order of the array
    for(int j=n-1; j>=0; --j)
    {   
        cout<<arr[j]<<" ";   
    }   
    return 0;
}