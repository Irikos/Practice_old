package com.springinaction.knights.impl

import com.springinaction.knights.api.Knight
import com.springinaction.knights.api.Quest

class BraveKnight(quest: Quest) : Knight {


    lateinit private var quest: Quest

    init {
        this.quest = quest
    }


    override fun embarkOnQuest() {
        quest.embark()
    }
}