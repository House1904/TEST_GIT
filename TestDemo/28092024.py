class SampleClass:
    class_attr = 100

    def __init__(self, instance_attr):
        self.instance_attr = instance_attr

    def method(self):
        print(f"Class attribute: {self.class_attr}")
        print(f"Instance attribute: {self.instance_attr}")

print(SampleClass.class_attr)
print(SampleClass.__dict__) # xuất ra tất cả các thuộc tính sẵn có của SampleClass
print(SampleClass.__dict__["class_attr"]) # truy cập vào giá trị thuộc tính