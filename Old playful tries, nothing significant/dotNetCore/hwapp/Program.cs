using System;

namespace hwapp
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            Console.WriteLine("Getting started with .net core...");
            Hello hello = new Hello();
            Hello alternativeHello = new Hello();
            hello.helloWorld();
            Console.WriteLine("This class has been instantiated " + Hello.getCount() + " times");
        }
    }
}
