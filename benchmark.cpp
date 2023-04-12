#include <algorithm>
#include <chrono>
#include <iomanip>
#include <iostream>
#include <random>
#include <vector>
#include <string.h>

extern void setup(int64_t N, uint64_t A[]);
extern int64_t sum(int64_t N, uint64_t A[]);

int main(int argc, char** argv)
{
    std::cout << std::fixed << std::setprecision(2);

    std::vector<int64_t> problem_sizes{1 << 20, 1 << 28}; // 1M and 256M
    std::vector<uint64_t> A(1 << 28);
    int64_t t;
    std::vector<int> sum_calls(problem_sizes.size(), 0);
    double min_duration = 30.0;
    int total_counter = 0; // Add the total counter here

    for (size_t i = 0; i < problem_sizes.size(); ++i)
    {
        int64_t n = problem_sizes[i];
        printf("Working on problem size N=%d \n", n);

        setup(n, &A[0]);
        double elapsed_time = 0.0;

        auto start_time = std::chrono::high_resolution_clock::now();
        do
        {
            t = sum(n, &A[0]);
            sum_calls[i]++;
            total_counter++; // Increment the total counter here

            auto end_time = std::chrono::high_resolution_clock::now();
            auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end_time - start_time).count();
            elapsed_time = duration / 1e6;
        } while (elapsed_time < min_duration);

        printf("Elapsed time = %lf seconds\n", elapsed_time);
        printf("Sum result = %lld \n", t);
    }

    for (size_t i = 0; i < problem_sizes.size(); ++i)
    {
        printf("Problem size N=%d was executed %d times\n", problem_sizes[i], sum_calls[i]);
    }

    printf("Total executions: %d\n", total_counter); // Print the total counter here

    return 0;
}

//EOF
