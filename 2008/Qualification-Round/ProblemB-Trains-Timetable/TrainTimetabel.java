/**
 * 
 */

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * @author baiqiang
 *
 */
public class TrainTimetabel {
    static Scanner in = new Scanner(System.in);

    static int N; // the number of cases
    static int T; // the turnaround time
    static int NA; // the number from A to B
    static int NB; // the number from B to A

    static void solution() {
        N = Integer.parseInt(in.nextLine());
        for (int k = 0; k < N; k++) {
            int Aneed = 0; // the number of trains that A station needs
            int Bneed = 0; // the number of trains that B station needs
            int Ahave = 0; // the number of trains that A station has
            int Bhave = 0; // the number of trains that A station has

            T = Integer.parseInt(in.nextLine()); // get T

            // get NA and NB
            String s = in.nextLine();
            Pattern tmp = Pattern.compile("(?<na>[0-9]+) (?<nb>[0-9]+)");
            Matcher mtmp = tmp.matcher(s);
            mtmp.find();
            NA = Integer.parseInt(mtmp.group("na"));
            NB = Integer.parseInt(mtmp.group("nb"));

            List<Time> time = new ArrayList<>(); // the list contains all time nodes

            // get the time departure from A and arrival at B
            for (int i = 0; i < NA; i++) {
                String str = in.nextLine();
                Pattern p = Pattern.compile("(?<dhour>[0-9]+):(?<dmin>[0-9]+) (?<ahour>[0-9]+):(?<amin>[0-9]+)");
                Matcher m = p.matcher(str);
                m.find();
                int dhour = Integer.parseInt(m.group("dhour"));
                int dmin = Integer.parseInt(m.group("dmin"));
                int ahour = Integer.parseInt(m.group("ahour"));
                int amin = Integer.parseInt(m.group("amin"));

                time.add(new Time(dhour, dmin, "Ad"));
                time.add(new Time(ahour, amin + T, "Ba"));
            }

            for (int i = 0; i < NB; i++) {
                String str = in.nextLine();
                Pattern p = Pattern.compile("(?<dhour>\\d+):(?<dmin>\\d+) (?<ahour>\\d+):(?<amin>\\d+)");
                Matcher m = p.matcher(str);
                m.find();
                int dhour = Integer.parseInt(m.group("dhour"));
                int dmin = Integer.parseInt(m.group("dmin"));
                int ahour = Integer.parseInt(m.group("ahour"));
                int amin = Integer.parseInt(m.group("amin"));

                time.add(new Time(dhour, dmin, "Bd"));
                time.add(new Time(ahour, amin + T, "Aa"));
            }

            // ascending order 
            time.sort((Time a, Time b) -> {
                // Give priority to arrival time
                if (a.minutes == b.minutes) {
                    if (a.key.equals("Ba") || a.key.equals("Aa")) {
                        return -1;
                    }
                }

                return a.minutes - b.minutes;
                
            });

            for (Time t : time) {
                if (t.key.equals("Aa")) {
                    Ahave++;
                } else if (t.key.equals("Ba")) {
                    Bhave++;
                } else if (t.key.equals("Ad")) {
                    if (Ahave == 0) {
                        Aneed++;
                        Ahave++;
                    }
                    Ahave--;
                } else if (t.key.equals("Bd")) {
                    if (Bhave == 0) {
                        Bneed++;
                        Bhave++;
                    }
                    Bhave--;
                }
            }

            System.out.println("Case #" + (k + 1) + ": " + Aneed + " " + Bneed);

        }
    }

    public static void main(String[] args) {
        solution();
    }

}

class Time {
    int hour; // the HH of  HH:MM
    int min; // the MM of  HH:MM
    int minutes; // the total minutes to this time
    
    /*
     * Ad --> the time departure from A
     * Bd --> the time departure from B
     * Aa --> the time arrive at A
     * Ba --> the time arrive at B
     */
    String key; // Used to mark this time

    /**
     * 
     */
    public Time(int hour, int min, String key) {
        this.hour = hour;
        this.min = min;
        this.key = key;
        minutes = hour * 60 + min;
    }
}
