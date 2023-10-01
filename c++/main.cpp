#include <iostream>
#include <fstream>
#include <regex>
#include <string>
#include <vector>

void iterateCodepoints(const std::string& pattern, const std::string& filePath) {
    std::ofstream file(filePath);
    if (!file.is_open()) {
        std::cerr << "Could not open file: " << filePath << std::endl;
        return;
    }

    std::wregex regex(pattern.begin(), pattern.end(), std::regex::extended);
    for (int i = 0; i <= 0x10ffff; ++i) {
        // if (0xd800 <= i && i <= 0xdfff) {
        //     continue;
        // }
        wchar_t wc = static_cast<wchar_t>(i);
        if (std::regex_match(&wc, &wc + 1, regex)) {
            file << std::hex << std::uppercase << i << std::endl;
        }
    }
}

int main(int argc, char* argv[]) {
    if (argc < 3) {
        std::cerr << "Usage: ./main <pattern> <file_path>" << std::endl;
        return 1;
    }

    std::string pattern = argv[1];
    std::string filePath = argv[2];

    iterateCodepoints(pattern, filePath);

    return 0;
}