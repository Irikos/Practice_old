package hello;


import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.PathVariable;

@RestController
public class StudentController {

  // Student vasile = new Student(1, 19, "Vasile", "Cupcea", "vasile.cupcea@gmail.com");

  @RequestMapping("/student/{id}")
  public Student student(@PathVariable("id") int id) {
    return new Student(id, 19, "Vasile", "Cupcea", "vasile.cupcea@gmail.com");
  }
}
