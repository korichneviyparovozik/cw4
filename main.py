# # class Computer:
#     def __init__(self):
#         super().__init__()
#         self.memory = 128
#
#
# class Display:
#     def __init__(self):
#         super().__init__()
#         self.resolution = "4K"
# 0
#
# class Phone(Computer, Display):
#     def print_info(self):
#         print(self.memory)
#         print(self.resolution)
#
#
# iphone = Phone()
# iphone.print_info()
try:
    a = int(input('A '))
    c = 10
    x = c / a
    print(f"X {x}")
except ZeroDivisionError:
    x = c / 1
    print(f"Except Zero {x}")
except ValueError:
    print("Its not a num")
else:

