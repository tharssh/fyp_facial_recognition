import face_recognition
import time
import xlwt

# Load the jpg files into numpy arrays
biden_image = face_recognition.load_image_file("syafiq.jpg")
obama_image = face_recognition.load_image_file("tharssh.jpg")
unknown_image = face_recognition.load_image_file("tharssh2.jpg")
#tharssh_image = face_recognition.load_image_file("maa.jpg")
john_image = face_recognition.load_image_file("john.jpg")
obama1_image = face_recognition.load_image_file("kelly.jpg")
farhana_image = face_recognition.load_image_file("farhana.jpeg")
#syafiq_image = face_recognition.load_image_file("syafiq.jpg")

# Get the face encodings for each face in each image file
# Since there could be more than one face in each image, it returns a list of encordings.
# But since I know each image only has one face, I only care about the first encoding in each image, so I grab index 0.
biden_face_encoding = face_recognition.face_encodings(biden_image)[0]
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
#tharssh_face_encoding = face_recognition.face_encodings(tharssh_image)[0]
john_face_encoding = face_recognition.face_encodings(john_image)[0]
kelly_face_encoding = face_recognition.face_encodings(obama1_image)[0]
farhana_face_encoding = face_recognition.face_encodings(farhana_image)[0]
#syafiq_face_encoding = face_recognition.face_encodings(syafiq_image)[0]

known_faces = [
    biden_face_encoding,
    obama_face_encoding,
    #tharssh_face_encoding,
    john_face_encoding,
    kelly_face_encoding,
    farhana_face_encoding,
    #syafiq_face_encoding

]

#unknown_faces = [

#]







# results is an array of True/False telling if the unknown face matched anyone in the known_faces array
results = face_recognition.compare_faces(known_faces, unknown_face_encoding)

#print("Is the unknown face a picture of Biden? {}".format(results[0]))
#print("Is the unknown face a picture of Obama? {}".format(results[1]))
#print("Is the unknown face a new person that we've never seen before? {}".format(not True in results))


#print("Is the unknown face a picture of Biden? {}".format(results[0]))
#print("Is the unknown face a picture of tharssh? {}".format(results[1]))
#print("Is the unknown face a new person that we've never seen before? {}".format(not True in results))
#print("Is the unknown face a picture of tharssh? {}".format(results[1]))

#print("Present: {}".format(results[1]))
#from pprint import pprint
#pprint(known_faces)

if results[1] == True:
    #print("Present")
    DATA = (("Attendance List", ),
           ("Tharssh", "Present",time.strftime("%c")),)

    wb = xlwt.Workbook()
    ws = wb.add_sheet("My Sheet")
    for i, row in enumerate(DATA):
        for j, col in enumerate(row):
            ws.write(i, j, col)
    ws.col(0).width = 256 * max([len(row[0]) for row in DATA])
    wb.save("attendance.xls")

else:
   #print("Absent")
   DATA = (("Attendance List", time.strftime("%c")),
           ("Tharssh", "Absent",),)

   wb = xlwt.Workbook()
   ws = wb.add_sheet("My Sheet")
   for i, row in enumerate(DATA):
       for j, col in enumerate(row):
           ws.write(i, j, col)
   ws.col(0).width = 256 * max([len(row[0]) for row in DATA])
   wb.save("attendance.xls")