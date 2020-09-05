package com.springinaction.knights

import com.springinaction.knights.api.Knight
import com.springinaction.knights.config.KnightConfig
import org.springframework.context.ApplicationContext
import org.springframework.context.annotation.AnnotationConfigApplicationContext


open class KnightsMain

fun main(args: Array<String>) {

    val context: ApplicationContext = AnnotationConfigApplicationContext(KnightConfig::class.java)
    val knight = context.getBean(Knight::class.java)
    knight.embarkOnQuest()
}