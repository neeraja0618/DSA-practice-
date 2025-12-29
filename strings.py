#counting character
s="pretty"
count=0
for i in s:
  count++1
print("length of string:",count)

#check palindrome 
s = "madam"
is_palindrome = True
for i in range(len(s) // 2):
    if s[i] != s[-i - 1]:
        is_palindrome = False
        break
if is_palindrome:
    print("Palindrome")
else:
    print("Not Palindrome")

#first non repeating charac 
s="swiss"
for char in s:
  if s.count(char)==1:
    print("first non repeating character:",char)
    break 
