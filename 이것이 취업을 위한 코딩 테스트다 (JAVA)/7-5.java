import java.util.*;

public class Main {
    // 이진 탐색 이용
    public static int binarySearch(int[] arr, int target, int start, int end) {
        while (start <= end) {
            int mid = (start+end)/2;
            if (arr[mid] == target) return mid;
            else if (arr[mid] < target) start = mid + 1;
            else end = mid - 1; 
        }
        return -1;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] array = new int[n]; 
        for (int i = 0; i < n; i++) {
            array[i] = sc.nextInt();
        }

        int m = sc.nextInt();
        int[] array_need = new int[m];
        for (int i = 0; i < m; i++) {
            array_need[i] = sc.nextInt();
        }
        

        Arrays.sort(array);

        for (int i = 0; i < m; i++) {
            if (binarySearch(array, array_need[i], 0, n-1) != -1) {
                System.out.print("yes ");
            } 
            else {
                System.out.print("no ");
            }
        }
    }
}