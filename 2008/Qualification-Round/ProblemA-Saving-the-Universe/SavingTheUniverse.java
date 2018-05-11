import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Scanner;
import java.util.Set;

/**
 * @author baiqiang
 *
 */
public class SavingTheUniverse {
    private static final Scanner in = new Scanner(System.in);
    static int caseNum;
    
    static int switchNum = 0;
    
    static void readCaseLine() {
        caseNum= Integer.parseInt(in.nextLine());
    }
    
    static void minSwitch() {
        for(int i = 0; i < caseNum; i++) {
            switchNum = 0;
            
            int engineNum = Integer.parseInt(in.nextLine());
            
            Set<String> engines = new HashSet<>();
            List<String> queries = new ArrayList<>();
            
            for(int j = 0; j < engineNum; j++) {
                engines.add(in.nextLine());
            }
            int queryNum = Integer.parseInt(in.nextLine());

            for(int j = 0; j < queryNum; j++) {
                queries.add(in.nextLine());
            }
            
            Set<String> visited = new HashSet<>();
            for(String q : queries) {
                if(!visited.contains(q)){
                    visited.add(q);
                }
                if(visited.size() == engineNum) {
                    switchNum++;
                    visited = new HashSet<>();
                    visited.add(q);
                }
            }
            
            System.out.println("Case #" + (i + 1) + ": " + switchNum);
        }
    }
    
    public static void main(String[] args) {
        readCaseLine();
        minSwitch();
    }
}
