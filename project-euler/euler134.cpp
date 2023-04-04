#include <chrono>
#include <iostream>
#include <vector>

std::vector<bool> sieve(size_t n) {
    std::vector<bool> is_prime(n, true);
    is_prime[0] = is_prime[1] = false;
    for(size_t p = 2; p * p < n; ++p){
        if(is_prime[p]) {
            for(size_t i = p * p; i < n; i += p) 
                is_prime[i] = false;
        }
    }
    return is_prime;
}

std::vector<size_t> extract_primes(const std::vector<bool> &is_prime) {
    std::vector<size_t> primes;
    for(size_t i = 2; i < is_prime.size(); ++i) {
        if(is_prime[i])
            primes.push_back(i);
    }
    return primes;
}

inline size_t find_s_naive(size_t p1, size_t p2, size_t d) {
    auto p = p2;
    while (p % d != p1) {
        p += p2;
    }
    return p;
}

using namespace std::chrono;

int main() {
    auto t0 = high_resolution_clock::now();
    const auto is_prime = sieve(2'000'000);
    auto t1 = high_resolution_clock::now();
    const auto primes = extract_primes(is_prime);
    auto t2 = high_resolution_clock::now();
    std::vector<size_t> ss;
    size_t d = 10;
    for(size_t i = 2; i < primes.size(); ++i) {
        if(primes[i] > 1'000'000)
            break;
        if(primes[i] / d)
            d *=  10;
        if(i % 100 == 0)
            std::cout << i << "\n";
        ss.push_back(find_s_naive(primes[i], primes[i + 1], d));
    }
    auto t3 = high_resolution_clock::now();
    std::cout << duration_cast<milliseconds>(t1 - t0).count() << std::endl;
    std::cout << duration_cast<milliseconds>(t2 - t1).count() << std::endl;
    std::cout << duration_cast<milliseconds>(t3 - t2).count() << std::endl;
    std::cout << ss.back() << std::endl;
    return 0;
}