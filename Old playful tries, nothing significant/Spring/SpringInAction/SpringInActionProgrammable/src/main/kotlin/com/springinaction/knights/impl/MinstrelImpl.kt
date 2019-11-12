package com.springinaction.knights.impl

import com.springinaction.knights.api.Minstrel
import java.io.PrintStream

class MinstrelImpl(stream: PrintStream): Minstrel {

    lateinit var stream: PrintStream

    init {
        this.stream = stream
    }

    override fun singBeforeQuest() {
        stream.println("The knight is going on a quest!")
    }

    override fun singAfterQuest() {
        stream.println("The quest is over!")
    }
}