package hello.impl;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;



/**
 * Created by Andrei on 31-Oct-16.
 */

@Component
class ScheduledMessagesImpl implements hello.api.ScheduledMessages {

    private int times;
    private static final Logger log = LoggerFactory.getLogger(ScheduledMessagesImpl.class);

    ScheduledMessagesImpl() {
        times = 0;
    }

    public int getTimes() {
        return times;
    }


    public void setTimes(int times) {
        this.times = times;
    }

    @Scheduled(fixedRate=5000)
    public void logTimes() {
        int times = getTimes();
        log.info("This code has been run " + times + " times.");
//        System.out.println("This code has been run " + times + " times.");
        setTimes(++times);

    }


}
