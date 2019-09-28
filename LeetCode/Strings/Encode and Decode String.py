"""

"""


class Codec:

    def encode(self, strs):
        result = ''
        for s in strs:
            result += (str(len(s)) + ' ' + s)

        return result

    def decode(self, s):
        result = []
        i = 0
        while i < len(s):
            n = 0
            current = ''
            while s[i].isdigit():
                #n = n * 10 + int(s[i])
                i += 1

            i += 1  # skip the splitting space

            #for j in range(n):
            current += s[i]
            i += 1

            result.append(current)

        return result

strs = "Hello World"
# Your Codec object will be instantiated and called as such:
codec = Codec()
codec.decode(codec.encode(strs))