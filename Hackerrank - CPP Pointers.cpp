void update(int *a,int *b) {
       int x = *a;
       *a =  x + *b;
       *b = abs(x - *b);
}
int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    cin>>a>>b;
    update(pa, pb);
    cout<<a<<"\n"<<b;
    return 0;
}