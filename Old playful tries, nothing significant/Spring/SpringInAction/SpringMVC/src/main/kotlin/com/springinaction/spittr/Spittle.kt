package com.springinaction.spittr

import org.apache.commons.lang3.builder.EqualsBuilder
import org.apache.commons.lang3.builder.HashCodeBuilder
import java.util.*

class Spittle(message: String, time: Date, longitude: Double?, latitude: Double?) {

    private val id: Long?
    private val message: String?
    private val time: Date?
    private var latitude: Double?
    private var longitude: Double?

    init {
        this.id = null
        this.message = message
        this.time = time
        this.latitude = latitude
        this.longitude = longitude

    }

    constructor(message: String, time: Date): this(message, time, null, null)

    override fun equals(other: Any?): Boolean {
        return EqualsBuilder.reflectionEquals(this, other, "id", "time")
    }

    override fun hashCode(): Int {
        return HashCodeBuilder.reflectionHashCode(this, "id", "time")
    }


}