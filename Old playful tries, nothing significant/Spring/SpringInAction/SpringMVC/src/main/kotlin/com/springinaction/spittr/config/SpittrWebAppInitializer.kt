package com.springinaction.spittr.config

import com.springinaction.spittr.config.WebConfig
import org.springframework.stereotype.Component
import org.springframework.web.servlet.support.AbstractAnnotationConfigDispatcherServletInitializer

@Component
class SpittrWebAppInitializer: AbstractAnnotationConfigDispatcherServletInitializer() {

    override fun getServletMappings(): Array<String> {
        return arrayOf( "/" )
    }

    override fun getRootConfigClasses(): Array<Class<*>> {
        return  arrayOf( RootConfig::class.java )
    }

    override fun getServletConfigClasses(): Array<Class<*>> {
        return arrayOf( WebConfig::class.java )
    }

}