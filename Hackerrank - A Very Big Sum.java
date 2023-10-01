import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        int n  = sc.nextInt();
        long sum = 0;
        for(int i = 0; i<n; i++)
        {
            sum = sum+ sc.nextInt();
        }
        System.out.println(sum);
    }
}
