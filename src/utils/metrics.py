from datetime import datetime
import os


def format_response(steps, elevation, coords, ):
    print(f"Steps taken during algorithm traversal: {steps}\n\n")
    print(f"Algorithm reached a max elevation of: {elevation}\n\n")
    print(f"Algorithm ended at coordinates: {coords}\n\n")
    pass

def write_output(path):
    timestamp =datetime.now().strftime("%Y%m%d_%H%M%S")
    root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    output_directory = os.path.join(root, "outputs")
    os.makedirs(output_directory, exist_ok=True)

    with open(f"{output_directory}/output_{timestamp}.txt", "w") as file:
        file.write("\n".join(str(entry) for entry in path))
