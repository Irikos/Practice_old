package hello.impl;

import hello.api.CustomerList;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

/**
 * Created by Andrei on 31-Oct-16.
 */
@RestController
class CustomerControllerImpl implements hello.api.CustomerController {

    CustomerControllerImpl() {
        CustomerImpl customer = new CustomerImpl(1, "Andrei", "Bardezi");
    }
    @RequestMapping("/customer/id")
    public CustomerImpl getCustomberById(Long id) {
        CustomerImpl customer = (CustomerImpl) CustomerList.findById(id);
        return customer;
    }

    @RequestMapping("/customer/add/{id}")
    public void addCustomer(@PathVariable("id") long id, @RequestParam(value="firstName")String firstName, @RequestParam(value="lastName")String lastName) {
        CustomerImpl customer = new CustomerImpl(id, firstName, lastName);
        CustomerList.addCustomer(customer);
    }
}
