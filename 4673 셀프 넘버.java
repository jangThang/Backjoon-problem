public class Main {
	public static void main(String[] args) {
		final int MAX_NUM = 10001;
		int[] selfNumberFlag = new int[MAX_NUM];
		
		for(int num=1; num<MAX_NUM; num++) {
			int notSelfNumber = notSelfNumber(num);
			
			if(notSelfNumber < MAX_NUM) {
				selfNumberFlag[notSelfNumber] = 1;
			}
		}
		
		for(int i=1; i<MAX_NUM; i++) {
			if(selfNumberFlag[i] == 0) {
				System.out.println(i);
			}
		}

	}
	
	public static int notSelfNumber(int num) {
		int result = num;
	
		while(num > 0) {
			result += num % 10;
			num /= 10;
		}
		
		return result;
	}
}
