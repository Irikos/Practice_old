package hello.impl;

import java.util.List;

/**
 * Created by Andrei on 31-Oct-16.
 */
public class CustomerListImpl {
    private static List<CustomerImpl> customerList;

    public CustomerImpl findById(Long id) {
        for (CustomerImpl customer: customerList) {
            if (customer.getId() == id)
                return customer;
        }
        return null;
    }

    public List<CustomerImpl> findAll() {
        return customerList;
    }


    static void addCustomer(long id, String firstName, String lastName) {
        CustomerImpl customer = new CustomerImpl(id, firstName, lastName);
        customerList.add(customer);
    }
}
