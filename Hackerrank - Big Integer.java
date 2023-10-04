import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import java.math.BigInteger;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner (System.in);
        BigInteger a = new BigInteger (sc.next());
        BigInteger b = new BigInteger (sc.next());
        BigInteger sum = a.add(b);
        BigInteger pro = a.multiply(b);
        System.out.println(sum);
        System.out.println(pro);
    }
    }
