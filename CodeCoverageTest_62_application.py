import pytest
from attendance_eligibility import attendance_percent, exam_eligibility, attendance_warning


def test_plain_percent():
    assert attendance_percent(30, 40, 0) == 75


def test_invalid_total():
    with pytest.raises(ValueError, match="invalid total"):
        attendance_percent(10, 0, 0)


def test_invalid_attended_count():
    with pytest.raises(ValueError, match="invalid attended"):
        attendance_percent(-1, 40, 0)
    with pytest.raises(ValueError, match="invalid attended"):
        attendance_percent(41, 40, 0)


def test_medical_leave_capped_at_five_days():
    assert attendance_percent(20, 40, 8) == 62


def test_credited_attendance_capped_at_total():
    assert attendance_percent(38, 40, 5) == 100


def test_fees_pending():
    assert exam_eligibility(90, True, False) == "fees pending"


def test_eligible():
    assert exam_eligibility(80, False, True) == "eligible"


def test_condonation_required():
    assert exam_eligibility(70, False, True) == "condonation required"


def test_condonation_makes_student_eligible():
    assert exam_eligibility(70, True, True) == "eligible"


def test_detained():
    assert exam_eligibility(60, True, True) == "detained"


def test_no_warning_at_eighty_five_or_above():
    assert attendance_warning(85, 2) is None


def test_critical_warning():
    assert attendance_warning(70, 5) == "critical"


def test_final_notice():
    assert attendance_warning(70, 4) == "final notice"


def test_reminder():
    assert attendance_warning(80, 2) == "reminder"