#include <iostream>
#include <vector>
#include <unordered_map>
#include <map>
#include <cassert>
#include <chrono>

using namespace std;

using ui = unsigned long long int; 
using map_t = unordered_map<ui, unsigned char>;

using std::chrono::high_resolution_clock;
using std::chrono::duration_cast;
using std::chrono::duration;
using std::chrono::milliseconds;

vector<bool> get_is_prime(ui n_primes){
    vector<bool> is_prime(n_primes+1, true);
    is_prime[0] = is_prime[1] = false;
    for (ui i = 2; i * i <= n_primes; i++) {
        if (is_prime[i]) {
            for (ui j = i * i; j <= n_primes; j += i)
                is_prime[j] = false;
        }
    }
    return is_prime;
}

vector<ui> get_primes(const vector<bool> &is_prime) {
    vector<ui> primes;
    for(ui i = 2; i < is_prime.size(); ++i) {
        if(is_prime[i])
            primes.push_back(i);
    }
    return primes;
}

vector<map_t> get_factorization(ui n, const vector<ui> &primes) {
    vector<map_t> factorizations(n);
    for(ui i = 2; i < n; ++i) {
        if(i % (n/100) == 0)
            cout << i / (n/100) << "%" << endl;
        const auto ub = std::min(primes.cbegin() + i + 1, primes.cend());
        const auto it = std::lower_bound(primes.cbegin(), ub, i);
        if( (it != ub) && ((*it) == i) ) {
            factorizations[i].emplace(i, 1);
        } else {
            for(ui j = 0; j < primes.size(); ++j) {
                const auto div = primes[j];
                if(i % div == 0) {
                    factorizations[i] = factorizations[i / div];
                    factorizations[i][div] += 1;
                    break;
                }
            }
        }
    }
    return factorizations;
}

vector<map_t> get_factorial_factorization(const vector<map_t> &factorizations) {
    vector<map_t> fact_factorizations(factorizations.size());
    fact_factorizations[2] = factorizations[2];
    for(ui i = 3; i < fact_factorizations.size(); ++i) {
        if(i % (factorizations.size()/100) == 0)
            cout << i / (factorizations.size()/100) << "%" << endl;
        fact_factorizations[i] = fact_factorizations[i-1];
        for(const auto &[k,v] : factorizations[i])
            fact_factorizations[i][k] += v;
    }
    return fact_factorizations;
}

bool is_divided(map_t n, map_t div) {
    for(const auto &[k, v] : div) {
        if( n[k] < v)
            return false;
    }
    return true;
}

ui s(ui n, const vector<map_t> &ff, const vector<map_t> &f) {
    for(ui i = 0; i < ff.size(); ++i) {
        if(is_divided(ff[i], f[n])) {
            //cout << n << ","<< i << endl;
            return i;
        }
    }
    return -1;
}

ui S(ui n, const vector<map_t> &ff, const vector<map_t> &f) {
    ui tot = 0;
    for(ui i = 2; i < n + 1; ++i) {
        //if(i % (n/100) == 0)
        //    cout << i / (n/100) << "%" << endl;
        tot += s(i, ff, f);
    }
    return tot;
}

void print(const map_t &m) {
    for(const auto &[k,v] : m)
        cout << "{" <<k <<","<< int(v) <<"}"<< ";";
    cout << endl;
}

ui how_many_times_n_factorial_divisible_by_k(ui n, ui k) {
    ui result = 0, k_pow = k;
    while( n / k_pow > 0 ) {
        result += n / k_pow;
        k_pow *= k;
    }
    return result;
}

ui how_many_times_n_divisible_by_k(ui n, ui k) {
    ui result = 0;
    while( n % k == 0 ) {
        n /= k;
        result++;
    }
    return result;
}

ui s(ui n, const vector<ui> &ss, const vector<ui> &primes, const vector<bool> &is_primes) {
    if(is_primes[n]) {
        return n;
    } else {
        for(const auto &p : primes) {
            if( n % p == 0 ) {
                auto base = ss[n / p];
                while( how_many_times_n_factorial_divisible_by_k(base, p) < how_many_times_n_divisible_by_k(n, p) ) {
                    base++;
                } 
                return base;
            }
        }
    }
    return -1;
}

ui S(ui n, const vector<ui> &primes, const vector<bool> &is_primes) {
    vector<ui> ss(n+1);
    ui result = 0;
    for(size_t i = 2; i <= n; ++i) {
        if(i % (n/100) == 0)
            cout << i / (n/100) << "%" << endl;
        ss[i] = s(i, ss, primes, is_primes);
        result += ss[i];
        //cout << i << "," << ss[i] << endl;
    }
    return result;
}

int main() {
    constexpr ui max = 100000001ull;
    std::cout << "Building primes" << std::endl;
    const auto is_prime = get_is_prime(max);
    const auto primes = get_primes(is_prime);

/*
    std::cout << "Factorizing" << std::endl;
    auto t1 = high_resolution_clock::now();
    const auto factorizations = get_factorization(max, primes);

    cout << "Factorizing factorial" << endl;
    const auto factorial_factorization = get_factorial_factorization(factorizations);

    cout << "Eval S" << endl;
    cout << S(max - 1, factorial_factorization, factorizations) << endl;
    auto t2 = high_resolution_clock::now();
    cout << "Time elapsed: " << duration_cast<milliseconds>(t2 - t1).count() << "[ms]"<< endl;
*/

    cout << "Eval S v2" << endl;
    auto t3 = high_resolution_clock::now();
    cout << S(max - 1, primes, is_prime) << endl;
    auto t4 = high_resolution_clock::now();
    cout << "Time elapsed: " << duration_cast<milliseconds>(t4 - t3).count() << "[ms]"<< endl;

    return 0;
}