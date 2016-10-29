package hello;

import java.util.List;
import java.util.ArrayList;

public class StudentList {
  private List<Student> studentList = new ArrayList<Student>();
  private static int id = 1;

  public void addStudent(int age, String firstName, String lastName, String email) {
    Student student = new Student(id++, age, firstName, lastName, email);
    studentList.add(student);
  }

  public void addStudent(int id, int age, String firstName, String lastName, String email) {
    Student student = new Student(id, age, firstName, lastName, email);
    studentList.add(student);
  }

  public void addStudent(Student student) {
    studentList.add(student);
  }

  public Student findById(int id) {
    for (Student student: studentList) {
      if (student.getId() == id)
        return student;
    }
    return null;
  }

  public List<Student> getAllStudents() {
    return this.studentList;
  }
}
