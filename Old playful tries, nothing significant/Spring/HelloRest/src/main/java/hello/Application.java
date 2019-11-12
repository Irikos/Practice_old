package hello;

//Hello Rest
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

//ScheduleTasks
import org.springframework.scheduling.annotation.EnableScheduling;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.web.client.RestTemplate;

@SpringBootApplication
@EnableScheduling
public class Application {

  private static final Logger log = LoggerFactory.getLogger(Application.class);

  public static void main(String[] args) throws Exception {
    SpringApplication.run(Application.class, args);

    RestTemplate restTemplate = new RestTemplate();
    int i = 1;
    Student student = restTemplate.getForObject("http://localhost:8080/students/" + i, Student.class);
    while(student != null) {
      log.info(student.toString());
      i++;
      student = restTemplate.getForObject("http://localhost:8080/students/" + i, Student.class);
    }
  }
}
