package hello;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

/**
 * Created by Andrei on 31-Oct-16.
 */
@JsonIgnoreProperties(ignoreUnknown = true)
class Student {
    private static long counter = 0;
    private long id;
    private String firstName, lastName, email;

    Student(long id, String firstName, String lastName, String email) {
        this.id = id;
        this.firstName = firstName;
        this.lastName = lastName;
        this.email = email;
        StudentList.addStudent(this);
    }
    Student(String firstName, String lastName, String email) {
        this.id = counter++;
        this.firstName = firstName;
        this.lastName = lastName;
        this.email = email;
        StudentList.addStudent(this);
    }

    public long getId() {
        return this.id;
    }

    public void setId(long id) {
        this.id = id;
    }

    public String getFirstName() {
        return this.firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public String getLastName() {
        return this.lastName;
    }
}
