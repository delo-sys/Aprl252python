from random import randint
from tkinter import *
from tkinter import messagebox
countries= ["Algeria","Angola","Benin","Botswana","Burundi","Burkina Faso","Cameroon","Cape Verde","Central African Republic","Chad","Comoros","Cote d’Ivoire","DR Congo","Djibouti","Egypt","Equatorial Guinea","Eritrea","Ethiopia","Gabon","Gambia","Ghana","Guinea","Guinea-Bissau","Kenya","Lesotho","Liberia","Libya","Madagascar","Malawi","Mali","Mauritania","Mauritius","Morocco","Mozambique","Namibia","Niger","Nigeria","Republic of the Congo","Réunion","Rwanda","São Tomé and Principe","Senegal","Seychelles","Sierra Leone","Somalia","South Africa","South Sudan","Sudan","Swaziland","Tanzania","Togo","Tunisia","Uganda","Zambia","Zimbabwe"]

cities= ["Algiers","Luanda","Porto-Novo","Gaborone","Bujumbura","Ouagadougou","Yaoundé","Praia","Bangui","N’Djamena","Moroni","Yamoussoukro","Kinshasa","Djibouti City","Cairo","Malabo","Asmara", "Addis Ababa","Libreville","Banjul","Accra","Conakry","Bissau","Nairobi","Maseru","Monrovia","Tripoli","Antananarivo","Lilongwe","Bamako","Nouakchott", "Port Louis","Rabat","Maputo","Windhoek","Niamey", "Abuja","Brazzaville","Saint-Denis","Kigali","São Tomé","Dakar","Victoria","Freetown","Mogadishu","Pretoria","Juba","Khartoum","Mbabane","Dodoma","Lome","Tunis","Kampala","Lusaka","Harare"]

# qn="What is the capital city of "


# rand=randint(0, len(countries)-1)
# print (qn+" "+countries[rand])
# ans=input()
# if (ans.upper==cities[rand].upper()):
#     print("correct")
# else:
#     print("incorrect")
# print("The correct answer is " + cities[rand])


root = Tk()
question=StringVar()
def generateQn():
    qn="What is the capital city of "
    rand=randint(0,len(countries)-1)
    qn=+" "+countries[rand]
    question.set(qn)

lblquestion=Label(root,textvariable=question)
lblquestion.grid(row=0,column=0,)

lblanswer=Label(root,text="Enter your answer")
lblanswer.grid(row=1,column=0,)

btnquiz=Button(root,text="Another Question",command=lambda:question.set("What is the capital city of "+countries[randint(0, len(countries)-1)]))
btnquiz.grid(row=0,column=1,)

# btnanswer=Button(root,text="Check answer",command=lambda:messagebox.showinfo("Answer",f"Correct answer is {cities[countries.index(question.get().split()[-1])]}"))
# btnanswer.grid(row=1,column=2,)

txtanswer=Entry(root)
txtanswer.grid(row=1,column=1,pady=10)

def checkAnswer():
    ans=txtanswer.get()
    if (ans.upper()==cities[countries.index(question.get().split()[-1])].upper()):
        messagebox.showinfo("Answer","Correct")
    else:
        messagebox.showinfo("Answer","Incorrect")
        messagebox.showinfo("Correct Answer",f"Correct answer is {cities[countries.index(question.get().split()[-1])]}")
btncheck=Button(root,text="Check Answer",command=checkAnswer)
btncheck.grid(row=2,column=1,pady=10)

root.mainloop()