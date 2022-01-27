import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int[] num = new int[10];
		for(int i = 0; i < 10; i++) {
			num[i] = sc.nextInt();
			num[i] %= 42;
		}
		int sum = 10;
		int same = 0;
		for(int i = 0; i < 10; i++) {
			for(int j = i; j < 10; j++) {
				if(num[i] == num[j]) 
					same++;
			}
			if(same > 1) {
				sum -= 1;
			}
			same = 0;
		}
		System.out.println(sum);
		sc.close();
	}
}
