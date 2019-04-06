"""
Note: This is a companion problem to the System Design problem: Design TinyURL.
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded
to a tiny URL and the tiny URL can be decoded to the original URL.
"""


class Codec:

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        self.url_dict = {}
        # using hash function to encode and then append to the new url
        shortUrl = "http://tinyurl.com/" + str(hash(longUrl))
        # add in dic the shortUrl and longUrl in key value pair
        self.url_dict[shortUrl] = longUrl
        # return shortUrl i.e the encoded Url
        return shortUrl

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        # return the original url stored in key value pair
        return self.url_dict[shortUrl]


# Your Codec object will be instantiated and called as such:
url = "https://leetcode.com/problems/design-tinyurl"
codec = Codec()
print(codec.encode(url))
print(codec.decode(codec.encode(url)))
