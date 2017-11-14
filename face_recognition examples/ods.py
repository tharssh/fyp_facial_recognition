import face_recognition
import xlwt
import time

DATA = (("Attendance List",time.strftime("%c")),
        ("Tharssh", "Present",),)


wb = xlwt.Workbook()
ws = wb.add_sheet("My Sheet")
for i, row in enumerate(DATA):
    for j, col in enumerate(row):
        ws.write(i, j, col)
ws.col(0).width = 256 * max([len(row[0]) for row in DATA])
wb.save("attendance.xls")
