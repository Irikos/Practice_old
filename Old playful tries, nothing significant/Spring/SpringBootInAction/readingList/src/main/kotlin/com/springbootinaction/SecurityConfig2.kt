//package com.springbootinaction
//
//import com.springbootinaction.repository.ReaderRepository
//import org.springframework.context.annotation.Configuration
//import org.springframework.security.config.annotation.authentication.builders.AuthenticationManagerBuilder
//import org.springframework.security.config.annotation.web.builders.HttpSecurity
//import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity
//import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter
//import org.springframework.security.core.userdetails.UserDetails
//import org.springframework.security.core.userdetails.UserDetailsService
//import org.springframework.security.core.userdetails.UsernameNotFoundException
//
//
//@Configuration
//@EnableWebSecurity
//class SecurityConfig2(private var readerRepository: ReaderRepository) : WebSecurityConfigurerAdapter() {
//
//
//    @Throws(Exception::class)
//    override fun configure(http: HttpSecurity) {
//        http
//            .authorizeRequests().antMatchers("/").access("hasRole('READER')").antMatchers("/**").permitAll()
//            .and()
//            .formLogin().loginPage("/login").failureUrl("/login?error=true")
//    }
//
//    @Throws(Exception::class)
//    override fun configure(auth: AuthenticationManagerBuilder) {
//
//        val userDetailService = UserDetailsService {
//            @Throws(UsernameNotFoundException::class)
//            fun loadUserByUsername(username: String) {
//                return readerRepository.findOne
//            }
//        }
//
//        auth.userDetailsService(userDetailService)
//
//    }
//}