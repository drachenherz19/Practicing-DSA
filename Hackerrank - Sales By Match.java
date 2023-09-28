import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {
    public static void main(String[] args){
      Scanner sc = new Scanner(System.in);  
      int n=sc.nextInt();
      int[] arr= new int[10000];
      int temp1=0; int count=0;
      
      for(int i=0; i<n; i++)
      {
       int bob = sc.nextInt();   
      arr[bob]++;
     
      if(arr[bob]%2==0)
      {
          count++;
          arr[bob]=0;
      }
      
      }
      System.out.println(count);
    }
}

        

