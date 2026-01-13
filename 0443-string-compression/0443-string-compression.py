class Solution:
    def compress(self, chars: List[str]) -> int:
        read=0
        write=0

        while read <len(chars):
            curr=chars[read]
            count=0

            while read<len(chars) and chars[read]==curr:
                count=count+1
                read=read+1
            chars[write]=curr
            write=write+1

            if count>1:
                for digit in str(count):
                    chars[write]=digit
                    write=write+1

        return write
