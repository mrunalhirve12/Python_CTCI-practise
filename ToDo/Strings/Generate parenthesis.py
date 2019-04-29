#https://leetcode.com/problems/generate-parentheses/discuss/215927/Python-solution

def generateParenthesis(n: 'int') -> 'List[str]':
    pairs = ["()"]
    i = 1
    while i < n:
        new_pairs = set()
        for p in pairs:
            for index, c in enumerate(p):
                if c == "(":
                    new_pairs.add(p[0:index + 1] + "()" + p[index + 1:])
            new_pairs.add(p + "()")
        pairs = list(new_pairs)
        i += 1
    print(pairs)
