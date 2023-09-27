import java.io.*;
import java.math.*;
import java.lang.*;
import java.text.*;
import java.util.*;

public class Solution {
    
    public static void main(String[] args) {
        
      Scanner sc = new Scanner(System.in);
      int count=1; String s=sc.next(); int l=s.length();
      char[] carray = s.toCharArray();
      for(int i=0; i<l; i++)
      {
          if(Character.isUpperCase(carray[i]) == true)
          {
              count++;
          }
      }
     System.out.println(count);
    }
}