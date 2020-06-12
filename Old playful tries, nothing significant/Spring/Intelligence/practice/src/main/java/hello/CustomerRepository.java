package hello;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by Andrei on 03-Nov-16.
 */
@RestController
public class CustomerRepository {

    private static final Logger log = LoggerFactory.getLogger(Application.class);

    @Autowired
    JdbcTemplate jdbcTemplate;

    @GetMapping("/customer/{id}")
    public List<Customer> getCustomerById(@PathVariable("id") Long id) {
        List<Customer> customerList = new ArrayList<Customer>();

        log.info("Querying customer with id " + id);
        jdbcTemplate.query(
                "SELECT id, first_name, last_name FROM customers WHERE id = ?", new Object[] { id },
                (rs, rowNum) -> new Customer(rs.getLong("id"), rs.getString("first_name"), rs.getString("last_name"))
        ).forEach(customer -> {
            log.info(customer.toString());
            customerList.add(customer);
        });

        return customerList;
    }
}
