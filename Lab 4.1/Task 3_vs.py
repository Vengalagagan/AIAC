def parse_student_info(student_dict):
    full_name = student_dict['name']['first'] + " " + student_dict['name']['last']
    branch = student_dict['academic']['branch']
    sgpa = int(float(student_dict['academic']['sgpa']))
    print("Student Details:")
    print(f"• Full Name: {full_name}")
    print(f"• Branch: {branch}")
    print(f"• SGPA:{sgpa}")

def get_student_input():
    first = input("First Name: ")
    last = input("Last Name: ")
    branch = input("Branch: ")
    sgpa = input("SGPA: ")
    student = {
        'name': {
            'first': first,
            'last': last
        },
        'academic': {
            'branch': branch,
            'sgpa': sgpa
        }
    }
    return student

if __name__ == "__main__":
    student_info = get_student_input()
    parse_student_info(student_info)