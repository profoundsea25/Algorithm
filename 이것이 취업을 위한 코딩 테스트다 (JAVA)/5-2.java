import java.util.*;

public class Main {

    public static void main(String[] args) {
        Queue<Integer> s = new LinkedList<>();

        s.offer(5);
        s.offer(2);
        s.offer(3);
        s.offer(7);
        s.poll();
        s.offer(1);
        s.offer(4);
        s.poll();
        // 먼저 들어온 원소부터 추출
        while(!s.isEmpty()) {
            System.out.println(s.poll());
        }
        // 출력값(최상단) 3 7 1 4
    }
    
}
