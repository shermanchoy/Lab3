import lab2.bmi as bmi 
def test_bmi_under_weight():
    result = bmi.calculate_bmi(1.75, 50)
    assert result == -1, "Expected -1 for underweight"

def test_bmi_normal_weight():
    result = bmi.calculate_bmi(1.75, 70)
    assert result == 0, "Expected 0 for normal weight"

def test_bmi_over_weight():
    result = bmi.calculate_bmi(1.75, 90)
    assert result == 1, "Expected 1 for overweight"
