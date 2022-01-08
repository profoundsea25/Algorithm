import java.util.*;

public class Main {
    // Java 내장 정렬
    public static void main(String[] args) {
        int n = 10;
        int[] arr = {7, 5, 9, 0, 3, 1, 6, 2, 4, 8};
        
        Arrays.sort(arr);

        for (int i = 0; i < n; i++) {
            System.out.print(arr[i] + " ");
        }
    }
}