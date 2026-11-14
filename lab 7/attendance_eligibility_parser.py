def normalize_srn(srn):
    """
    Trims and upper-cases a student registration number.
    Assumes srn is a non-empty string.
    """
    return srn.strip().replace(' ', '').upper()

def attendance_from_ratio(text):
    """
    Converts 'ATTENDED/HELD' into a whole-number percentage.
    Assumes both values are whole numbers and HELD is not zero.
    """
    attended, held = text.split('/')
    return int(attended) * 100 // int(held)

def attendance_from_register(marks):
    """
    Works out the attendance percentage from a string of P (present) and A (absent).
    Assumes marks has at least one character.
    """
    marks = marks.strip().upper()
    return marks.count('P') * 100 // len(marks)

def main():
    print("==== Running normalize_srn ====")
    value = input("Enter an SRN (e.g. pes1ug23cs001): ")
    print("Normalized SRN:", normalize_srn(value))

    print("\n==== Running attendance_from_ratio ====")
    value = input("Enter classes attended and held as ATTENDED/HELD (e.g. 30/40): ")
    print("Attendance percent:", attendance_from_ratio(value))

    print("\n==== Running attendance_from_register ====")
    value = input("Enter the register as P/A marks (e.g. PPAPP): ")
    print("Attendance percent:", attendance_from_register(value))

if __name__ == "__main__":
    main()
