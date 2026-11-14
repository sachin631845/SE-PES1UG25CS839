from hypothesis import given, strategies as st
from attendance_eligibility_parser import normalize_srn, attendance_from_ratio, attendance_from_register

@given(st.text() | st.none())
def test_normalize_srn_no_crash(s):
    # To-Do: Using try and except complete this function.
    pass

@given(st.text() | st.none())
def test_attendance_from_ratio_no_crash(s):
    # To-Do: Using try and except complete this function.
    pass

@given(st.text() | st.none())
def test_attendance_from_register_no_crash(s):
    # To-Do: Using try and except complete this function.
    pass