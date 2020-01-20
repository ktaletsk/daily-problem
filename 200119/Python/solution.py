class Solution(object):
    def topKFrequent(self, words, k):
        # Fill this in.
        d = {}
        for word in words:
            if word not in d:
                d.update({word: 1})
            else:
                d[word] += 1

        return [el[0] for el in sorted(list(zip(d.keys(), d.values())), key=lambda x: x[1])[:-k-1:-1]]

def test():
    words = ["daily", "interview", "pro", "pro", "for", "daily", "pro", "problems"]
    k = 2

    assert Solution().topKFrequent(words, k) == ['pro', 'daily']