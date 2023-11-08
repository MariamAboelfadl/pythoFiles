class Solution(object):
    def reverse(self, x):
        s=str(x)
        if s.startswith('-')==False:
            rev=s[: :-1]
            n=int(rev)
        else:
            s=s[1:]
            rev=s[: :-1]
            rev="-"+rev
            n=int(rev)
        if n<((-2)**31) or n>((2**31)-1):
            return 0
        else:
            return n