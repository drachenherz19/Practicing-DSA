import java.io.*;
import java.math.*;
import java.util.*;

public class Solution {

       public static void main(String[] args){
       Scanner sc = new Scanner(System.in);
         int n= sc.nextInt(); int max=-1; int min = 1000000000;
         int[] arr= new int [n]; int maxcount=0; int mincount=0;
         for(int i=0; i<n; i++)
         {
             arr[i]=sc.nextInt();
             int copy= arr[0];
             if(arr[i]>max)
             {
                 max=arr[i];
                 maxcount++;
             }
             if(arr[i]<min)
             {
                 min=arr[i];
                 mincount++;
             }
         }
         System.out.println((maxcount-1)+" "+(mincount-1));
    }
}