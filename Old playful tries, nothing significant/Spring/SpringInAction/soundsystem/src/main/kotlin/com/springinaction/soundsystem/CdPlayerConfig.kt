package com.springinaction.soundsystem

import com.springinaction.soundsystem.api.CompactDisc
import com.springinaction.soundsystem.api.MediaPlayer
import com.springinaction.soundsystem.impl.CdPlayer
import com.springinaction.soundsystem.impl.SgtPeppers
import org.springframework.context.annotation.Bean
import org.springframework.context.annotation.Configuration

@Configuration
//@ImportResource("classpath*:/resources/configuration.xml")
open class CdPlayerConfig {

    @Bean
    open fun sgtPeppers(): CompactDisc {
        return SgtPeppers()
    }

    @Bean
    open fun cdPlayer(compactDisc: CompactDisc): MediaPlayer {
        return CdPlayer(compactDisc)
    }
}