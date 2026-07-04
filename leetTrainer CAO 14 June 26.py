"""
Building Algorithms for LeetTrainer App
"""

# imports
from datetime import datetime


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

    def eval_rpn(self, tokens):
        stack = []
   
        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b - a))
            elif token == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(token))

        return stack[-1]


class menu_calls:

    def two_sum_call(self):

        two_sum_array = []

        print("You selected Two Sum!\n")

        array_iterator = int(
            input("Enter amount of integers:\n")
        )

        for i in range(array_iterator):

            try:
                value = int(
                    input("Enter value: ")
                )

                two_sum_array.append(value)

            except ValueError:
                print("Invalid data type")

        try:
            target = int(
                input("Enter target value:\n")
            )

        except ValueError:
            print("Invalid target entered")
            return None

        algos = Algos()

        pairs = algos.two_sum(
            two_sum_array,
            target
        )

        if pairs:

            print(f"\nIndex Pairs: {pairs}")

            print(
                f"Value Pairs: "
                f"{[(two_sum_array[i], two_sum_array[j]) for i, j in pairs]}"
            )

        else:
            print("No valid combos found!")

        return pairs


    def binary_search_call(self):

        print("\nQueue Binary Search\n")

        user_input = get_integer_array()

        user_input.sort()

        print(
            f"\nSorted Array: "
            f"{user_input}"
        )

        try:
            target = int(
                input(
                    "Enter target value: "
                )
            )

        except ValueError:
            print("Invalid target")
            return None

        algos = Algos()

        result = algos.binary_search(
            user_input,
            target
        )

        if result != -1:

            print(
                f"Target found at index {result}"
            )

        else:
            print("Target not found")

        return result


    def valid_parenth_call(self):

        print("\nValid Parentheses Selected\n")

        parenth_string = input(
            "Enter brackets: "
        )

        algos = Algos()

        result = algos.valid_parenth(
            parenth_string
        )

        if result:
            print("Valid Parentheses")

        else:
            print("Invalid Parentheses")

        return result
   
    def sliding_window_call(self):
       
        print("\nSliding Window Selected\n")
       
        algos = Algos()
       
        # Grab user input and provide example
        print("\nProvide a string with repeating substrings\n")
        sliding_wind_str = input("Example --> 'abcabcbb' || Input Here: ")
        # Clean the string to prevent algo failure
        clean_string = sliding_wind_str.replace(" ", "").lower()
        # Store results then return a clean output
        result = algos.sliding_window(clean_string)
       
        if result:
            print("\nHere are the results for your string...\n")
            print(f"\nUser String: {sliding_wind_str}, Longest Substring Found: Length {result}\n")
        else:
            print("No Substring Found")
           
        return result
   
    def top_k_call(self):
        k = 0
       
        print("\nSliding Window Selected\n")
       
        algos = Algos()
       
        user_input = get_integer_array()
           
        k = int(input("Input the frequency you would like to search: "))
       
        result = algos.top_k_frequency(
            user_input,
            k
            )
       
        print(f"TOP K RESULTS! --> {result}")
               
        return result
   
    def contains_dupes_call(self):
        algos = Algos()
       
        user_input = get_integer_array()
       
        result = algos.contains_dupes(user_input)
               
        return result

    def buy_stonks_call(self):
        algos = Algos()
       
        user_input = get_integer_array()

        result = algos.buy_stonks(user_input)

        print("=" * 30)
        print("\tBUY / SELL STOCKS")
        print("=" * 30)
        print(f"Prices Entered: {user_input}")
        print(f"Maximum Profit: {result}")

        return result
    
    def rpn_call(self):
        tokens = []

        print("You selected Reverse Polish Notation Evaluator!\n")

        try:
            count = int(input("Enter number of tokens to input:\n"))
        except ValueError:
            print("Invalid number")
            return None
        
        for i in range(count):
            token = input(f"Enter token #{i+1} (integer or operator + - * /): ").strip()
            if token in {"+", "-", "*", "/"}:
                tokens.append(token)
            else:
                try:
                    # ensure token is an integer string
                    tokens.append(str(int(token)))
                except ValueError:
                    print("Invalid token — must be integer or one of + - * /. Please re-enter this token.")
                    # re-prompt for the same index
                    i -= 1
                    continue
        
        if not tokens:
            print("No valid tokens entered.")
            return None
        
        algos = Algos()
        try:
            result = algos.eval_rpn(tokens)
        except (IndexError, ZeroDivisionError) as e:
            print(f"Error evaluating RPN: {e}")
            return None
        
        print(f"\nTokens: {tokens}")
        print(f"RPN Result: {result}")
        
        return result
   
"""
Helper Function for Array Values
"""    
def get_integer_array():
    numbers = []
   
    stop_binary_input = "Y"
   
    print("\nProvide an array of numbers. If you wish to continue/stop input using 'Y/N'\n")
   
    while stop_binary_input == "Y" or stop_binary_input == "y":
        try:
            array_value = int(input("Provide a number for the array: "))
            numbers.append(array_value)
           
        except ValueError:
            print("Invalid Data Type...")
           
        stop_binary_input= input("Continue? (Y/N): ")
       
    return numbers
       
"""
Functions Dedicated to Touching Files
"""        
def save_results(
        user_name,
        algorithm,
        result):

    with open(
            "results.txt",
            "a") as file:

        timestamp = datetime.now()

        file.write(
            f"Date: {timestamp} | "
            f"User: {user_name} | "
            f"Algo: {algorithm} | "
            f"Result: {result}\n"
        )

def read_results():
    file = open("results.txt", "r")
    print("=" * 40)
    print("\t\tHISTORY")
    print("=" * 40)
    for line in file:
        print(line.strip())
           
    file.close()

def return_latest():
    file = open("results.txt", "r")
    latest_entry = file.readlines()
    print("=" * 30)
    print("\tLATEST ENTRY...")
    print("=" * 30)
    if latest_entry:
        print(latest_entry[-1].strip())
    else:
        print("No history found.")
   
def view_statistics():
    from collections import Counter
    algo_count = Counter()
    with open("results.txt", "r") as file:
        for raw in file:
            line = raw.strip()
            if not line:
                continue
            parts = [p.strip() for p in line.split("|")]
            # require at least Date | User | Algo | Result
            if len(parts) < 4:
                continue
            algo_part = parts[2]
            if ":" in algo_part:
                algorithm = algo_part.split(":", 1)[1].strip()
            else:
                algorithm = algo_part.strip()
            if algorithm:
                algo_count[algorithm] += 1
       
        print("=" * 30)
        print("\tSTATISTICS")
        print("=" * 30)
       
        for algo, c in algo_count.items():
            print(f"Algo: {algo}, Algo Count: {c}\n")


def menu():

    menu_call = menu_calls()

    user_name = input(
        "Welcome to LeetTrainer!\n"
        "Enter your full name:\n"
    )

    print("=" * 40)

    print(
        f"\nHi {user_name}, "
        f"welcome to LeetTrainer!"
    )

    while True:

        print("\nSelect Algorithm:\n")

        print(
            "1. Two Sum\n"
            "2. Binary Search\n"
            "3. Valid Parentheses\n"
            "4. Test Sliding Window\n"
            "5. Top K Frequent Element\n"
            "6. Contains Duplicates\n"
            "7. Buy/Sell Stocks\n"
            "8. Evaluate Reverse Polish Notation\n"
            "9. Read Back Results\n"
            "10. Return Latest Log\n"
            "11. Run Analytics\n"
            "E. Exit"
        )

        user_selection = (
            input(
                "\nEnter selection: "
            )
            .strip()
            .upper()
        )

        if user_selection == "1":

            result = (
                menu_call
                .two_sum_call()
            )

            save_results(
                user_name,
                "Two Sum",
                result
            )

        elif user_selection == "2":

            result = (
                menu_call
                .binary_search_call()
            )

            save_results(
                user_name,
                "Binary Search",
                result
            )

        elif user_selection == "3":

            result = (
                menu_call
                .valid_parenth_call()
            )

            save_results(
                user_name,
                "Valid Parentheses",
                result
            )
           
        elif user_selection == "4":
            result = (
                menu_call
                .sliding_window_call()
                )
           
            save_results(
                user_name,
                "Longest Substring",
                result
                )
           
        elif user_selection == "5":
            result = (
                menu_call
                .top_k_call()
                )
           
            save_results(
                user_name,
                "Top K Element",
                result
                )
           
        elif user_selection == "6":
            result = (
                menu_call  
                .contains_dupes_call()
                )
           
            if result:
                formatted = " | ".join(f"Value: {n}, Count: {c}" for n, c in result.items())
            else:
                formatted = "No duplicates"
           
            save_results(
                user_name,
                "Contains Duplicates",
                formatted
                )

        elif user_selection == "7":
            result = (
                menu_call  
                .buy_stonks_call()
                )
           
            save_results(
                user_name,
                "Buy Stocks",
                result
                )

        elif user_selection == "8":
            print("RPN Mapping")
            result = (
                menu_call  
                .rpn_call()
                )
           
            save_results(
                user_name,
                "Reverse Polsih Notation",
                result
                )

        elif user_selection == "9":
            read_results()

        elif user_selection == "10":
            return_latest()
           
        elif user_selection == "11":
            view_statistics()

        elif user_selection == "E":

            print("\nGoodbye!")

            break

        else:

            print(
                "\nInvalid Option\n"
            )


menu()