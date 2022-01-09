#題目一
def calculate(min, max):
    a=1
    b=1
    s1=0
    s2=0
    while a<=int(max):
        s1=s1+a
        a+=1
    while b<=int(min-1):
        s2=s2+b
        b+=1
    print(s1-s2)
calculate(1, 3) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8) # 你的程式要能夠計算 4+5+6+7+8，最後印出 30

#題目二
def avg(data):
    money=0
    for i in range(data["count"]):
        money=money+data["employees"][i]["salary"]
    meanmoney=money/data["count"]
    print(meanmoney)
avg({
"count":3,
"employees":[
{
"name":"John",
"salary":30000
},
{
"name":"Bob",
"salary":60000
},
{
"name":"Jenny",
"salary":50000
}
]
}) # 呼叫 avg 函式

#題目三
def maxProduct(nums):
    d=max(nums)
    nums.remove(d)
    e=max(nums)
    nums.append(d)
    f=min(nums)
    nums.remove(f)
    g=min(nums)
    print(max(d*e,f*g))
maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([-1, -2, 0]) # 得到 2

#題目四
def twoSum(nums, target):
    for y in range(len(nums)-1):
        for z in range(y+1,len(nums)):
            if nums[y]+nums[z]==target:
                return([y,z])
result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9

#題目五
def maxZeros(nums):
    maxcount=0
    count=0
    for i in range(len(nums)):
        if nums[i]==0:
            count+=1
            maxcount=max(count,maxcount)
        else:
            count=0 
    print(maxcount)
maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
maxZeros([0, 0, 0, 1, 1]) # 得到 3