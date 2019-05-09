Eng_Marks=int(input(("enter your english marks: ")))
Urd_Marks=int(input(("enter your urdu marks: ")))
Phy_Marks=int(input(("enter your physics marks: ")))
Mat_Marks=int(input(("enter your maths marks: ")))
Isl_Marks=int(input(("enter your islamiat marks: ")))
Obt_Marks= Eng_Marks+Urd_Marks+Phy_Marks+Mat_Marks+Isl_Marks
Per= float(Obt_Marks)/5
if Per>40 and Per<50:
    print("**Congratulations!** Your Grade is D & Your Marks is: "+str(Obt_Marks)+" & Your Percentage is: "+str(Per)+"%")
elif Per>50 and Per<60:
    print("**Congratulations!** Your Grade is C & Your Marks is: "+str(Obt_Marks)+" & Your Percentage is: "+str(Per)+"%")
elif Per>60 and Per<70:
    print("**Congratulations!** Your Grade is B & Your Marks is: "+str(Obt_Marks)+" & Your Percentage is: "+str(Per)+"%")
elif Per>70 and Per<80:
    print("**Congratulations!** Your Grade is A & Your Marks is: "+str(Obt_Marks)+" & Your Percentage is: "+str(Per)+"%")
elif Per>80:
    print("**Congratulations!** Your Grade is A+ & Your Marks is: "+str(Obt_Marks)+" & Your Percentage is: "+str(Per)+"%")
elif Per<30:
    print("**fail!** sorry you can't made it try again in next exam. Your Percentage is: "+str(Per)+"%")