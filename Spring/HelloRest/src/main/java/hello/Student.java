package hello;

import java.text.SimpleDateFormat;
import java.util.Date;
import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

@JsonIgnoreProperties(ignoreUnknown = true)
public class Student {
  private int id;
  private int age;
  private String firstName;
  private String lastName;
  private String email;
  private String createdAt;
  private static final SimpleDateFormat dateFormat = new SimpleDateFormat("HH:mm:ss");

  public Student() {

  }
  public Student(int id, int age, String firstName, String lastName, String email) {
    this.id = id;
    this.age = age;
    this.firstName = firstName;
    this.lastName = lastName;
    this.email = email;
    this.createdAt = dateFormat.format(new Date());
  }

  public int getId() {
    return this.id;
  }

  public void setId(int id) {
    this.id = id;
  }

  public int getAge() {
    return this.age;
  }

  public void setAge(int age) {
    this.age = age;
  }

  public String getFirstName() {
    return this.firstName;
  }

  public void setFirstName() {
    this.firstName = firstName;
  }

  public String getLastName() {
    return this.lastName;
  }

  public void setLastName(String lastName) {
    this.lastName = lastName;
  }

  public String getEmail() {
    return this.email;
  }

  public void setEmail(String email) {
    this.email = email;
  }

  public String getCreatedAt() {
    return this.createdAt;
  }

  public void setCreatedAt(String createdAt) {
    this.createdAt = createdAt;
  }

  @Override
  public String toString() {
    return "id: " + id + ", age: " + age + ", firstName: " + firstName + ", lastName: " + lastName + ", email:"
      + email + ", createdAt: " + createdAt;
  }
}
