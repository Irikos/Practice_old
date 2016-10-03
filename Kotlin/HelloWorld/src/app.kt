/**
 * Created by Andrei on 10/3/2016.
 */

import kotlin.*

var testString: String = "test"

fun main(args: Array<String>) {
    println("Hello, world!")
    println(sum(2,3))
    println(sumLine(4,5))
    println(testString)

    if (args.size > 0) {
        for (arg in args) {
            println("the argument is: ${arg}")
        }
    }
    max(2, 3)
    max(5, 4)
    max(1, 1)
    println(parseInt("42"))
    println(isString("yes"))
    println(isString(4))

    cases(1)
}

fun sum(a: Int, b: Int) : Int {
    return a + b

}

fun sumLine (a: Int, b: Int) = a + b

fun max (a: Int, b: Int) : Int {
    if (a > b) {
        println("$a e mai mare")
        return a
    }
    else
        if(b > a) {
            println("$a e mai mare")
            return b
        }
        else {
            println("sunt egale")
            return 0
        }
}

fun parseInt(str: String) : Int? {
    println("test nullable")
    return 0
}

fun isString(obj: Any) : Int? {
    if (obj is String) {
        return obj.length
    }

    return null
}

fun cases(obj: Any) {
    var a = obj;
    when (a) {
        1 -> {
            print("a is $a")
            if (a is Int)
                a++
        }
        2 -> {
            print("a is $a")
            if (a is Int)
                a++
        }
        3 -> {
            print("a is $a")
            if (a is Int)
                a++
        }
        4 -> {
            print("a is $a")
            if (a is Int)
                a++
        }
        5 -> {
            print("a is $a")
            if (a is Int)
                a++
        }
        6 -> {
            print("a is $a")
            if (a is Int)
                a++
        }
    }
}