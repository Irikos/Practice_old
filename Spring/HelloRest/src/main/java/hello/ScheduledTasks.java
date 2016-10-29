package hello;

import java.text.SimpleDateFormat;
import java.util.Date;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

import org.springframework.web.client.RestTemplate;
import org.springframework.boot.web.client.RestTemplateBuilder;
import org.springframework.context.annotation.Bean;
import org.springframework.boot.CommandLineRunner;


@Component
public class ScheduledTasks {
  private static final Logger log = LoggerFactory.getLogger(ScheduledTasks.class);

  private static final SimpleDateFormat dateFormat = new SimpleDateFormat("HH:mm:ss");

  private static String myDate = new String();

  @Scheduled(fixedRate=5000)
  public void reportCurrentTime() {
    setMyDate();
    log.info("The time is now {}", dateFormat.format(new Date()));

    // RestTemplate restTemplate = new RestTemplate();
    // Quote quote = restTemplate.getForObject("http://gturnquist-quoters.cfapps.io/api/random", Quote.class);
    // log.info(quote.toString());

  }

  @Bean
  public RestTemplate restTemplate(RestTemplateBuilder builder) {
    return builder.build();
  }

  @Bean
  public CommandLineRunner run(RestTemplate restTemplate) throws Exception {
    return args -> {
      Quote quote = restTemplate.getForObject("http://gturnquist-quoters.cfapps.io/api/random", Quote.class);
      log.info(quote.toString());
    };
  }

  private static void setMyDate() {
    myDate = dateFormat.format(new Date());
  }
  public String getDate() {
    return myDate;
  }
}
