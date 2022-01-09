import java.util.*;

public class Main {
    // 순차탐색
    public static int sequantialSearch(int n, String target, String[] arr) {
        // 각 원소를 하나씩 확인 하며,
        for (int i = 0; i < n; i++) {
            System.out.println(arr[i]);
            // 현재의 원소가 찾고자 하는 원소와 동일한 경우
            if (arr[i].equals(target)) {
                return i+1; // 현재 위치 반환
            }
        }
        // 찾지 못한 경우 -1 반환
        return -1;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.");
        int n = sc.nextInt();
        String target = sc.next();

        System.out.println("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.");
        String[] arr = new String[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.next();
        }

        // 순차 탐색 수행 결과 출력
        System.out.println(sequantialSearch(n, target, arr));
    }
}