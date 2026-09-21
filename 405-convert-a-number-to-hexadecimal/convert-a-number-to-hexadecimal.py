class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        
        # Convert negative integer to 32-bit two's complement representation
        if num < 0:
            num += (1 << 32)
            
        hex_chars = "0123456789abcdef"
        result = []
        
        # Extract 4 bits at a time
        while num > 0:
            digit = num & 15  # num % 16
            result.append(hex_chars[digit])
            num >>= 4         # num // 16
            
        # The digits are extracted from least significant to most, so reverse them
        return "".join(reversed(result))