package com.springbootinaction

import org.springframework.boot.SpringApplication
import org.springframework.boot.autoconfigure.SpringBootApplication

@SpringBootApplication
open class ReadingListApplication

fun main(args: Array<String>) {
    SpringApplication.run(ReadingListApplication::class.java, *args)
}
