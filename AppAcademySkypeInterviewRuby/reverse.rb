def reverse(str)
  str_reversed = []
  split_str = str.split("")
  counter = split_str.length
  while counter >= 0
    str_reversed << split_str[counter]
    counter -= 1
  end
  str_reversed.join("")
end

puts reverse("dolly")