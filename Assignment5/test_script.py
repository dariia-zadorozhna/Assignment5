import subprocess

def run_calculator(input_data):
    process = subprocess.Popen(
        ['./Source'],  # Assumes 'Source' is the compiled executable
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, stderr = process.communicate(input_data)
    return stdout.strip(), stderr.strip()

def test_calculator():
    tests = [
        {
            "input": "1+4",
            "expected_output": "Answer: 5"
        },
        {
            "input": "12345-345",
            "expected_output": "Answer: 12000"
        }
    ]
    for test in tests:
        input_data = test["input"]
        expected_output = test["expected_output"]

        output, error = run_calculator(input_data)

        if error:
            print(f"Test failed for input:\n{input_data}")
            print(f"Error:\n{error}")
        elif output.strip() != expected_output:
            print(f"Test failed for input:\n{input_data}")
            print(f"Expected:\n{expected_output}")
            print(f"Got:\n{output}")
        else:
            print(f"Test passed for input:\n{input_data}")

if __name__ == "__main__":
    test_calculator()
