# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

def isPrime(n)
  for i in 2..Math.sqrt(n)
    if (n % i == 0)
      return false;
    end
  end
  return true
end

max = 0;
number = 600851475143
for i in 2..Math.sqrt(number)
  if (number % i == 0 && isPrime(i))
    max = i;
  end
end

puts max;
