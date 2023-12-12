#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>
#include <map>

static std::map<std::pair<std::string, std::vector<int64_t>>, int64_t> TABLE; 

int64_t find(char* str, int64_t s, char c) {
  for (int64_t i = 0; i < s; ++i)
    if (c == str[i]) return i;
  return -1;
}

int64_t solve_recursive(char* arrangement, int64_t ss, const int64_t* expect, int64_t es) {
  if (ss == 0) {
    if (es == 0) {
      return 1;
    } else {
      return 0;
    }
  }
  if (es == 0) {
    if (find(arrangement, ss, '#') == -1) {
      return 1;
    } else {
      return 0;
    }
  }

  std::string s(arrangement, arrangement + ss);
  std::vector<int64_t> v(expect, expect + es);
  auto k = std::make_pair(s, v);

  if(TABLE.find(k) != TABLE.cend()) {
    return TABLE[k];
  }

  int64_t i = 0;
  for (; i < ss; ++i) {
    if (arrangement[i] != '.') break;
  }

  if (i > 0) {
    int64_t r = solve_recursive(arrangement + i, ss - i, expect, es);
    TABLE[k] = r;
    return r;
  }

  int64_t canfit = 0;
  i = 1;
  for (; i < ss && i < expect[0]; ++i) {
    if (arrangement[i] == '.') {
      break;
    }
  }

  if(i == expect[0]) {
    if (i == ss || arrangement[i] != '#') {
      char old = arrangement[i];
      arrangement[i] = '.';
      canfit = solve_recursive(arrangement + i, ss - i, expect + 1, es - 1);
      arrangement[i] = old;
    }
  }

  if(arrangement[0] == '?') {
    arrangement[0] = '.';
    int64_t dot = solve_recursive(arrangement + 1, ss - 1, expect, es);
    arrangement[0] = '?';
    int64_t r = dot + canfit;
    TABLE[k] = r;
    return r;
  } else {
    TABLE[k] = canfit;
    return canfit;
  }
}

void parseFile(const std::string& filename,
               std::vector<std::string>& parsedStrings,
               std::vector<std::vector<int64_t>>& parsedint64_tegers) {
  std::ifstream file(filename);

  std::string line;
  while (std::getline(file, line)) {
    std::istringstream lineStream(line);
    std::string strPart;
    std::vector<int64_t> int64_tPart;

    lineStream >> strPart;

    int64_t number;
    char comma;
    while (lineStream >> number >> comma) {
      int64_tPart.push_back(number);
    }
    int64_tPart.push_back(number);
    parsedStrings.push_back(strPart);
    parsedint64_tegers.push_back(int64_tPart);
  }
}

int main() {
  std::vector<std::string> strs;
  std::vector<std::vector<int64_t>> int64_ts;
  parseFile("12.input.2", strs, int64_ts);

  int64_t t = 0;
  for (size_t i = 0; i < strs.size(); ++i) {
    // std::cout << strs[i] << std::endl;
    // for(auto i : int64_ts[i])
    //   std::cout << i << ",";
    // std::cout << std::endl;
    TABLE.clear();
    int64_t s = solve_recursive((char*)strs[i].c_str(), strs[i].size(),
                            int64_ts[i].data(), int64_ts[i].size());
    t += s;

    int64_t r = 0;
    for(auto &[k, v] : TABLE)
      r += (v - 1);
    std::cout << s << " " << r << " " << TABLE.size() << std::endl;
  }

  std::cout << t << std::endl;

  return 0;
}