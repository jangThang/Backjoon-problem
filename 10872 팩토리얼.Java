import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int time = sc.nextInt();
		sc.close();
		System.out.print(factorial(time));
	}
	public static int factorial(int a) {
		int result = 1;
		for(int i = 1; i <= a; i++) {
			result *= i;
		}
		return result;
	}
}
