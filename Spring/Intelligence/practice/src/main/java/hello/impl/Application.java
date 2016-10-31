package hello.impl;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.scheduling.annotation.EnableScheduling;
import org.springframework.web.client.RestTemplate;

/**
 * Created by Andrei on 28-Oct-16.
 */
@SpringBootApplication
@EnableScheduling
public class Application {


    public static void main(String[] args) throws Exception {



        SpringApplication.run(Application.class, args);

        RestTemplate restTemplate = new RestTemplate();
//        String hello = restTemplate.getForObject("http://localhost:8080/", String.class);
//        System.out.println(hello);
//        Student student = restTemplate.getForObject("http://localhost:8080/student/19", Student.class);
//        Customer customer = restTemplate.getForObject("http://localhost:8080/customer/1", Customer.class);
//        System.out.println(student.getFirstName());
    }
}
