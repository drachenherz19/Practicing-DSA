import java.io.*;
import java.math.*;

import java.util.*;

public class Solution {

    
    public static void main(String args[]) {
        Scanner sc = new Scanner (System.in);
        int orangecount=0;
        int s=sc.nextInt();
        int t=sc.nextInt();
        int apple=sc.nextInt();
        int orange = sc.nextInt();
        int m= sc.nextInt();
        int n=sc.nextInt();
        int applecount=0;
        for(int i=0; i<m; i++)
        {
            int applepos= apple + sc.nextInt();
            if (applepos >= s && applepos <=t)
            {
            applecount++;
            }
        }
        System.out.println(applecount);
        
        for(int j=0; j<n; j++)
        {
            int orangepos = orange +sc.nextInt();
            if (orangepos >=s && orangepos <=t)
            {
            orangecount++;
            }
        }
        System.out.println(orangecount);
    }
}
