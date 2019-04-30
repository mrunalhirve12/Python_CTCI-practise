"""
A sentence S is given, composed of words separated by spaces. Each word consists of lowercase and uppercase letters only.

We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)

The rules of Goat Latin are as follows:

If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
For example, the word 'apple' becomes 'applema'.

If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add "ma".
For example, the word "goat" becomes "oatgma".

Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.
Return the final sentence representing the conversion from S to Goat Latin.



Example 1:

Input: "I speak Goat Latin"
Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
Example 2:

Input: "The quick brown fox jumped over the lazy dog"
Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"


Notes:

S contains only uppercase, lowercase and spaces. Exactly one space between each word.
1 <= S.length <= 150.
"""
class Solution(object):

    def toGoatLatin(self, S):
        """
        """
        #:type S: str
        #:rtype: str
        """
        # creat a list with all vowel
        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        # convert string to list with space ' '
        A = S.split(' ')

        # creat a empty list#
        lis = []

        # loop through list A to check every element.
        # If the first letter of A[i] element is a vowel. Then append 'ma'
        for i in range(len(A)):
            if A[i][0] in vowel:
                A[i] = A[i] + 'ma'

            # if the first letter of A[i] element is not a vowel.
            # convert it to a list. pop out the first letter and append this letter,followed by 'ma'.
            if A[i][0] not in vowel:
                lis = list(A[i])
                fir = lis.pop(0)
                lis.append(fir)
                A[i] = "".join(lis)
                A[i] += 'ma'

            # append (i+1) * 'a'
            A[i] += (i + 1) * 'a'
        return ' '.join(A)
    """
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        word_list = S.split()
        for i, word in enumerate(word_list):
            if word[0] in vowels:
                word_list[i] = word + 'ma' + 'a' * (i + 1)
            else:
                word_list[i] = word[1:] + word[0] + 'ma' + 'a' * (i + 1)
        return " ".join(word_list)


s = Solution()
print(s.toGoatLatin("I speak Goat Latin"))