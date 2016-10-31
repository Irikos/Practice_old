package hello;

import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * Created by Andrei on 31-Oct-16.
 */
@RestController
public class StudentController {

    StudentController() {
        StudentList.addStudent(19, "Vasile", "Cupcea", "vasile.cupcea@gmail.com");
        StudentList.addStudent(22, "Ion", "Cucilic", "ion.cucilic@gmail.com");
        StudentList.addStudent(24, "Cret", "Leustean", "cret.leustean@gmail.com");
        StudentList.addStudent(55, "Bird", "Loboda", "bird.loboda@gmail.com");
    }
    @RequestMapping("/student/{id}")
    public Student student(@PathVariable("id") long id) {
        return StudentList.findById(id);
    }

}
