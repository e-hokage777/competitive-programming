#include <algorithm>

class Solution {
public:
    int longestPalindrome(string s) {
        int arr[58];
        for(int i = 0; i < s.length(); ++i){
            char current = s[i];
            int index = current - '0' - 17;

            arr[index] += 1;
        }

        int total_evens = 0;
        int max_odd_count = 0;
        for(int i  = 0; i < sizeof(arr) / sizeof(arr[0]); ++i){
            if (arr[i]%2 == 0){
                total_evens += arr[i];
            }
            else{
                max_odd_count = max(max_odd_count, arr[i]);
            }

        }


        return total_evens + max_odd_count ;
    }
};