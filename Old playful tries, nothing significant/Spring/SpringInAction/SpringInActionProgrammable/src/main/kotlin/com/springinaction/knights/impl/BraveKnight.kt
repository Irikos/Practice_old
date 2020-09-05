package com.springinaction.knights.impl

import com.springinaction.knights.api.Knight
import com.springinaction.knights.api.Quest

class BraveKnight(quest: Quest): Knight {

    private lateinit var quest: Quest
    init {
        this.quest = quest
    }

    override fun embarkOnQuest() {
        quest.embark()
    }
}