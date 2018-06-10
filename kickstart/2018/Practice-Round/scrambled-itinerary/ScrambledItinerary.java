import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;


public class ScrambledItinerary {
	static Scanner in = new Scanner(System.in);
	
	static void solution(){
		int T = Integer.parseInt(in.nextLine());
		for(int caseNum = 1; caseNum <= T; caseNum++){
			int N = Integer.parseInt(in.nextLine());			
			String first = null;
			Map<String, String> start2end = new HashMap<>();
			Map<String, String> end2start = new HashMap<>();
			for(int i = 0; i < N; i++){
				String start = in.nextLine();
				String end = in.nextLine();
				if(i == 0){
					first = start;
				}
				start2end.put(start, end);
				end2start.put(end, start);
			}
			List<String> itinerary = new ArrayList<>();
			itinerary.add(first);
			String next = start2end.get(first);
			while(next != null){
				itinerary.add(next);
				if(start2end.get(next) != null){
					itinerary.add(next);
				}
				next = start2end.get(next);
			}
			if(end2start.get(first) != null){
				itinerary.add(0, first);
			}
			String last = end2start.get(first);
			while(last != null){
				itinerary.add(0, last);
				if(end2start.get(last) != null){
					itinerary.add(0, last);
				}
				last = end2start.get(last);
			}
			System.out.print("Case #" + caseNum + ":");
			for(int i = 0; i < itinerary.size();  i+=2){
				System.out.print(" " + itinerary.get(i) + "-" + itinerary.get(i + 1));
			}
			System.out.println();
		}
	}
	
	public static void main(String[] args) {
		solution();
	}
}
