package com.springinaction.soundsystem

import org.junit.Assert.*

import com.springinaction.soundsystem.impl
import org.junit.Test
import org.junit.runner.RunWith
import org.junit.runners.BlockJUnit4ClassRunner
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.test.context.ContextConfiguration

@RunWith(BlockJUnit4ClassRunner::class)
@ContextConfiguration(classes =
arrayOf(CdPlayerConfig::class)
)
class SgtPeppersTest {

    @Autowired
    lateinit var cd: CompactDisc

    @Test
    fun cdShouldNotBeNull() {
        assertNotNull(cd)
    }
}