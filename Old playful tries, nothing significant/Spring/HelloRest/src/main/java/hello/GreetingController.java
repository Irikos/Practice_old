package hello;

import java.util.concurrent.atomic.AtomicLong;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;



import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

@RestController
public class GreetingController {
  private static final String template = "Hello, %s!";
  private final AtomicLong counter = new AtomicLong();
  private static int seconds = 10;
  private ScheduledTasks scheduledTask = new ScheduledTasks();
  private static final Logger log = LoggerFactory.getLogger(ScheduledTasks.class);


  @RequestMapping("/greeting")
  public Greeting greeting(@RequestParam(value="name", defaultValue="World") String name) {
    return new Greeting(counter.incrementAndGet(), String.format(template, name), seconds, scheduledTask.getDate());
  }

  @RequestMapping("/test")
  public Greeting test() {
    log.info("The time is now {}", scheduledTask.getDate());
    return new Greeting(0, "test", seconds, "dateTest");
  }

}
