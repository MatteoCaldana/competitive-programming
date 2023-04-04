#include <iostream>
#include <string>
#include <vector>

#define SPLIT_LENGTH 12
#define NSPLITS 1940

void print(int current[SPLIT_LENGTH]) {
    for(int j = 0; j < SPLIT_LENGTH; ++j) {
        std::cout << current[j] << " ";
    }
    std::cout << std::endl;
}

int toi(const char *string, int len) {
    int result = 0;
    int exp = 1;
    for(int i = 0; i < len; ++i) {
        result += exp * (string[len-i-1] - '0');
        exp *= 10;
    }
    return result;
}

void split_string(const char *string, const int str_len, int results[NSPLITS][SPLIT_LENGTH],
                  int &nres, int current[SPLIT_LENGTH], const int depth,
                  const int max_len, const int root) {
    if(str_len < max_len) {
        current[depth] = toi(string, str_len);
        std::copy(current, current+SPLIT_LENGTH, results[nres++]);
    }
    for(int i = 1; i < std::min(str_len, max_len); ++i) {
        current[depth] = toi(string, i);
        split_string(string+i, str_len-i, results, nres, current, depth+1, max_len, root);
    }
    current[depth] = 0;
}

void print(int results[NSPLITS][SPLIT_LENGTH], int how_many) {
    for(int i = 0; i < how_many; ++i) {
        for(int j = 0; j < SPLIT_LENGTH; ++j) {
            std::cout << results[i][j] << " ";
        }
        std::cout << std::endl;
    }
}

bool is_S(int root) {
    int results[NSPLITS][SPLIT_LENGTH];
    int current[SPLIT_LENGTH] = {0,0,0, 0,0,0, 0,0,0, 0,0,0};
    int n_res = 0;
    const std::string s = std::to_string(root*root);
    const std::string sr = std::to_string(root);
    split_string(s.c_str(), s.length(), results, n_res, current, 0, sr.length()+1, root);
    for(int i = 0; i < n_res; ++i) {
        int partial_result = 0;
        for(int j = 0; j < SPLIT_LENGTH; ++j) {
            partial_result += results[i][j];
        }
        if( partial_result == root ) {
            return true;
        }
    }
    return false;
}

int main() {
    int result = 0;
    for(int i = 3; i <= 1000000; ++i) {
        if( i % 10000 == 0) std::cout << i << std::endl;
        if(is_S(i)) {
            result += i*i;
        }
    }
    std::cout << "tot" << result << std::endl;
    return 0;
}
