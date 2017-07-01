package com.springbootinaction.model

import org.springframework.security.core.GrantedAuthority
import org.springframework.security.core.authority.SimpleGrantedAuthority
import org.springframework.security.core.userdetails.UserDetails
import java.util.*
import javax.persistence.Entity
import javax.persistence.Id

@Entity
open class ReaderK(
        @Id
        private val username: String? = null,
        private val fullname: String? = null,
        private val password: String? = null
) : UserDetails {
    override fun isEnabled(): Boolean {
        return true
    }

    override fun getAuthorities(): MutableCollection<out GrantedAuthority> {
        return Arrays.asList(SimpleGrantedAuthority("READER"))
    }

    override fun isAccountNonLocked(): Boolean {
        return true
    }

    override fun isAccountNonExpired(): Boolean {
        return true
    }

    override fun isCredentialsNonExpired(): Boolean {
        return true
    }

    override fun getUsername() = username
    override fun getPassword() = password

}