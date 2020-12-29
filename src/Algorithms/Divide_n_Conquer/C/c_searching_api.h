#ifndef C_SEARCHING_API
#define C_SEARCHING_API

/*
 * Binary Search Basically Return the index of the element if the element was found
 * else It will return 0;
 * array is the array you want to search into
 * key -> the value you want to search
 * l -> lowest index probably 0
 * h -> highest index probably strlen(array)
 * 
 * only Works if the array is allready shorted
 */
C_SEARCHING_API int BinarySearch_INT(int* array, int key, int l , int h);
C_SEARCHING_API int BinarySearch_FLOAT(float* array, float key, int l , int h);
C_SEARCHING_API int BinarySearch_LONG(long* array, long key, int l , int h);
C_SEARCHING_API int BinarySearch_DOUBLE(double* array, double key, int l , int h);

#endif C_SEARCHING_API