class Algos:

    def two_sum(self, nums, targ):
        prev_map = {}
        poss_combos = []

        for i, num in enumerate(nums):
            difference = targ - num

            if difference in prev_map:
                poss_combos.append((prev_map[difference], i))
            else:
                prev_map[num] = i

        return poss_combos if poss_combos else None


    def binary_search(self, nums, targ):
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if targ > nums[middle]:
                left = middle + 1

            elif targ < nums[middle]:
                right = middle - 1

            else:
                return middle

        return -1


    def valid_parenth(self, string: str):
        stack = []

        valid_map = {
            "}": "{",
            ")": "(",
            "]": "["
        }

        for char in string:

            if char in valid_map:

                if stack and stack[-1] == valid_map[char]:
                    stack.pop()

                else:
                    return False

            else:
                stack.append(char)

        return len(stack) == 0
   
   
    def sliding_window(self, string: str):
        left = 0
        string_tracker = set()
        result = 0
       
        for r in range(len(string)):
            while string[r] in string_tracker:
                string_tracker.remove(string[left])
                left += 1
            string_tracker.add(string[r])
           
            result = max(result, (r - left) + 1)
           
        return result
   
    def top_k_frequency(self, numbers, k):
        freq_map ={}
        freq = [[] for i in range(len(numbers) + 1)]
       
        for n in numbers:
            freq_map[n] = 1 + freq_map.get(n, 0)
           
        for n, c in freq_map.items():
            freq[c].append(n)
           
        results = []
        for i in range(len(freq)- 1, 0, -1):
            for n in freq[i]:
                results.append(n)
                if len(results) == k:
                    return results
               
        return results
   
    def contains_dupes(self, numbers):
        dupe_set = set()
        freq_map = {}
       
        for num in numbers:
            if num in dupe_set:
                freq_map[num] = freq_map.get(num, 1) + 1
            else:
                dupe_set.add(num)
               
        return freq_map

    def buy_stonks(self, prices):
        lowest_price = prices[0]
        result = 0

        for price in prices:
            if price < lowest_price:
                lowest_price = price
    
            curr_price = price - lowest_price
            if curr_price > result:
                result = curr_price
            
        return result