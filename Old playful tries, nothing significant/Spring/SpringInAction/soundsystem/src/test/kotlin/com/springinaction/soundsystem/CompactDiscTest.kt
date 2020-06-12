package com.springinaction.soundsystem

import com.springinaction.soundsystem.api.CompactDisc
import com.springinaction.soundsystem.api.MediaPlayer
import org.junit.Assert.assertNotNull
import org.junit.Rule
import org.junit.Test
import org.junit.contrib.java.lang.system.SystemOutRule
import org.junit.runner.RunWith
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.test.context.ContextConfiguration
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner

@RunWith(SpringJUnit4ClassRunner::class)
@ContextConfiguration(locations =
    arrayOf("classpath*:/test-config.xml")
)
//@ContextConfiguration(classes =
//    arrayOf(CdPlayerConfig::class)
//)
class SgtPeppersTest {

    @get:Rule
    var systemOutRule  = SystemOutRule().enableLog()

    @Autowired
    lateinit var player: MediaPlayer

    @Autowired
    lateinit var cd: CompactDisc

    @Test
    fun cdShouldNotBeNull() {
        assertNotNull(cd)
        cd.play()
    }

    @Test
    fun play() {
        player.play()
//        assertEquals("Playing Sgt. Peppers's Lonely Hearts Club Band by The Beatles\n",
//                systemOutRule .logWithNormalizedLineSeparator)
    }
}