import subprocess

def test_lesson_04():
    result = subprocess.run(['python3', 'lesson_04.py'], capture_output=True, text=True)
    output = result.stdout.strip().splitlines()

    assert output[0] == "1", f"Failed TODO 1: {output[0]}"
    assert output[1].startswith("Index"), f"Failed TODO 2: {output[1]}"
    assert output[2] == "10", f"Failed TODO 3: {output[2]}"
    assert output[3].startswith("1 x 2 ="), f"Failed TODO 4: {output[3]}"
    assert output[4] == "1", f"Failed TODO 5: {output[4]}"
    assert "break" in output[5], f"Failed TODO 6: {output[5]}"
    assert "continue" in output[6], f"Failed TODO 7: {output[6]}"
    assert output[7].startswith("Hello"), f"Failed TODO 8: {output[7]}"
    assert "Alice" in output[8], f"Failed TODO 9: {output[8]}"
    assert "fixed" in output[9], f"Failed TODO 10: {output[9]}"

    print("Lesson 4: All tests passed!")

if __name__ == "__main__":
    test_lesson_04()
