import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		if(n == 0) {
			System.out.println(1);
			return;
		}
		int i = 0;
		int n1 = n;
		int n2 = 0;
		for(; n2 != n; i++) {
			n2 = n1%10 + n1/10;
			n2 = (n2%10) + (n1%10)*10;
			n1 = n2;
		}
		System.out.println(i);
		sc.close();
	}
}
