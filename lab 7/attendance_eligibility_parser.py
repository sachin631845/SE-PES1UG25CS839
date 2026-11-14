
def normalize_srn(srn):
    """
    Trims spaces and converts the SRN to uppercase.
    Handles invalid inputs safely.
    """
    if not isinstance(srn, str):
        return ""

    return ''.join(srn.split()).upper()


def attendance_from_ratio(text):
    """
    Calculates attendance percentage from ATTENDED/HELD.
    Handles invalid ratios, zero denominator and unexpected inputs.
    """
    if not isinstance(text, str):
        return 0

    try:
        parts = text.split('/')

        if len(parts) != 2:
            return 0

        attended = int(parts[0].strip())
        held = int(parts[1].strip())

        if attended < 0 or held <= 0 or attended > held:
            return 0

        return attended * 100 // held

    except (ValueError, TypeError):
        return 0


def attendance_from_register(marks):
    """
    Calculates attendance percentage using P (Present)
    and A (Absent).
    Handles empty strings and invalid characters safely.
    """
    if not isinstance(marks, str):
        return 0

    marks = marks.strip().upper()

    if not marks:
        return 0

    if any(char not in "PA" for char in marks):
        return 0

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
