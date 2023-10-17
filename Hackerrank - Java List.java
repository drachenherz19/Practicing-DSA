public class Solution {

public static void main(String[] args) {

Scanner scan =new Scanner(System.in);

int N=scan.nextInt();

List<Integer> L = new ArrayList();

for(int i=0;i<N;i++){
    int x = scan.nextInt();
    L.add(x);
}
    int Q = scan.nextInt();
    for(int j=0;j<Q;j++){
        String s = scan.next();

        if(s.equals("Insert")){

            int a = scan.nextInt();
            int b = scan.nextInt();

        L.add(a,b);
        }
        else {
                int c = scan.nextInt();
                L.remove(c);
            }
        }
        for(int x : L){
            System.out.print(x+" ");
        }
} }