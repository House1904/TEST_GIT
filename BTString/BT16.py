def longest_substring_with_all_characters(s):
    unique_characters = set(s)
    unique_count = len(unique_characters)  

    n = len(s)
    longest_substring = ""
    
    for i in range(n):
        current_chars = set()  
        for j in range(i, n):
            current_chars.add(s[j])
            if (len(current_chars) == unique_count): 
                current_substring = s[i:j+1]  
                if (len(current_substring) > len(longest_substring)):
                    longest_substring = current_substring 
                break 

    return longest_substring

def main():
    input_string = input("Nhập chuỗi ký tự: ")
    result = longest_substring_with_all_characters(input_string)
    print(f"Xâu con dài nhất chứa tất cả các ký tự trong chuỗi là: '{result}'")

if __name__ == "__main__":
    main()
