public static void main(String[] args) {        
    Scanner sc = new Scanner(System.in);
    
    int n = sc.nextInt();
    ArrayList<ArrayList> arr = new ArrayList();  
    
    for(int i = 0; i < n; i++) {
        ArrayList subArr = new ArrayList();
        
        int d = sc.nextInt();
        for(int j = 0; j < d; j++) {
            int k = sc.nextInt();
            subArr.add(k);
        }    
        arr.add(subArr);
    }
    
    int q = sc.nextInt();
    for(int i = 0; i < q; i++) {
        int x = sc.nextInt();
        int y = sc.nextInt();
        
        try {
            System.out.println((arr.get(x-1)).get(y-1));
            
        } catch (IndexOutOfBoundsException e) {
            System.out.println("ERROR!");
        }
		
}    
        
    }
 
        
    }