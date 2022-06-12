import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		int b = sc.nextInt();
		int c = sc.nextInt();
		int d = sc.nextInt();
		
		double zero = (double)a/c + (double)b/d;
		double one = (double)c/d + (double)a/b;
		double two = (double)d/b + (double)c/a;
		double three = (double)b/a + (double)d/c;
		
		if((zero >= one) && (zero >= two) && (zero >= three)) {
			System.out.println(0);
		}
		else if((one >= zero) && (one >= two) && (one >= three)) {
			System.out.println(1);
		}
		else if((two >= zero) && (two >= one) && (two >= three)) {
			System.out.println(2);
		}
		else {
			System.out.println(3);
		}
		// System.out.println(a + " " + b + " " + c + " " + d);
		// System.out.println(zero + " " + one + " " + two + " " + three);
	}
}
