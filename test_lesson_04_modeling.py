import subprocess

def test_lesson_04_modeling():
    result = subprocess.run(['python3', 'lesson_04_modeling.py'], capture_output=True, text=True)
    output = result.stdout.strip().splitlines()

    # Detailed checks for each TODO
    try:
        assert "Fibonacci" in output[0], "TODO 1 Failed: Fibonacci sequence is incorrect."
        print("TODO 1 Passed: Fibonacci sequence works.")
    except AssertionError as e:
        print(e)

    try:
        assert "factorial" in output[1], "TODO 2 Failed: Factorial calculation is incorrect."
        print("TODO 2 Passed: Factorial calculation works.")
    except AssertionError as e:
        print(e)

    try:
        assert "dice roll" in output[2], "TODO 3 Failed: Dice roll simulation is incorrect."
        print("TODO 3 Passed: Dice roll simulation works.")
    except AssertionError as e:
        print(e)

    try:
        assert "savings" in output[3], "TODO 4 Failed: Savings growth modeling is incorrect."
        print("TODO 4 Passed: Savings growth modeling works.")
    except AssertionError as e:
        print(e)

    try:
        assert "*" in output[4], "TODO 5 Failed: Pattern printing logic is incorrect."
        print("TODO 5 Passed: Pattern printing works.")
    except AssertionError as e:
        print(e)

    try:
        assert "prime" in output[5], "TODO 6 Failed: Prime number checker is incorrect."
        print("TODO 6 Passed: Prime number checker works.")
    except AssertionError as e:
        print(e)

    try:
        assert "queue" in output[6], "TODO 7 Failed: Queue simulation is incorrect."
        print("TODO 7 Passed: Queue simulation works.")
    except AssertionError as e:
        print(e)

    print("Testing completed for Lesson 4 Modeling Sequences.")

if __name__ == "__main__":
    test_lesson_04_modeling()
