package com.springinaction.spittr.data

import com.springinaction.spittr.Spittle

interface SpittleRepository {

    fun findSpittles(max: Long, count: Int): List<Spittle>
}