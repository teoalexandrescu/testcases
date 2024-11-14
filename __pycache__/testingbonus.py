import unittest

class Student:
    def __init__(self, student_id, name, age, major):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.major = major

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Major: {self.major}"

class StudentRegistrationSystem:
    def __init__(self):
        self.students = {}

    # CREATE
    def create_student(self, student_id, name, age, major):
        if student_id in self.students:
            print("Student with this ID already exists.")
            return False
        else:
            self.students[student_id] = Student(student_id, name, age, major)
            print("Student created successfully.")
            return True

    # READ
    def read_student(self, student_id):
        if student_id in self.students:
            print(str(self.students[student_id]) + "\n")
            return student_id
        else:
            print("Student not found.")

    def read_all_students(self):
        if not self.students:
            print("No students registered.")
            return []
        else:
            for student in self.students.values():
                print(str(student))
            return self.students.values()

    # UPDATE
    def update_student(self, student_id, name=None, age=None, major=None):
        if student_id in self.students:
            student = self.students[student_id]
            if name:
                student.name = name
            if age:
                student.age = age
            if major:
                student.major = major
            print("Student updated successfully.")
            return True
        else:
            print("Student not found.")
            return False

    # DELETE
    def delete_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            print("Student deleted successfully.")
            return True
        else:
            print("Student not found.")
            return False


class TestStudentRegistration(unittest.TestCase):
    def setUp(self):
        self.registration = StudentRegistrationSystem()

    def test_create_student1(self):
        print("Test #1: Create.")
        self.assertTrue(self.registration.create_student(student_id=123432, name="Tom", age=18, major="Electrical Engineering"))  
        self.assertIn(123432, self.registration.students)  
        
    def test_create_student2(self):
        print("Test #2: Create.")
        self.assertTrue(self.registration.create_student(student_id=546777, name="", age=21, major="Astronomy"))
        self.assertEqual(self.registration.students[546777].name, "")

    def test_create_student3(self):
        print("Test #3: Create.")
        self.assertTrue(self.registration.create_student(student_id=123432, name="Tom", age=18, major="Electrical Engineering"))
        self.assertFalse(self.registration.create_student(student_id=123432, name="Mary", age=15, major="Bio"))

    def test_create_student4(self):
        print("Test #4: Create.")
        self.assertTrue(self.registration.create_student(student_id=123456, name="A", age=19, major=""))  
        self.assertEqual(self.registration.students[123456].name, "A")
        self.assertEqual(self.registration.students[123456].age, 19)  
        self.assertEqual(self.registration.students[123456].major, "")  

    def test_create_student5(self):
        print("Test #5: Create.")
        self.assertTrue(self.registration.create_student(
            student_id=12222222223231231232131232131233456,
            name="Abbbbcccccddddddeeeeeefffffgggggghhhhiiii",
            age=200,
            major="Computerscienceenvirmentalengineeringelectricalmechanical"
        ))  
        self.assertEqual(self.registration.students[12222222223231231232131232131233456].name, "Abbbbcccccddddddeeeeeefffffgggggghhhhiiii")
        self.assertEqual(self.registration.students[12222222223231231232131232131233456].age, 200)
        self.assertEqual(self.registration.students[12222222223231231232131232131233456].major, "Computerscienceenvirmentalengineeringelectricalmechanical")

    def test_create_student6(self):
        print("Test #6: Create.")
        self.registration.create_student(student_id=322444, name="Allen", age=18, major="Computer Science")
        self.assertFalse(self.registration.create_student(student_id=322444, name="Ana", age=21, major="Math"))
        self.assertEqual(self.registration.students[322444].age, 18)

    def test_read_student1(self):
        print("Test #1: Read.")
        self.registration.create_student(student_id=123432, name="Tom", age=18, major="Electrical Engineering")
        self.assertEqual(self.registration.read_student(student_id=123432), 123432)

    def test_read_student2(self):
        print("Test #2: Read.")
        self.assertIsNone(self.registration.read_student(student_id=987765))

    def test_read_student3(self):
        print("Test #3: Read.")
        self.registration.create_student(student_id=453322, name="Ana", age=21, major="Math")
        self.assertEqual(self.registration.read_student(student_id=453322), self.registration.read_student(student_id=453322))

    def test_read_all1(self):
        print("Test #1: Read all.")
        self.assertEqual(self.registration.read_all_students(), [])
   
    def test_read_all2(self):
        print("Test #2: Read all.")
        self.registration.create_student(student_id=123432, name="Tom", age=18, major="Electrical Engineering")
        self.registration.create_student(student_id=987654, name="Mary", age=21, major="Bio")
        self.registration.create_student(student_id=543216, name="Ana", age=19, major="Math")
        result = list(self.registration.read_all_students())        
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].name, "Tom")
        self.assertEqual(result[1].name, "Mary")
        self.assertEqual(result[2].name, "Ana")

    def test_update1(self):
        print("Test #1: Update.")
        self.registration.create_student(student_id=54321, name="Emma", age=22, major="Math")       
        self.assertTrue(self.registration.update_student(student_id=54321, name="Emily", age=23, major="Bio"))
        self.assertEqual(self.registration.students[54321].name, "Emily")
        self.assertEqual(self.registration.students[54321].age, 23)
        self.assertEqual(self.registration.students[54321].major, "Bio")

    def test_update2(self):
        print("Test #2: Update.")
        self.assertFalse(self.registration.update_student(student_id=123454, name="Karol"))

    def test_delete1(self):
        print("Test #1: Delete.")
        self.registration.create_student(student_id=123456, name="Tom", age=18, major="Electrical Engineering")
        self.assertTrue(self.registration.delete_student(student_id=123456))  
        self.assertNotIn(123456, self.registration.students)
    
    def test_delete2(self):
        print("Test #2: Delete.")
        self.registration.create_student(student_id=123456, name="Tom", age=18, major="Electrical Engineering")
        self.registration.students.clear() 
        self.assertFalse(self.registration.delete_student(student_id=123456))  

    def test_delete3(self):
        print("Test #3: Delete.")
        self.assertFalse(self.registration.delete_student(student_id=876555))
 

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestStudentRegistration('test_create_student1'))
    suite.addTest(TestStudentRegistration('test_create_student2'))
    suite.addTest(TestStudentRegistration('test_create_student3'))
    suite.addTest(TestStudentRegistration('test_create_student4'))
    suite.addTest(TestStudentRegistration('test_create_student5'))
    suite.addTest(TestStudentRegistration('test_create_student6'))
    suite.addTest(TestStudentRegistration('test_read_student1'))
    suite.addTest(TestStudentRegistration('test_read_student2'))
    suite.addTest(TestStudentRegistration('test_read_student3'))
    suite.addTest(TestStudentRegistration('test_read_all1'))
    suite.addTest(TestStudentRegistration('test_read_all2'))
    suite.addTest(TestStudentRegistration('test_update1'))
    suite.addTest(TestStudentRegistration('test_update2'))
    suite.addTest(TestStudentRegistration('test_delete1'))
    suite.addTest(TestStudentRegistration('test_delete2'))
    suite.addTest(TestStudentRegistration('test_delete3'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())