# Атрибуты класса

class Comment:
    count = 0

    def __int__(self, text):
        self.text = text

    def upcount(self):
        self.count += 1


my_comment = Comment()

my_comment.upcount()
print(my_comment.count)
# print(my_comment.__dict__)
#
# my_comment.count = 17
# print(my_comment.count)
# print(Comment.count)
# print(Comment.__dict__)
