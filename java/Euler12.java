package solutions;

public class Euler12 {
	
	public static void main(String[] args) {
		int n = 0;
		int tri_n = 0;
		int num_div = 0;
		
		while(num_div<=500){
			num_div = 0;
			n++;
			tri_n += n;
			for(int i=2; i<= tri_n + 1; i++){
				if(tri_n%i == 0){
					num_div++;
				}
			}
			num_div += 1;
			System.out.println(n + " " + tri_n + " " + num_div);
		}
		
		System.out.println(tri_n);
	}

}
