def factorial(n)
  return 1 if n == 0 || n == 1
  factorial(n-1) * n
end

puts factorial(5)