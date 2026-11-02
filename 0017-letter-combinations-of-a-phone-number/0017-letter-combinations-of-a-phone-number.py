class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        current_path = []
        result = []

        def traverse(i : int, current_path: list[str], result: list[list[str]]):

            if len(current_path) == len(digits):
                result.append("".join(current_path))
                return
            
            alphabets = phone_map[digits[i]]

            for ch in alphabets:
                current_path.append(ch)
                traverse(i+1, current_path, result)

                current_path.pop()
            
        traverse(0, current_path, result)
        return result


            

        