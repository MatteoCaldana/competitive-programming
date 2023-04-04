#include <vector>
#include <iostream>
#include <cmath>

typedef unsigned long long int luint;

template<typename T>
void print(T v, char sep = ' ') {
    for(auto i : v)
        std::cout << i << sep;
    return;
}


bool is_prime(const std::vector<luint> & prime_table, luint n) {
    luint bound = static_cast<luint>(std::sqrt(static_cast<double>(n))) + 1;

    luint i = 0;
    while(prime_table[i] < bound) {
        if(n % prime_table[i] == 0) {
            return false;
        }
        ++i;
    }
    return true;
}

bool is_in_sorted(const std::vector<luint> & iterable, luint n) {
    auto it = std::lower_bound(iterable.begin(), iterable.end(), n);
    if( it != iterable.end() && *it == n )
        return true;
    return false;
}

const std::vector<luint> fill_prime_table(luint limit) {
    std::vector<luint> table = {2};
    for(luint i = 3; i < limit; i+=2) {
        if(is_prime(table, i)) {
            table.push_back(i);
        }
    }
    return table;
}

namespace unint {
    luint pow(luint base, luint exp) {
        luint pow = 1;
        while ( exp ) {
            if ( exp & 1 ) {
                pow *= base;
                --exp;
            }
            base *= base;
            exp = exp / 2;
        }
        return pow;
    }
}
 