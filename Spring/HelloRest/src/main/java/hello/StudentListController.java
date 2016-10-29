package hello;

import java.util.List;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.PathVariable;

@RestController
public class StudentListController {

  // Student vasile = new Student(1, 19, "Vasile", "Cupcea", "vasile.cupcea@gmail.com");
  private StudentList students = new StudentList();
  public StudentListController() {

    students.addStudent(19, "Vasile", "Cupcea", "vasile.cupcea@gmail.com");
    students.addStudent(22, "Ion", "Cucilic", "ion.cucilic@gmail.com");
    students.addStudent(24, "Cret", "Leustean", "cret.leustean@gmail.com");
    students.addStudent(55, "Bird", "Loboda", "bird.loboda@gmail.com");
  }

  // @RequestMapping("/students/{id}")
  // public Student students(@PathVariable("id") int id) {
  //   students.addStudent(new Student(id, ));
  // }
  @RequestMapping("/students/{id}")
  public Student students(@PathVariable("id") int id) {
    return students.findById(id);
  }

  @RequestMapping("/students/add/{id}")
  public Student students(@PathVariable("id") int id, @RequestParam(value="age") int age, @RequestParam(value="firstName") String firstName, @RequestParam(value="lastName") String lastName, @RequestParam(value="email") String email) {
    students.addStudent(id, age, firstName, lastName, email);

    return students.findById(id);
  }

  @RequestMapping("/students")
  public List<Student> getAllStudents() {
    return students.getAllStudents();
  }
}
