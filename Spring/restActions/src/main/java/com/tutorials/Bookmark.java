package com.tutorials;

import com.fasterxml.jackson.annotation.JsonIgnore;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.ManyToOne;

/**
 * Created by Andrei on 22-Nov-16.
 */
@Entity
public class Bookmark {

    @JsonIgnore
    @ManyToOne
    private Account account;

    @Id
    @GeneratedValue
    private Long Id;

    Bookmark() {

    }

    public Bookmark(Account account, String uri, String description) {
        this.uri = uri;
        this.description = description;
        this.account = account;
    }

    public String uri;
    public String description;

    public Long getId() {
        return Id;
    }

    public String getUri() {
        return uri;
    }

    public String getDescription() {
        return description;
    }

    public Account getAccount() {
        return account;
    }

}
