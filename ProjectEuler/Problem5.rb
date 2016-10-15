# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

x = false
i = 1
start = Time.now
while (x == false)
  x = true
  for j in 1..20
    if (i % j != 0)
      x = false
    end
  end

  if x == true
    puts i
  end
  if i % 2432902008176640000 == 0
    puts i
  end
  if i == 1
    puts "de la capat"
  end
  i += 1
end
finish = Time.now

dif = finish - star
#
# 2432902008176640000.0
