# Bảng ánh xạ ký tự sang mã Morse
morse_code_dict = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',
    'E': '.',     'F': '..-.',  'G': '--.',   'H': '....',
    'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',   'P': '.--.',
    'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.'
}

# Nhập chuỗi từ người dùng
input_string = input("Nhập chuỗi ký tự (chỉ chấp nhận chữ cái và số): ").upper()

# Khởi tạo danh sách để lưu mã Morse
morse_code = []

# Dịch từng ký tự sang mã Morse
for char in input_string:
    if char in morse_code_dict:  # Kiểm tra ký tự có trong bảng ánh xạ không
        morse_code.append(morse_code_dict[char])  # Thêm mã Morse vào danh sách

# Nối các mã Morse với khoảng trắng giữa chúng
morse_string = ' '.join(morse_code)

# In ra kết quả
print("Mã Morse tương ứng là:", morse_string)
