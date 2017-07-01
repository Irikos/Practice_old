package com.springinaction.soundsystem

import org.springframework.context.annotation.Import


@Import(
        CdPlayerConfig::class
)
open class main()

fun main(args: Array<String>) {
}