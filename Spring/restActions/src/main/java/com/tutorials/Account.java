package com.tutorials;

import com.fasterxml.jackson.annotation.JsonIgnore;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.OneToMany;
import java.util.HashSet;
import java.util.Set;

/**
 * Created by Andrei on 22-Nov-16.
 */
@Entity
public class Account {

    @OneToMany
    private Set<Bookmark> bookmarks = new HashSet<>();

    @Id
    @GeneratedValue
    private long id;

    public Set<Bookmark> getBookmarks() {
        return bookmarks;
    }

    public Long getId() {
        return id;
    }

    public String getPassword() {
        return password;
    }

    public String getUsername() {
        return username;
    }
    @JsonIgnore
    private String password;
    private String username;

    public Account(String name, String password) {
        this.username = name;
        this.password = password;
    }
    Account() {

    }

}
