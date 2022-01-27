import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		System.out.println(leap(N));
		sc.close();
}
	public static int leap(int year) {
		if(((year%4 == 0) && (year%100 != 0)) || (year%400 == 0))
			return 1;
		return 0;
	}
}
