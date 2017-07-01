package com.springbootinaction.repository

import com.springbootinaction.model.ReaderK
import org.springframework.data.jpa.repository.JpaRepository

interface ReaderRepository : JpaRepository<ReaderK, String> {
}