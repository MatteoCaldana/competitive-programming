#include <iostream>
#include <string>
#include <vector>

#define SPLIT_LENGTH 12
#define NSPLITS 10000

void print(long long current[SPLIT_LENGTH]) {
    for(long long j = 0; j < SPLIT_LENGTH; ++j) {
        std::cout << current[j] << " ";
    }
    std::cout << std::endl;
}

long long toi(const char *string, long long len) {
    long long result = 0;
    long long exp = 1;
    for(long long i = 0; i < len; ++i) {
        result += exp * (string[len-i-1] - '0');
        exp *= 10;
    }
    return result;
}

void split_string(const char *string, long long str_len, long long results[NSPLITS][SPLIT_LENGTH], long long &nres, long long current[SPLIT_LENGTH], long long depth) {
    current[depth] = toi(string, str_len);
    std::copy(current, current+SPLIT_LENGTH, results[nres++]);
    for(long long i = 1; i < str_len; ++i) {
        current[depth] = toi(string, i);
        split_string(string+i, str_len-i, results, nres, current, depth+1);
    }
    current[depth] = 0;
}

void print(long long results[NSPLITS][SPLIT_LENGTH], long long how_many) {
    for(long long i = 0; i < how_many; ++i) {
        for(long long j = 0; j < SPLIT_LENGTH; ++j) {
            std::cout << results[i][j] << " ";
        }
        std::cout << std::endl;
    }
}

bool is_S(long long root) {
    long long results[NSPLITS][SPLIT_LENGTH];
    long long current[SPLIT_LENGTH] = {0,0,0, 0,0,0, 0,0,0, 0,0,0};
    long long n_res = 0;
    const std::string s = std::to_string(root*root);
    split_string(s.c_str(), s.length(), results, n_res, current, 0);
    for(long long i = 0; i < n_res; ++i) {
        long long partial_result = 0;
        for(long long j = 0; j < SPLIT_LENGTH; ++j) {
            partial_result += results[i][j];
        }
        if( partial_result == root ) {
            return true;
        }
    }
    return false;
}

int main() {
    long long result = 0;
    for(long long i = 3; i <= 1000000; ++i) {
        if( i % 10000 == 0) std::cout << i << std::endl;
        if(is_S(i)) {
            result += i*i;
        }
    }
    std::cout << "tot" << result << std::endl;
    return 0;
}