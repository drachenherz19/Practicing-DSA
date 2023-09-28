import java.io.*;
import java.text.*;
import java.util.*;
import java.util.Scanner;

public class Solution {
    
    public static void main(String[] args){
        
      Scanner sc = new Scanner(System.in);  
      int n=sc.nextInt();
      for(int i=0; i<n; i++)
      {
          int cata = sc.nextInt();
          int catb = sc.nextInt();
          int mouse = sc.nextInt();
          int d1= Math.abs(cata-mouse); int d2=Math.abs(catb-mouse);
          if(d1==d2)
          {
              System.out.println("Mouse C");
          }
          else if(d1>d2)
          {
              System.out.println("Cat B");
          }
          else
          {
              System.out.println("Cat A");
          }
      }
}
}
