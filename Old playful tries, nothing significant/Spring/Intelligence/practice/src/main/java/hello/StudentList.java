package hello;

import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by Andrei on 31-Oct-16.
 */
@RestController
public class StudentList {
    private static List<Student> students = new ArrayList<>();



    public static Student addStudent(Student student) {
        students.add(student);
        return student;
    }

    public static Student addStudent(long id, String firstName, String lastName, String email) {
        Student student = new Student(id, firstName, lastName, email);
        students.add(student);
        return student;
    }

    public static Student addStudent(String firstName, String lastName, String email) {
        Student student = new Student(firstName, lastName, email);
        students.add(student);
        return student;
    }

    public List<Student> findAll() {
        return students;
    }

    public static Student findById(long id) {
        for (Student student: students) {
            if (student.getId() == id)
                return student;
        }
        return null;
    }
}
