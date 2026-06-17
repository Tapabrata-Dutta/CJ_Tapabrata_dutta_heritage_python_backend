
class GradeFinder: 

    def __init__(self, students): 

        self.students = students   # list of dicts 

  

    def find_by_name(self, name): 

        """O(n) — linear search by name""" 

        for s in self.students: 

            if s['name'].lower() == name.lower(): 

                return s 

        return None 

  

    def find_by_roll(self, roll): 

        """O(n) — linear search by roll number""" 

        for s in self.students: 

            if s['roll'] == roll: 

                return s 

        return None 

  

    def find_above_grade(self, threshold): 

        """O(n) — find all students above a grade""" 

        return [s for s in self.students if s['grade'] >= threshold] 

  

    def find_topper(self): 

        """O(n) — linear scan for maximum grade""" 

        return max(self.students, key=lambda s: s['grade']) 

  

  

# Dataset 

students = [ 

    {'roll': 101, 'name': 'Arjun',   'grade': 88}, 

    {'roll': 102, 'name': 'Priya',   'grade': 95}, 

    {'roll': 103, 'name': 'Rahul',   'grade': 72}, 

    {'roll': 104, 'name': 'Sneha',   'grade': 91}, 

    {'roll': 105, 'name': 'Vikram',  'grade': 68}, 

    {'roll': 106, 'name': 'Deepika', 'grade': 84}, 

]  

gf = GradeFinder(students) 

print(gf.find_by_name('priya'))    

print(gf.find_by_roll(104))             

print(gf.find_above_grade(85))          

print(gf.find_topper())                 

