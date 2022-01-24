import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		sc.close();
		
		int a;
		int ans = -1;
		for (a = 0; a * 5 <= N; a++)
			if ((N - a * 5) % 3 == 0)
				ans = a + ((N - a * 5) / 3);
		System.out.println(ans);
	}
}
