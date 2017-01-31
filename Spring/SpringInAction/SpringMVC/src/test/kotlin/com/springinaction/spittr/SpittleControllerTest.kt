package com.springinaction.spittr

import com.springinaction.spittr.data.SpittleRepository
import com.springinaction.spittr.web.SpittleController
import org.hamcrest.Matchers.hasItems
import org.junit.Test
import org.mockito.Mockito.mock
import org.springframework.test.web.servlet.MockMvc
import org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get
import org.springframework.test.web.servlet.result.MockMvcResultMatchers.model
import org.springframework.test.web.servlet.result.MockMvcResultMatchers.view
import org.springframework.test.web.servlet.setup.MockMvcBuilders.standaloneSetup
import org.springframework.web.servlet.view.InternalResourceView
import java.util.*

class SpittleControllerTest {

    @Test
    fun shouldShowRecentSpittles() {

        val expectedSpittles: MutableList<Spittle> = createSpittleList(2)
        val mockRepository: SpittleRepository = mock(SpittleRepository::class.java)

        val controller = SpittleController(mockRepository)

        val mockMvc: MockMvc = standaloneSetup(controller).setSingleView(
                InternalResourceView("/WEB-INF/views/spittles.jsp")).build()

        mockMvc.perform(get("/spittles")).andExpect(view().name("spittles"))
            .andExpect(model().attributeExists("spittleList"))
            .andExpect(model().attribute("spittleList", hasItems(expectedSpittles.toTypedArray())))

//        mockMvc.perform(get("/spittles")).andExpect(view().name("spittles"))
//                .andExpect(model().attributeExists("spittleList"))
//                .andExpect(model().attribute("spittleList",
//                hasItems<Any>(*expectedSpittles.toTypedArray())))
    }

    fun createSpittleList(count: Int): MutableList<Spittle> {

        val spittles: MutableList<Spittle> = ArrayList<Spittle>()

        for (i in 0..count) {
            spittles.add(Spittle("Spittle ", Date()))
        }
        return spittles
    }
}