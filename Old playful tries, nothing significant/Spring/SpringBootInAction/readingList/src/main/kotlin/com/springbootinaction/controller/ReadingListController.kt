package com.springbootinaction.controller

import com.springbootinaction.AmazonProperties
import com.springbootinaction.model.Book
import com.springbootinaction.repository.ReadingListRepository
import org.springframework.stereotype.Controller
import org.springframework.ui.Model
import org.springframework.web.bind.annotation.GetMapping
import org.springframework.web.bind.annotation.PathVariable
import org.springframework.web.bind.annotation.PostMapping
import org.springframework.web.bind.annotation.RequestMapping

@Controller
@RequestMapping("/")
open class ReadingListController(private val readingListRepository: ReadingListRepository, private val amazonProperties: AmazonProperties) {

    @GetMapping("/{reader}")
    fun readersBook(@PathVariable("reader") reader: String, model: Model): String {

        val readingList = readingListRepository.findByReader(reader)

        if (readingList.isNotEmpty()) {
            model.addAttribute("books", readingList)
            model.addAttribute("reader", reader)
            model.addAttribute("amazonID", amazonProperties.getAssociateId())
        }
        return "readingList"
    }

    @PostMapping(value="{reader}")
    fun addToReadingList(@PathVariable("reader") reader: String, book: Book): String {

        book.reader = reader
        readingListRepository.save(book)
        return "redirect:/"
    }
}