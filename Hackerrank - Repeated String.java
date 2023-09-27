import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {
      
    public static void main(String[] args) {
         Scanner sc = new Scanner(System.in);
         String s = sc.next();
         long n = sc.nextLong();

        long Char = 0 ;
        int A = 0;
        
    if(s.length() > 0){
       for(int i=0;i<s.length();i++)
       {
          if(s.charAt(i)=='a'){
            A++;
          } 
       } 

       long division = n / s.length();
       long mod = n % s.length();
       Char = division * A;

       for(int i=0;i<mod;i++){
           if(s.charAt(i)=='a'){
               Char++;
           }
       }

    }

    System.out.println(Char);
}
}