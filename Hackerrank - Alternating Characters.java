import java.io.*;
import java.math.*;
import java.util.*;

public class Solution {
public static void main (String args[])
{
Scanner sc = new Scanner (System.in);
     int n= sc.nextInt();
     int count = 0;
        
   for(int i=0; i<n; i++)
   {
       String s=sc.next();
       int l=s.length();
       count=0;
       for(int j=0; j<l-1; j++)
       {
           if(s.charAt(j) == s.charAt(j+1))
           {
               count++;
           }
       }
       System.out.println(count);
   }
    }
}