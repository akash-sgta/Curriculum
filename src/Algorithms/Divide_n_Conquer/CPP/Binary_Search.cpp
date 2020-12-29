#include "searching_api.hpp"

template<typename t>
SEARCHING_API int BinarySearch(t* array, t key, int l, int h){
    if ( l > h) return 0;

    int mid =  l + (int)((h-1)/2);

    if (key == array[mid])
        return (mid + 1);
    if ( key < array[mid])
        return BinarySearch(array, key, l, mid-1); 
    else 
        return BinarySearch(array, key, mid+1, h);
}