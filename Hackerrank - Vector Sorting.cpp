int scores[5];
    public:
    void input() {
        for (int i = 0;i < 5;i++) {
            cin >> scores[i];
        }
    }
    int calculateTotalScore() {
        int sum = 0;
        for (int i = 0; i < 5; i++) {
            sum += scores[i];
        }
        return sum;
int main() {
    vector<int> v;
    int N;
    int i;
    
    cin >> N;
    while(cin >> i) v.push_back(i);
    
    sort(v.begin(), v.end());
    
    i = -1;
    while(++i < v.size()) cout << v[i] << + " ";
    
    return 0;
}