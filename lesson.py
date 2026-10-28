marks = [50,80,100]
student ={ "name":"sid","marks":marks}

def avg(nums):
    return sum(nums) / len(nums)

for m in student["marks"]:
    if m >=80:
        print( m , "is good")

print ( student["name"], round(avg(marks),2))

print("Day 1 coding complete!")