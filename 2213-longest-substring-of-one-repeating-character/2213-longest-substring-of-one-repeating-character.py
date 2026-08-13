class Solution:
    def longestRepeating(
        self,
        s: str,
        queryCharacters: str,
        queryIndices: List[int]
    ) -> List[int]:

        n = len(s)

        # Each segment tree node stores:
        # [left_character, right_character, prefix_length,
        #  suffix_length, best_length, total_length]
        tree = [None] * (4 * n)

        def merge(left, right):
            if left is None:
                return right
            if right is None:
                return left

            left_char, left_right_char, left_pre, left_suf, left_best, left_len = left
            right_char, right_right_char, right_pre, right_suf, right_best, right_len = right

            # Character at the extreme ends
            new_left_char = left_char
            new_right_char = right_right_char

            # Prefix
            new_pre = left_pre

            if left_pre == left_len and left_right_char == right_char:
                new_pre = left_len + right_pre

            # Suffix
            new_suf = right_suf

            if right_suf == right_len and left_right_char == right_char:
                new_suf = right_len + left_suf

            # Best repeating substring
            new_best = max(left_best, right_best)

            # A repeating substring can cross the boundary
            if left_right_char == right_char:
                new_best = max(new_best, left_suf + right_pre)

            return (
                new_left_char,
                new_right_char,
                new_pre,
                new_suf,
                new_best,
                left_len + right_len
            )

        def build(node, l, r):
            if l == r:
                tree[node] = (s[l], s[l], 1, 1, 1, 1)
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        def update(node, l, r, index, char):
            if l == r:
                tree[node] = (char, char, 1, 1, 1, 1)
                return

            mid = (l + r) // 2

            if index <= mid:
                update(node * 2, l, mid, index, char)
            else:
                update(node * 2 + 1, mid + 1, r, index, char)

            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        build(1, 0, n - 1)

        answer = []

        for i in range(len(queryIndices)):
            index = queryIndices[i]
            char = queryCharacters[i]

            update(1, 0, n - 1, index, char)

            # Root contains information about the entire string
            answer.append(tree[1][4])

        return answer