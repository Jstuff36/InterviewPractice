#!/usr/bin/env ruby

class RPNCalculator

  def self.command_line_interface
    #debugger
    command = ""

    while true
      puts "Enter an operation or number. Press enter to exit"
      input = gets.chomp
      break if input == ""
      command << " #{input}"
    end

    RPNCalculator.new.evaluate(command)

  end



  def initialize
    @calculations = []
  end


  def self.run_file(file)
    contents = File.readlines(file)
    line_results = []
    this_calc = RPNCalculator.new #this_calc is an instance variable
    contents.each do |i|
      line_results << this_calc.evaluate(i)
    end
    line_results
  end

  def push(num)
    @calculations << num
  end

  def plus
    calcs(:+)
  end

  def minus
    calcs(:-)
  end

  def divide
    calcs(:/)
  end

  def times
    calcs(:*)
  end

  def calcs(operation)

    #raise "calculator is empty" if @calculations.length < 2
    until @calculations.length < 2
      first = @calculations.pop.to_f
      second = @calculations.pop.to_f

      case operation
      when :+
        @calculations << first + second
      when :-
        @calculations << second - first
      when :/
        @calculations << second / first
      when :*
        @calculations << second * first
      end
    end

  end

  def value
    @calculations.last
  end


  def evaluate(string)
    string_to_operations = tokens(string)
    string_to_operations.each do |i|
      if i.is_a? Symbol
        calcs(i)
      else
        push(i)
      end
    end
    value
  end

  def tokens(string)
    operations = [:+, :-, :/, :*]
    string_mod = string.split(" ")
    string_converted = []
    string_mod.each do |j|
      if operations.include? j.to_sym
        string_converted << j.to_sym
      else
        string_converted << j.to_i
      end
    end
    string_converted
  end

end

puts RPNCalculator.command_line_interface

#if __FILE__ == $PROGRAM_NAME
#  if ARGV.empty?
#    #doesn't properaly handle 3 numbers in a row only performs execution on last 2
#    puts RPNCalculator.command_line_interface
#  else
#    puts RPNCalculator.run_file(ARGV[0])
#  end
#end