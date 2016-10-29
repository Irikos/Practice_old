package hello;

import org.springframework.beans.factory.annotation.Autowired;

/**
 * Created by Andrei on 28-Oct-16.
 */
public class MessagePrinter {

    final private MessageService service;

    @Autowired
    public MessagePrinter(MessageService service) {
        this.service = service;
    }

    public void printMessage() {
        System.out.println(this.service.getMessage());
    }
}
