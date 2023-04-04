#include <iostream>
#include <vector>

#include "utils.hpp"

const std::vector<uint> synteic_spiral(uint n) {
    uint layer = 1;
    uint circle_size = 1;
    uint curr_circle_size = 0;
    uint edge_size = 0;
    std::vector<uint> diagonal_elems;
    for(uint i = 1; i < n; ++i) {
        if(curr_circle_size == circle_size-3*edge_size-1 || 
           curr_circle_size == circle_size-2*edge_size-1 ||
           curr_circle_size == circle_size-edge_size-1 ||
           curr_circle_size == circle_size-1 )
            diagonal_elems.push_back(i);
        if(curr_circle_size == circle_size) {
            curr_circle_size = 0;
            layer += 1;
            edge_size = 2*(layer - 1);
            circle_size = 4*edge_size;
        }
        curr_circle_size += 1;
    }
    return diagonal_elems;
}

int main() {
    uint limit = 26241;
    auto diag = synteic_spiral(limit*limit);
    auto prime_table = fill_prime_table(limit+2);

    uint n_primes = 0;
    for(auto i : diag) {
        bool tmp = is_prime(prime_table, i);
        if( tmp ) {
            n_primes++;
        }
    }
    n_primes--;

    std::cout << n_primes << " " << (2*limit-1) << std::endl;
    std::cout << static_cast<double>(n_primes)/static_cast<double>(2*limit-1) << std::endl;
    return 0;
}