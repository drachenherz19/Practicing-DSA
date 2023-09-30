import java.io.*;
import java.math.*;
import java.util.*;
import java.util.Arrays;
public class Solution {
   
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n =sc.nextInt();
        int[] arr = new int [n];
        for(int i=0; i<n; i++)
        {
            arr[i]=sc.nextInt();
        }
        Arrays.sort(arr);
        System.out.println(arr.length);
        for (int j = 1; j < arr.length; j++)
        {
            if (arr[j] != arr[j-1])
            {
                System.out.println(arr.length - j);
            }
        }
    }
}
