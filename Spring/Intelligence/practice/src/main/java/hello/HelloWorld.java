package hello;


import java.text.SimpleDateFormat;
import java.util.Calendar;

/**
 * Created by Andrei on 28-Oct-16.
 */
public class HelloWorld {
    public static void main(String[] args) {

        Calendar calendar = Calendar.getInstance();

        String time = new SimpleDateFormat("dd.MM.yyyy HH:mm:ss").format(calendar.getTime());
        Greeter greeter = new Greeter();
        System.out.println(greeter.sayHello());
        System.out.println("The local date and time is: " + time);
    }
}
