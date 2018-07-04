#include <stdio.h>
#include <math.h>

#define E 0.000001

double getMedian(int* nums, int numsSize)
{
    return (double)(nums[numsSize / 2] + nums[(numsSize - 1) / 2]) / 2.0;
}

double mergeSortMedian(int* nums1, int nums1Size, int* nums2, int nums2Size)
{
    int p1 = 0, p2 = 0;
    int count = 0;
    int numsSize = nums1Size + nums2Size;
    int nums[numsSize];
    while(p1 < nums1Size && p2 < nums2Size)
    {
        int min = 0;
        if(nums1[p1] < nums2[p2])
        {
            min = nums1[p1++];
        }
        else
        {
            min = nums2[p2++];
        }
        nums[count++] = min;
    }
    while(p1 < nums1Size)
    {
        nums[count++] = nums1[p1++];
    }
    while(p2 < nums2Size)
    {
        nums[count++] = nums2[p2++];
    }
    return getMedian(nums, numsSize);
}

double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) 
{
    int m = nums1Size;
    int n = nums2Size;

    // Base case
    if(m <= 2 || n <=2)
    {
        if(m > 2)
        {
            nums1 = nums1 + (m - 3) / 2;
            m = (m + 4) / 2 - (m - 3) / 2;
        }
        if(n > 2)
        {
            nums2 = nums2 + (n - 3) / 2;
            n = (n + 4) / 2 - (n - 3) / 2;
        }
        // printf("mergeSortMedian(nums1, %d, nums2[0] = %d, %d)\n", m, nums2[0], n);
        return mergeSortMedian(nums1, m, nums2, n);
    }

    double median1 = getMedian(nums1, nums1Size);
    double median2 = getMedian(nums2, nums2Size);
    if(fabs(median1 - median2) < E)
    {
        return median1;
    }

    // Divide
    int minSize = m < n ? (m - 1) / 2 : (n - 1) / 2;
    return median1 < median2 
        ? findMedianSortedArrays(nums1 + minSize, m - minSize, nums2, n - minSize)
        : findMedianSortedArrays(nums1, m - minSize, (nums2 + minSize), n - minSize);
}

// int main(int argc, char const *argv[])
// {
//     int nums1[0] = {};
//     int nums2[5] = {1, 2, 3, 4, 5};
//     printf("%f\n", findMedianSortedArrays(nums1, 0, nums2, 5));
//     return 0;
// }
