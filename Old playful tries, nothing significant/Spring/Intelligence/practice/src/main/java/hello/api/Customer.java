package hello.api;

/**
 * Created by Andrei on 31-Oct-16.
 */
public interface Customer {

    long getId();

    void setId(Long id);

    String getFirstName();

    void setFirstName(String firstName);

    String getLastName();

    void setLastName(String lastName);

    String toString();


}
