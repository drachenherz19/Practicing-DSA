import java.io.*;
import java.math.*;
import java.util.*;
import java.util.Scanner;

public class Solution {

    public static void main(String args[]){
    Scanner sc = new Scanner(System.in);
    int t= sc.nextInt();
    int sum=1;
    for(int i=0; i<t; i++)
    {
        int n = sc.nextInt();
        
            if(n%2==0)
            {           
            System.out.println((int) (Math.pow(2, n/2)*2) -1);
            }
            else
            {
                System.out.println((int) ((Math.pow(2, (n-1)/2)*2) -1)*2);
            }
        
    }
}
}
