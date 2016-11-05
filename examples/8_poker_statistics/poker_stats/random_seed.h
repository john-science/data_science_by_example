
#ifndef _RANDOM_SEED
#define _RANDOM_SEED

int randint(const int);
int randint(const int, const int);
template<typename T> T choice(const T arr[], const int length);
bool in_array(const int arr[], const int value);
int* floyds_algorithm(const int, const int);

#endif
