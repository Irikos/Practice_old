package com.springinaction.spittr

import com.springinaction.spittr.web.HomeController
import org.junit.Assert.assertEquals
import org.junit.Test
import org.springframework.test.web.servlet.MockMvc
import org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get
import org.springframework.test.web.servlet.result.MockMvcResultMatchers.view
import org.springframework.test.web.servlet.setup.MockMvcBuilders.standaloneSetup

open class HomeControllerTest {

    @Test
    fun testHomePage() {
        val controller = HomeController()
        val mockMvc: MockMvc = standaloneSetup(controller).build()

        mockMvc.perform(get("/")).andExpect(view().name("home"))
        assertEquals("home", controller.home())
    }

}
