import java.io.*;
import java.math.*;
import java.util.*;
public class Solution {

    public static void main(String[] args){
      Scanner sc = new Scanner(System.in); 
      int n=sc.nextInt();
       int f=5;
        int cum=0;  
      for(int i=0; i<n; i++)
      {
         f= (int)Math.floor(f/2);
         cum=cum+f;
         f=f*3;
      }
      System.out.println(cum);
    }
}
