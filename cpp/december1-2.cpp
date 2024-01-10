#include <fstream>
#include <iostream>
#include <ranges>
#include <regex>
#include <string>
#include <string_view>
#include <unordered_map>

const static std::regex numbers_as_words(
    "one|two|three|four|five|six|seven|eight|nine",
    std::regex_constants::icase);

const static std::unordered_map<std::string_view, std::string_view> word_to_number_map = {
  {"one", "1"},
  {"two", "2"},
  {"three", "3"},
  {"four", "4"},
  {"five", "5"},
  {"six", "6"},
  {"seven", "7"},
  {"eight", "8"},
  {"nine", "9"}
};

constexpr bool is_digit(const char c) {
  return '0' <= c && c <= '9';
}

std::string numerize_line(std::string line) {
  std::smatch result;
  std::regex_match(line, result, numbers_as_words);

  if (!result.empty()){
    auto replacement = word_to_number_map.at(result.str()).data();
    return numerize_line(std::regex_replace(line, numbers_as_words, replacement, std::regex_constants::format_first_only));
  }   

  return line;
}

std::size_t get_number(const std::string line) {
  std::string number;
  auto digits = std::views::filter(line, is_digit);
  number += *digits.begin();
  number += *(std::views::reverse(digits)).begin();

  if (number.empty())
    return 0;

  return std::stoull(number);
}

void read_sum(const std::string filename) {
  std::ifstream istrm(filename);

  if (!istrm.is_open()) {
    std::cout << ("File: " + filename + " does not exist.");
    return;
  } 

  std::string line;
  std::size_t sum = 0;
  while (std::getline(istrm, line)) {
    sum += get_number(numerize_line(line));
  }

  std::cout << sum << '\n';
}


auto main(int argc, char **argv) -> int {
  if (argc == 2) {
    read_sum(std::string(argv[1]));

    return 0;
  } else if (argc < 2) {
    std::string filename;
    std::cout << "Enter name of input file: ";
    std::cin >> filename;
    read_sum(filename);

    return -1;
  } else {
    std::string error_message = "Too many argument(s) - expected (1): <inputfile>, got: ";
    for (auto i = 0; i < argc; i++) {
      error_message += std::string(argv[i]) + " ";
    }

    std::cout << error_message << '\n';
    return 1;
  }
}
