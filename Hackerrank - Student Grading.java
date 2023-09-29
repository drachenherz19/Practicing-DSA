import java.io.*;
import java.math.*;
import java.util.Scanner;
import java.util.*;

class Solution {
    public static void main(String args[]){
        Scanner sc= new Scanner (System.in);
        int n=sc.nextInt(); int i; int grade=0;
        for(i=0;i<n;i++)
        {
            grade = sc.nextInt();
            int copy = grade;
            if ((grade > 37) && (grade <100))
            {
                int a = grade%10;
                int b= grade/10; 
                int c= 10 - a;
                if (a>5)
                {
                    int x = b*10 + 10;
                    if(x-copy < 3)
                    { 
                        grade= grade + c;
                        System.out.println(grade+" ");
                    }
                    else
                    {
                       System.out.println(grade+" "); 
                    }
                    
                }
                else if (a==5)
                {
                   System.out.println(grade+" "); 
                }
                else
                {
                    int p = 5-a;
                    int y=(10*b) + p + a;
                    if (y-grade < 3)
                    grade = grade +p;
                    System.out.println(grade+" ");
                }
            }
            else
            {
                System.out.println(grade+" ");
            }
        }
    }
}
    
