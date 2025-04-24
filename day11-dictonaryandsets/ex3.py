room={"CS101":3004,
"CS102":4501,
"CS103":6755,
"NT110":1244,
"CM241":1411}

instructor={"CS101":"Haynes",
"CS102":"Alvarado",
"CS103":"Rich",
"NT110":"Burke",
"CM241":"Lee"}

meeting_time={"CS101":"8:00 a.m",
"CS102":"9:00 a.m",
"CS103":"10:00 a.m",
"NT110":"11:00 a.m",
"CM241":"1:00 p.m"}

course_no=input("Enter a room number: ")
course_no=course_no.upper()
if course_no in room.keys():
    print(f"Room number: {room[course_no]}")
    print(f"Instructor: {instructor[course_no]}")
    print(f"Meeting time: {meeting_time[course_no]}")
else:
    print("Room not found")