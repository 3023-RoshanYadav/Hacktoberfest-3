class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        # code here
        arr.sort()
        dep.sort()
        temp=0
        i=0
        j=0
        station=0
        while (i<n):
            if (arr[i]<=dep[j]):
                temp+=1
                station=max(station,temp)
                i+=1
            else:
                temp-=1
                j+=1
        return station
