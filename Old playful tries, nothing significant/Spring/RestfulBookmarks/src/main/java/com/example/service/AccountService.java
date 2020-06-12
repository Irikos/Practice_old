package com.example.service;

import com.example.model.Account;

import java.util.List;
import java.util.Optional;

public interface AccountService {

    List<Account> findAll();
    Account findById(Long id);
    Optional<Account> findByUsername(String username);
}
