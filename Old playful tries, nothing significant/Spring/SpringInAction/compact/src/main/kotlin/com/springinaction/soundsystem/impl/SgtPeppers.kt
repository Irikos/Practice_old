package com.springinaction.soundsystem.impl

import com.springinaction.soundsystem.api.CompactDisc
import org.springframework.stereotype.Component

@Component
class SgtPeppers: CompactDisc {

    val title: String = "Sgt. Peppers's Lonely Hearts Club Band"
    val artist: String = "The Beatles"

    override fun play() {
        System.out.println("Playing " + title + " by " + artist)
    }
}