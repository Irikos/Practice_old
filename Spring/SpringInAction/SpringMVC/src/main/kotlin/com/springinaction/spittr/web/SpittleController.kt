package com.springinaction.spittr.web

import com.springinaction.spittr.Spittle
import org.springframework.stereotype.Controller
import org.springframework.ui.Model
import org.springframework.web.bind.annotation.GetMapping
import org.springframework.web.bind.annotation.RequestMapping

@Controller
@RequestMapping("/spittles")
class SpittleController() {

    @GetMapping
    fun spittles(model: Model): List<Spittle> {
        return listOf()
//        return spittleRepository.findSpittles(Long.MAX_VALUE, 20)
//        model.addAttribute("spittleList",
//                spittleRepository.findSpittles(Long.MAX_VALUE, 20)
//        )
//        return "spittles"
    }

}