class Grade:
    def __init__(self, nilai):
        self.nilai = nilai
    
    def grade(self):
        if self.nilai < 80 or self.nilai == 100:
            print("Grade A")
        elif self.nilai < 71 or self.nilai > 80:
            print("Grade B+")
        elif self.nilai < 61 or self.nilai > 71:
            print("Grade B")
        elif self.nilai < 50 or self.nilai > 60:
            print("Grade C")
        elif self.nilai < 40 or self.nilai > 50:
            print("Grade D")
        else:
            print("Grade E")

def main():
    nilai = int(input("Masukkan nilai : "))

    grade = Grade(nilai)

    grade_nilai = grade.grade()

    print(grade_nilai)


main()