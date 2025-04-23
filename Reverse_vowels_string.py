class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        s_list = list(s)
        
        # First pass: collect all vowels
        vowel_stack = [char for char in s_list if char in vowels]
        
        # Second pass: replace vowels from the end of the stack
        for i in range(len(s_list)):
            if s_list[i] in vowels:
                s_list[i] = vowel_stack.pop()
        
        return ''.join(s_list)
