# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome(n)
  return n.to_s.split('').reverse == n.to_s.split('')
end


def largestPalindrome(n1, n2)
  max = 0;
  for i in n1..999
    for j in n2..999
      if isPalindrome(i * j) && (i * j) > max
        max = i * j;
      end
    end
  end
  return max;
end

puts largestPalindrome(900, 900)
