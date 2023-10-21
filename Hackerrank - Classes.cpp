class Student{
    private:
        int age;
        string firstName;
        string lastName;
        int standard;
    public:
        void set_age(int a){
            age = a;
        }
        int get_age(){
            return age;
        }
        void set_first_name(string fName){
            firstName = fName;
        } 
        string get_first_name(){
            return firstName;
        }
        void set_last_name(string lName){
            lastName = lName;
        }
        string get_last_name(){
            return lastName;
        }
        void set_standard(int s){
            standard = s;
        }
        int get_standard(){
            return standard;
        }
        string to_string() {
        stringstream ss;
        ss << age << "," << firstName << "," << lastName << "," << standard;
        return ss.str();
    }
};