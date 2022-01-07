import java.util.*;

public class Main {
    public static void recursiveFunction(int i) {
        if (i==100) return;
        System.out.println(i + " to " + (i+1));
        recursiveFunction(i + 1);
        System.out.println("exit " + i);
    }
    public static void main(String[] args) {
        recursiveFunction(1);
    }
}