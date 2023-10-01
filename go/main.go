package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"unicode/utf8"
)

func iterateCodepoints(pattern string, filePath string) error {
	file, err := os.Create(filePath)
	if err != nil {
		return err
	}
	defer file.Close()

	writer := bufio.NewWriter(file)
	regex, err := regexp.Compile(pattern)
	if err != nil {
		return err
	}

	for i := 0; i <= 0x10ffff; i++ {
		// if 0xd800 <= i && i <= 0xdfff {
		// 	continue
		// }
		char := string(rune(i))
		if !utf8.ValidString(char) {
			continue
		}
		if regex.MatchString(char) {
			writer.WriteString(fmt.Sprintf("%04X\n", i))
		}
	}
	writer.Flush()
	return nil
}

func main() {
	if len(os.Args) < 3 {
		fmt.Println("Usage: go run main.go <pattern> <file_path>")
		return
	}
	pattern := os.Args[1]
	filePath := os.Args[2]
	err := iterateCodepoints(pattern, filePath)
	if err != nil {
		fmt.Println("Error:", err)
	}
}
