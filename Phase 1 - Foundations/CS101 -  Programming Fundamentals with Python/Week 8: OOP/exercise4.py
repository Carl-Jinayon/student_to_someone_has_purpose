"""
Exercise 4 (__str__ and Guard):
Create a class Student with name and grades (list).

1. Method average() returns the average grade.
2. __str__ returns "Student: name, Average: x.x".
3. Use the if __name__ == "__main__": guard to create a student and print it.
"""

class Student:
    def __init__(self, name: str, grades: list):
        # Validate name and grades type
        if not isinstance(name, str) or not isinstance(grades, list):
            raise ValueError("Name must be a string and grades must be a list.")
        
        # Validate that ALL grades are between 0 and 100
        if not all(0 <= grade <= 100 for grade in grades):
            raise ValueError("All grades must be between 0 and 100.")

        self.name = name
        self.__grades = grades

    def __str__(self):
        return f"Student: {self.name}, Average: {self.average():.1f}"

    def average(self):
        if not self.__grades:
            return 0.0
        return sum(self.__grades) / len(self.__grades)
    
if __name__ == "__main__":
    my_student = Student("Carl Jinayon", [90,98,87,97])

    print(my_student)


# improved code:
class Student:
    def __init__(self, name: str, grades: list[int]):
        # 1. Validate Name
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string.")
        
        # 2. Validate Grades Type
        if not isinstance(grades, list):
            raise ValueError("Grades must be a list.")
        
        # 3. Validate Grade Content & Range
        for i, grade in enumerate(grades):
            if not isinstance(grade, (int, float)):
                raise ValueError(f"Grade at index {i} is not a number ({type(grade).__name__}).")
            if not 0 <= grade <= 100:
                raise ValueError(f"Grade at index {i} ({grade}) is out of range (0-100).")

        self.name = name
        # 4. Store a COPY to prevent external mutation
        self.__grades = list(grades)

    def __str__(self):
        return f"Student: {self.name}, Average: {self.average():.1f}"

    def average(self) -> float:
        if not self.__grades:
            return 0.0  # Always return float
        return sum(self.__grades) / len(self.__grades)

if __name__ == "__main__":
    try:
        my_student = Student("Carl Jinayon", [90, 98, 87, 97])
        print(my_student)
        
        # Test mutation protection
        # original_list = [100, 100]
        # s = Student("Test", original_list)
        # original_list.append(0) 
        # print(s.average()) # Still 100.0, not 66.6!
        
    except ValueError as e:
        print(f"Error: {e}")   
    
