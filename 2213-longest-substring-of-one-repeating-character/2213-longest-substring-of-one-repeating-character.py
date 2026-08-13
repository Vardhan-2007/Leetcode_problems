from typing import List


class Solution:
    def longestRepeating(
        self,
        s: str,
        queryCharacters: str,
        queryIndices: List[int]
    ) -> List[int]:

        n = len(s)

        # Each node:
        # [left_char, right_char, prefix, suffix, best, length]
        tree = [None] * (4 * n)

        def merge(a, b):
            if a is None:
                return b
            if b is None:
                return a

            lc1, rc1, pre1, suf1, best1, len1 = a
            lc2, rc2, pre2, suf2, best2, len2 = b

            same = rc1 == lc2

            prefix = pre1
            if pre1 == len1 and same:
                prefix += pre2

            suffix = suf2
            if suf2 == len2 and same:
                suffix += suf1

            best = max(best1, best2)

            if same:
                best = max(best, suf1 + pre2)

            return (
                lc1,
                rc2,
                prefix,
                suffix,
                best,
                len1 + len2
            )

        def build(node, l, r):
            if l == r:
                ch = s[l]
                tree[node] = (ch, ch, 1, 1, 1, 1)
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        def update(node, l, r, idx, ch):
            if l == r:
                tree[node] = (ch, ch, 1, 1, 1, 1)
                return

            mid = (l + r) // 2

            if idx <= mid:
                update(node * 2, l, mid, idx, ch)
            else:
                update(node * 2 + 1, mid + 1, r, idx, ch)

            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        build(1, 0, n - 1)

        ans = []

        for idx, ch in zip(queryIndices, queryCharacters):
            update(1, 0, n - 1, idx, ch)
            ans.append(tree[1][4])

        return ans