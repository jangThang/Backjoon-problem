import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String a = sc.next();
		String b = sc.next();
		int rA = 0;
		int rB = 0;

		int tmp = 1;
		for(int i = 0; i < a.length(); i++) {
			rA += (Integer.parseInt(a.substring(i, i+1)) * tmp);
			tmp *= 10;
		}
		tmp = 1;
		
		for(int i = 0; i < b.length(); i++) {
			rB += (Integer.parseInt(b.substring(i, i+1)) * tmp);
			tmp *= 10;
		}
		
		System.out.println( (rA > rB) ? rA : rB );
		sc.close();
	}
}
