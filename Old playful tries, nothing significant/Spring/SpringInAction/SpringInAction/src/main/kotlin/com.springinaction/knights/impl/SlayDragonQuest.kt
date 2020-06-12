package com.springinaction.knights.impl

import com.springinaction.knights.api.Quest
import java.io.PrintStream

class SlayDragonQuest(stream: PrintStream): Quest {

    lateinit private var stream: PrintStream

    init {
        this.stream = stream
    }

    override fun embark() {
        stream.println("Embarking on a quest to slay the dragon!")
    }

}