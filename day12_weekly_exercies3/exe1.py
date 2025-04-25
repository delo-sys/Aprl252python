from random import randint 
countries= ["Algeria","Angola","Benin","Botswana","Burundi","Burkina Faso","Cameroon",
"Cape Verde","Central African Republic","Chad","Comoros","Cote d’Ivoire","DR Congo","Djibouti",
"Egypt","Equatorial Guinea","Eritrea","Ethiopia","Gabon","Gambia","Ghana","Guinea",
"Guinea-Bissau","Kenya","Lesotho","Liberia","Libya","Madagascar","Malawi","Mali","Mauritania",
"Mauritius","Morocco","Mozambique","Namibia","Niger","Nigeria","Republic of the Congo","Réunion",
"Rwanda","São Tomé and Principe","Senegal","Seychelles","Sierra Leone","Somalia","South Africa","South Sudan",
"Sudan","Swaziland","Tanzania","Togo","Tunisia","Uganda","Zambia","Zimbabwe"]


cities= ["Algiers","Luanda","Porto-Novo","Gaborone","Bujumbura","Ouagadougou","Yaoundé","Praia","Bangui","N’Djamena","Moroni","Yamoussoukro","Kinshasa","Djibouti City",
        "Cairo","Malabo","Asmara", "Addis Ababa","Libreville","Banjul","Accra","Conakry","Bissau","Nairobi","Maseru","Monrovia","Tripoli","Antananarivo","Lilongwe","Bamako","Nouakchott", "Port Louis","Rabat","Maputo","Windhoek","Niamey", "Abuja","Brazzaville","Saint-Denis",
        "Kigali","São Tomé","Dakar","Victoria","Freetown","Mogadishu","Pretoria","Juba",
    "Khartoum","Mbabane","Dodoma","Lome","Tunis","Kampala","Lusaka","Harare"]

qn="What is the capital city of "

for counter in range (1,6):
    rand=randint(0, len(countries)-1)
    print (qn+" "+countries[rand])
    ans=input()
    if (ans.upper==cities[rand].upper()):
        print("correct")
    else:
        print("incorrect")
        print("The correct answer is " + cities[rand])
