#include <iostream>
#include <vector>
#include <cmath>
#include <list>
#include <algorithm>

template<typename T>
void print(T v, char sep = ' ') {
    for(auto i : v)
        std::cout << i << sep;
    return;
}


bool is_prime(const std::vector<uint> & prime_table, uint n) {
    uint bound = static_cast<uint>(std::sqrt(static_cast<double>(n))) + 1;

    uint i = 0;
    while(prime_table[i] < bound) {
        if(n % prime_table[i] == 0)
            return false;
        ++i;
    }
    return true;
}

const std::vector<uint> fill_prime_table(uint limit) {
    std::vector<uint> table = {2};
    for(uint i = 3; i < limit; ++i) {
        if(is_prime(table, i)) {
            table.push_back(i);
        }
    }
    return table;
}

const std::vector<uint> divisors(const std::vector<uint> & prime_table, const std::vector<std::vector<uint>> & div_table, uint n) {
    auto it = std::lower_bound(prime_table.begin(), prime_table.end(), n);
    if(it != prime_table.end()) {
        if(*it == n)
            return std::vector<uint>({1, n});
    }
    for(const uint i : prime_table) {
        if(n % i == 0) {
            uint div = n / i;
            std::vector<uint> new_div;
            for(auto j : div_table[div])
                new_div.push_back(j*i);
            std::vector<uint> result(div_table[div].size() + new_div.size());
            auto it = std::set_union(new_div.begin(), new_div.end(), div_table[div].begin(), div_table[div].end(), result.begin());
            result.resize(it - result.begin());
            return result;
        }
    }
    std::cout << "ERROR in divisors";
    std::exit(0);
    return std::vector<uint>();
}

const std::vector<std::vector<uint>> fill_div_table(const std::vector<uint> & prime_table, uint limit) {
    std::vector<std::vector<uint>> table = {{},{1}};
    for(uint i = 2; i < limit; ++i) {
        table.push_back(divisors(prime_table, table, i));
    }
    return table;
}

uint amicable_chain(uint n, const std::vector<uint> & sum_div, std::vector<bool> & visited) {
    const uint N = 5916;


    uint chain_size = 1;
    std::vector<uint> mem = {n};
    n = sum_div[n];

    auto it = std::lower_bound(mem.begin(), mem.end(), n);
    while( it == mem.end() ) {
        if( n == 1 || n >= visited.size() || visited[n] ) {
            if(mem[0] == N)
                std::cout << "BREAK" << std::endl; 
            chain_size = it - mem.begin();
            break;
        }
        if(mem[0] == N)
            std::cout << n << std::endl;
        visited[n] = true;
        mem.push_back(n);
        n = sum_div[n];
        ++chain_size;

        it = std::lower_bound(mem.begin(), mem.end(), n);
        if( it != mem.end() && *it != n )
            it = mem.end();
    }
    chain_size -= it - mem.begin();
    if(mem[0] == N) {
        std::cout << "find:" << n << std::endl;
        print(mem);
        std::cout << std::endl;
        std::cout << "offset:" << it - mem.begin() << std::endl;
        std::cout << "chain length:" << chain_size << std::endl;
    }
    return chain_size;
}

int main() {
    const uint limit = 1000000;
    auto v(fill_prime_table(limit));
    auto d(fill_div_table(v, limit));
    std::vector<uint> sum_div;
    for(uint i = 0; i < d.size(); ++i) {
        uint sum = 0;
        for(auto j : d[i])
            sum += j;
        sum_div.push_back(sum - i);
    }
    
    std::vector<uint> to_check;
    for(uint i = 4; i < limit; ++i)
        to_check.push_back(i);
    std::vector<uint> s(limit);
    auto it = std::set_difference(to_check.begin(), to_check.end(), v.begin(), v.end(), s.begin());
    s.resize(it - s.begin());

    std::vector<bool> visited(limit, false);
    std::vector<uint> result(limit, 0);

    std::cout << "===============================================" << std::endl;

    for(uint i = 0; i < s.size(); ++i) {
        //print(visited);
        //std::cout << std::endl;
        //print(result);
        //std::cout << std::endl;
        //std::cout << "to visit:" << s[i] << std::endl;
        //std::cout << "\n===============================================" << std::endl;

        uint to_visit = s[i];

        if(to_visit == 12496)
            std::cout << visited[to_visit] << std::endl;

        if( !visited[to_visit] ) {
            result[to_visit] = amicable_chain(to_visit, sum_div, visited);
        }
    }

    auto res = std::max_element(result.begin(), result.end());
    std::cout << "chain lenght:" << *res 
    << "\nfirst element of the chain:" << res - result.begin() 
    << "\ndiv sum:" << sum_div[res - result.begin()] << std::endl;

    return 0;
}