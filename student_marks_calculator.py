name=input("enter student name")
s1=int(input("enter marks1:"))
s2=int(input("enter marks2:"))
s3=int(input("enter marks3:"))
total=(s1+s2+s3)
avg=total/3
if avg>=90:
       GRADE="A"
elif avg>=70:
       GRADE="B" 
elif avg>=50:
       GRADE="C"
else:
       GRADE="FAIL"      
print(f"\nStudent Name: {name}")
print(f"Total Marks: {total}")
print(f"Average Marks: {avg}")
print(f"Grade: {GRADE}")       

