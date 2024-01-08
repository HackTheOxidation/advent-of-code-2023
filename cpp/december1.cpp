#include <fstream>
#include <iostream>
#include <iterator>
#include <ranges>
#include <string>

constexpr bool is_digit(const char c) {
  return '0' <= c && c <= '9';
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
    sum += get_number(line);
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
