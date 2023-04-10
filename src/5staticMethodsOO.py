# I want to use this class at any time, without instacing an object
# for that, i'll create a static method:
class Math:
    # static methods don't have acces to an instance
    @staticmethod
    def add5(x):
        return x+5

    @staticmethod
    def pr():
        return "some string"

print(Math.add5(5))
print(Math.pr())