package com.springinaction.soundsystem.impl

import com.springinaction.soundsystem.api.CompactDisc
import org.springframework.beans.factory.annotation.Autowired

class BlankDisc: CompactDisc {

    lateinit var title: String
    lateinit var artist: String
    lateinit var tracks: List<String>

    constructor(title: String, artist: String, tracks: List<String>) {
        this.title = title
        this.artist = artist
        this.tracks = tracks
    }

    override fun play() {
        println("Playing $title by $artist")
        tracks.map {
            println(" - Track: $it")
        }
    }
}