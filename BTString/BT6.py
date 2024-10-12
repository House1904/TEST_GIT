def lowerandupper(s):
	s = " ".join(s.strip().split())
	result_string = ""
	for char in s:
		if (char.isupper()):
			result_string += char.lower()
		else:
			result_string += char.upper()
	return result_string
def main():
	s = input("Nhập chuỗi cần xử lí: ")
	print(f"Chuỗi sau khi xử lí chữ hoa và chữ thường: {lowerandupper(s)}")

if __name__ == "__main__":
    main()