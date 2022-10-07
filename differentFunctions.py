class differentFunctions():
    def Subfields():
        print("Sub-fields in AI are:")
        print("Machine Learning")
        print("Neural Networks")
        print("Vision")
        print("Robotics")
        print("Speech Processing")
        print("Natural Language Processing")
    def OddEven():
        num=int(input("Enter a number:"))
        if((num%2)==0):
            print(num,"is Even number") 
        else:
            print(num,"is Odd number")
    def Elegible():
        gender=input("Your Gender:")
        age=int(input("Your Age:"))
        if(gender=="Male"):
            if(age<21):
                print("Not Eligible")
            else:
                print("Eligible")
        else:
            if(age<18):
                print("Not Eligible")
            else:
                print("Eligible") 
    def percentage():
        sub1=int(input("Subject1="))
        sub2=int(input("Subject2="))
        sub3=int(input("Subject3="))
        sub4=int(input("Subject4="))
        sub5=int(input("Subject5="))
        total=sub1+sub2+sub3+sub4+sub5
        print("Total :",total)
        print("Percentage :{0:.9f}".format(total/5))
    def triangle():
        hgt=int(input("Height :"))
        bdh=int(input("Breadth :"))
        print("Area of Triangle :",(hgt*bdh)/2)
        hgt1=int(input("Height1 :"))
        hgt2=int(input("Height2 :"))
        bdh1=int(input("Breadth :"))
        print("Perimeter of Triangle :",hgt1+hgt2+bdh1)