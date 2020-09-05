using System;

namespace hwapp {

  class Hello {
    static int count = 0;

    public Hello() {
      count++;
    }
    public void helloWorld() {
      Console.WriteLine("Hello, World!");
    }
    public static int getCount() {
      return count;
    }
  }
}
