import java.io.*;
import java.math.*;
import java.util.*;

public class Solution {
     public static void main(String[] args){
       
       Scanner sc = new Scanner(System.in);
       String s = sc.next();
       int n =s.length();
       String sample = "abcdefghijklmnopqrstuvwxyz";
       int odd=0, even=0;
       for(int i=0; i<26; i++)
       {
           int count=0;
           for(int j=0; j<n; j++)
           {
               if(sample.charAt(i)==s.charAt(j))
               {
                   count++;
               }
           }
           if(count%2==0)
           {
               even++;
           }
           else
           {
               odd++;
           }
       }
       if(odd<=1)
       {
           System.out.println("YES");
       }
       else if ((odd==2) && (n%2==0))
       {
          System.out.println("YES");
       }
       else
       {
           System.out.println("NO");
       }
    }
    }