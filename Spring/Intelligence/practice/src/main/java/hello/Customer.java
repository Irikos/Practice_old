package hello;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

/**
 * Created by Andrei on 03-Nov-16.
 */
@JsonIgnoreProperties(ignoreUnknown = true)
public class Customer {
    private long id;
    private String firstName, lastName;

    public Customer(long id, String firstName, String lastName) {
        this.id = id;
        this.firstName = firstName;
        this.lastName = lastName;
    }
    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public String toString() {
        return String.format("Customer[id = %d, firstName = '%s', lastString = '%s']", id, firstName, lastName);
    }
}
