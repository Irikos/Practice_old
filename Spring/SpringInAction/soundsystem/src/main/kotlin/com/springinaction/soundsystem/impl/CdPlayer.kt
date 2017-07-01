package com.springinaction.soundsystem.impl

import com.springinaction.soundsystem.api.CompactDisc
import com.springinaction.soundsystem.api.MediaPlayer
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.stereotype.Component

@Component
class CdPlayer: MediaPlayer {

    lateinit var cd: CompactDisc

    @Autowired
    constructor(cd: CompactDisc) {
        this.cd = cd
    }

    @Autowired
    fun setCompactDisc(cd: CompactDisc) {
        this.cd = cd
    }

    // if there are no matching beans, it won't throw an exception. Not the best idea
    @Autowired
    fun insertDisc(cd: CompactDisc) {
        this.cd = cd
    }

    override fun play() {
        cd.play()
    }
}