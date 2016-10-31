package hello.impl;
/**
 * Created by Andrei on 28-Oct-16.
 */

public class CustomerImpl implements hello.api.Customer {
    private long id;
    private String firstName, lastName;

    public CustomerImpl(long id, String firstName, String lastName) {
        this.id = id;
        this.firstName = firstName;
        this.lastName = lastName;
    }

    CustomerImpl() {}

    public long getId() {
        return this.id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getFirstName() {
        return this.firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String getLastName() {
        return this.lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    @Override
    public String toString() {
        return "id: " + id + ", firstName: " + firstName + ", lastName: " + lastName;
    }
}
