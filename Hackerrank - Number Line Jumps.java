import java.io.*;
import java.math.*;
import java.util.*;

public class Solution {
    public static void main(String args[]) {
        
       Scanner sc = new Scanner(System.in);   
       int x1 = sc.nextInt();
       int v1 = sc.nextInt();
       int x2 = sc.nextInt();
       int v2 = sc.nextInt();
       int  count=0;
        
      if (v1 > v2)
         {
          if (((x1-x2)%(v1-v2))==0)
          { count++;} 
       }
       if (count > 0)
       {
           System.out.println("YES");
       }
       else
       {
           System.out.println("NO");
       }
    }
}
    