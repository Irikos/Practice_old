package hello.api;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by Andrei on 31-Oct-16.
 */
public interface CustomerList {
    static List<Customer> customerList = new ArrayList();
    static List<Customer> findAll() {
        return customerList;
    }
    static Customer findById(Long id) {
        for (Customer customer: customerList) {
            if (customer.getId() == id)
                return customer;
        }
        return null;
    }
    static void addCustomer(Customer customer) {
        customerList.add(customer);
    }

}
