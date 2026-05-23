name=input("enter student name")
s1=int(input("enter marks1:"))
s2=int(input("enter marks2:"))
s3=int(input("enter marks3:"))
if s1>100 or s2>100 or s3>100:
       print("Invalid marks entered")
else:       
    total=(s1+s2+s3)
    avg=total/3
    if avg>=90:
       grade="A"
    elif avg>=70:
       grade="B" 
    elif avg>=50:
       grade="C"
    else:
       grade="FAIL"      
    print(f"\nStudent Name: {name}")
    print(f"Total Marks: {total}")
    print(f"Average Marks: {avg:.2f}")
    print(f"Grade: {grade}")       

