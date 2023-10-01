require 'fileutils'

def iterate_codepoints(pattern, file_path)
  begin
    file = File.open(file_path, mode = 'w')
    regex = Regexp.new(pattern)
    (0..0x10ffff).each do |i|
      # if 0xd800 <= i && i <= 0xdfff
      #   next
      # end
      char = [i].pack('U')
      if char.valid_encoding? && regex.match?(char)
        file.puts(sprintf('%04X', i))
      end
    end
  rescue => e
    puts "Error: #{e}"
  ensure
    file.close unless file.nil?
  end
end

if ARGV.length < 2
  puts "Usage: ruby main.rb <pattern> <file_path>"
else
  pattern = ARGV[0]
  file_path = ARGV[1]
  iterate_codepoints(pattern, file_path)
end
