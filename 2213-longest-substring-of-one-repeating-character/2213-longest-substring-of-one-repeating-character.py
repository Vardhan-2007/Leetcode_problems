from typing import List

class Solution:
    def longestRepeating(
        self,
        s: str,
        queryCharacters: str,
        queryIndices: List[int]
    ) -> List[int]:

        n = len(s)

        # Segment tree size
        size = 1
        while size < n:
            size <<= 1

        # For every node:
        # left character
        # right character
        # prefix length
        # suffix length
        # best length
        left = [''] * (2 * size)
        right = [''] * (2 * size)
        prefix = [0] * (2 * size)
        suffix = [0] * (2 * size)
        best = [0] * (2 * size)
        length = [0] * (2 * size)

        # Build leaves
        for i, ch in enumerate(s):
            p = size + i

            left[p] = right[p] = ch
            prefix[p] = suffix[p] = best[p] = length[p] = 1

        # Build tree
        for p in range(size - 1, 0, -1):
            a = p << 1
            b = a | 1

            left[p] = left[a]
            right[p] = right[b]
            length[p] = length[a] + length[b]

            same = right[a] == left[b]

            prefix[p] = prefix[a]
            if same and prefix[a] == length[a]:
                prefix[p] += prefix[b]

            suffix[p] = suffix[b]
            if same and suffix[b] == length[b]:
                suffix[p] += suffix[a]

            best[p] = best[a]
            if best[b] > best[p]:
                best[p] = best[b]

            if same:
                x = suffix[a] + prefix[b]
                if x > best[p]:
                    best[p] = x

        ans = []

        # Process queries
        for idx, ch in zip(queryIndices, queryCharacters):

            p = size + idx

            # Update leaf
            left[p] = right[p] = ch
            prefix[p] = suffix[p] = best[p] = length[p] = 1

            # Update ancestors
            p >>= 1

            while p:
                a = p << 1
                b = a | 1

                left[p] = left[a]
                right[p] = right[b]
                length[p] = length[a] + length[b]

                same = right[a] == left[b]

                prefix[p] = prefix[a]
                if same and prefix[a] == length[a]:
                    prefix[p] += prefix[b]

                suffix[p] = suffix[b]
                if same and suffix[b] == length[b]:
                    suffix[p] += suffix[a]

                best[p] = best[a]
                if best[b] > best[p]:
                    best[p] = best[b]

                if same:
                    x = suffix[a] + prefix[b]
                    if x > best[p]:
                        best[p] = x

                p >>= 1

            ans.append(best[1])

        return ans