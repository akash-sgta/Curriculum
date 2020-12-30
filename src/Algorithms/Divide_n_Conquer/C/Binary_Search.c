#include "c_searching_api.h"

C_SEARCHING_API int BinarySearch_INT(int* array, int key, int l , int h){

    if ( l > h) return 0;

    int mid =  l + (int)((h-1)/2);

    if (key == array[mid])
        return (mid + 1);
    if ( key < array[mid])
        return BinarySearch(array, key, l, mid-1); 
    else 
        return BinarySearch(array, key, mid+1, h);
}

C_SEARCHING_API int BinarySearch_FLOAT(float* array, float key, int l , int h){
    if ( l > h) return 0;

    int mid =  l + (int)((h-1)/2);
    
    if (key == array[mid])
        return (mid + 1);
    if ( key < array[mid])
        return BinarySearch(array, key, l, mid-1); 
    else 
        return BinarySearch(array, key, mid+1, h);
}

C_SEARCHING_API int BinarySearch_LONG(long* array, long key, int l , int h){
    if ( l > h) return 0;

    int mid =  l + (int)((h-1)/2);
    
    if (key == array[mid])
        return (mid + 1);
    if ( key < array[mid])
        return BinarySearch(array, key, l, mid-1); 
    else
        return BinarySearch(array, key, mid+1, h);
}

C_SEARCHING_API int BinarySearch_DOUBLE(double* array, double key, int l , int h){
    if ( l > h) return 0;

    int mid =  l + (int)((h-1)/2);
    
    if (key == array[mid])
        return (mid + 1);
    if ( key < array[mid])
        return BinarySearch(array, key, l, mid-1); 
    else
        return BinarySearch(array, key, mid+1, h);
}