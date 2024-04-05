class Solution {
public:
    int kthFactor(int n, int k) {
        int a[200];
        // int count=0;
        int j=0;
        for(int i=1;i<=n;)
        {
            if(n%i==0)
            {
                a[j] = i;
                j++;
                // count++;
            }
                i++;   
        }
        if(j < k)
        {
            return -1;
        }
        return a[k-1];
    }
};