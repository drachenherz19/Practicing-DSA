import java.io.*;
import java.math.*;

import java.util.*;

public class Solution {
    
    public static void main(String args[])  {   
        
   Scanner sc = new Scanner(System.in);
   int n=sc.nextInt();
   int k=sc.nextInt();
   int height; int max=-1;
   for(int i=0; i<n; i++)
   {
       height=sc.nextInt();
       if (height>max)
       {
           max=height;
       }
   }
   if(k<max)
   {
       int potion= max-k;
       System.out.println(potion);
   }
   else
   {
     System.out.println(0);  
   }
    }
}
