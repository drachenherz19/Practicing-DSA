import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        int n= A.length();
        String copy = A; String str = "";
        
        for(int i=n-1; i>=0; i--)
        {
            str = str + A.charAt(i);
        }
        if(str.equals(A))
        {
            System.out.println("Yes");
        }
        else
        {
          System.out.println("No");  
        }
    }
}
