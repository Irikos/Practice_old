package com.springinaction.spittr.config

import org.springframework.context.annotation.ComponentScan
import org.springframework.context.annotation.ComponentScan.Filter
import org.springframework.context.annotation.Configuration
import org.springframework.context.annotation.FilterType
import org.springframework.web.servlet.config.annotation.EnableWebMvc


@Configuration
@ComponentScan(
        basePackages = arrayOf("com.springinaction.spittr"),
        excludeFilters = arrayOf(Filter(type=FilterType.ANNOTATION, value=EnableWebMvc::class))
        )
open class RootConfig {
}