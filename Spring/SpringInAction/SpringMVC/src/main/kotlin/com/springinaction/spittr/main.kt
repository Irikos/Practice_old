package com.springinaction.spittr

import com.springinaction.spittr.config.RootConfig
import org.springframework.context.ApplicationContext
import org.springframework.context.annotation.AnnotationConfigApplicationContext
import org.springframework.context.annotation.Import

@Import()
open class main()

fun main(args: Array<String>) {
    val context: ApplicationContext = AnnotationConfigApplicationContext(RootConfig::class.java)
}