package com.springbootinaction

import org.springframework.boot.context.properties.ConfigurationProperties
import org.springframework.stereotype.Component

@Component
@ConfigurationProperties(prefix="amazon")
open class AmazonProperties {

    lateinit private var associateId: String

    open fun getAssociateId(): String {
        return associateId
    }

    open fun setAssociateId(associateId: String) {
        this.associateId = associateId
    }

}