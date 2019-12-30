class Solution:
    def reverse(self, x):
        if x>=2**31 or x<-2**31:
            return 0
        else:
            return str(x)[::-1]

def main():
    print(Solution().reverse(123))
    print(Solution().reverse(2**31))

if __name__== "__main__":
    main()