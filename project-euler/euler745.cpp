#include <iostream>
#include <vector>

using namespace std;

using ui = unsigned long long int; 

vector<ui> get_primes(ui n_primes){
    vector<bool> is_prime(n_primes+1, true);
    is_prime[0] = is_prime[1] = false;
    for (ui i = 2; i * i <= n_primes; i++) {
        if (is_prime[i]) {
            for (ui j = i * i; j <= n_primes; j += i)
                is_prime[j] = false;
        }
    }
    vector<ui> primes;
    for(ui i = 2; i < is_prime.size(); ++i) {
        if(is_prime[i])
            primes.push_back(i);
    }
    return primes;
}

ui g(ui n, const vector<ui> &primes) {
    ui result = 1;
    for(const auto &p : primes) {
        const auto pp = p*p;
        while(n % pp == 0) {
            n /= pp;
            result *= pp;
        }
        if(pp > n)
            break;
    }
    return result;
}

int main() {
    std::cout << "Building primes" << std::endl;
    const auto primes = get_primes(10000000);
    std::cout << "Got primes" << std::endl;
    ui result = 0;
    for(ui i = 1; i <= 1'000'000ull; ++i)
        result += g(i, primes);
    std::cout << result << std::endl;
    return 0;
}