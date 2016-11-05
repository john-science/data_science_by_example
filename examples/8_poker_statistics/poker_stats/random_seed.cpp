
#include <random>

using namespace std;


/**
 *    Randomly select an integer below a max value.
 */
int randint(const int max_int) {
    float r = static_cast <float> (rand()) / static_cast <float> (RAND_MAX);
    return (int)(r * max_int);
}


/**
 *    Randomly select an integer in a range.
 */
int randint(const int min_int, const int max_int) {
    float r = static_cast <float> (rand()) / static_cast <float> (RAND_MAX);
    return (int)((r * (max_int - min_int)) + min_int);
}


/**
 *    Randomly select an element from an integer array.
 */
template<typename T> T choice(const T arr[], const int length) {
    float r = static_cast <float> (rand()) / static_cast <float> (RAND_MAX);
    return arr[(int)(length * r)];
}


/**
 * Test if value is in array of integers.
 */
template<typename T> bool in_array(const T arr[], const size_t len, const T value) {
    for (size_t i=0; i < len; ++i) {
        if (arr[i] == value) {
            return true;
        }
    }

    return false;
}



/**
 * Floyd's Algorithm
 * Randomly select M distinct value from [0 to N).
 */
int* floyds_algorithm(const int n, const int m) {
    int* result = new int[m];
    int i(0);
    int t(0);

    for (int j = n - m; j < n + 1; ++j) {
        t = randint(1, j + 1);

        if (in_array(result, m, t)) {
            result[i] = j;
        } else {
            result[i] = t;
        }

        i += 1;
    }

    return result;
}
