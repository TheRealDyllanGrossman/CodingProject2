#include <algorithm>
#include <chrono>
#include <iomanip>
#include <iostream>
#include <random>
#include <vector>
#include <string.h>



void setup(int64_t N, uint64_t A[]) {
    for (int64_t i = 0; i < N; i++) {
        A[i] = i;
    }
}

int64_t sum(int64_t N, uint64_t A[]) {
    int64_t result = 0;
    for (int64_t i = 0; i < N; i++) {
        result += A[i];
    }
    return result;
}
