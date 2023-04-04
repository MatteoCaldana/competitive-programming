#include "utils.hpp"

bool is_prime_generating_pt1(luint n, const std::vector<luint> & squared_primes) {
    // if d^2 divides n this would lead in (d + n/d) to (d + dk) which has d as a divisor
    for(auto i : squared_primes) {
        if(i > n)
            break; 
        if(n % i == 0)
            return false; 
    }
    return true;
}

bool is_prime_generating_pt2(luint n, const std::vector<luint> & prime_table) {
    luint bound = static_cast<luint>(std::sqrt(static_cast<double>(n))) + 1;
    for(luint i = 1; i < bound; ++i) {
        if(n % i == 0) {
            if(!is_in_sorted(prime_table, i + n / i))
                return false;
        }
    }
    return true;
}

const std::vector<luint> square_vector(const std::vector<luint> & v) {
    std::vector<luint> result(v.size());
    for(luint i = 0; i < v.size(); ++i) {
        result[i] = v[i] * v[i];
    }
    return result;
}

int main() {
    luint limit = 100000000;
    const auto prime_table(fill_prime_table(limit));
    std::cout << prime_table.size() << std::endl;

    const auto squared(square_vector(prime_table));

    std::vector<luint> generating_pt1;
    for(auto i : prime_table) {
        if(is_prime_generating_pt1(i-1, squared))
            generating_pt1.push_back(i-1);
    }
    std::cout << generating_pt1.size() << std::endl;

    std::vector<luint> generating_pt2;
    for(luint i = 0; i < generating_pt1.size(); ++i) {
        if(is_prime_generating_pt2(generating_pt1[i], prime_table))
            generating_pt2.push_back(generating_pt1[i]);
    }
    std::cout << generating_pt2.size() << std::endl;

    luint sum = 0;
    for(auto i : generating_pt2) {
        sum += i;
    }
    std::cout << sum << std::endl;
    
    return 0;
}