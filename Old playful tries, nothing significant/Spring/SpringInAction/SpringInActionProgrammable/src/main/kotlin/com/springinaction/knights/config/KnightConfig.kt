package com.springinaction.knights.config

import com.springinaction.knights.api.Knight
import com.springinaction.knights.api.Quest
import com.springinaction.knights.impl.BraveKnight
import com.springinaction.knights.impl.SlayDragonQuest
import org.springframework.context.annotation.Bean
import org.springframework.context.annotation.Configuration

@Configuration
open class KnightConfig {

    @Bean
    open fun knight(): Knight {
        return BraveKnight(quest())
    }

    @Bean
    open fun quest(): Quest {
        return SlayDragonQuest(System.out)
    }
}