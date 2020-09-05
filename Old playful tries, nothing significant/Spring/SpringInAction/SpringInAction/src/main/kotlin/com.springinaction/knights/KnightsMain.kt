package com.springinaction.knights

import com.springinaction.knights.api.Knight
import org.springframework.context.support.ClassPathXmlApplicationContext

open class KnightsMain

fun main(args: Array<String>) {
    val context = ClassPathXmlApplicationContext("/META-INF/spring/knight.xml")
    val knight: Knight = context.getBean(Knight::class.java)
    knight.embarkOnQuest()
    context.close()
}