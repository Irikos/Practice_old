package com.springbootinaction.model

import java.io.Serializable
import javax.persistence.Entity
import javax.persistence.GeneratedValue
import javax.persistence.Id

@Entity
open class Book(

    @Id
    @GeneratedValue
    val id: Long? = null,

    var reader: String? = null,

    var isbn: String? = null,

    var title: String? = null,

    var author: String? = null,

    var description: String? = null

) :Serializable