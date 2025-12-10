from datetime import datetime
import os


def format_response(
    steps,
    elevation,
    coords,
):
    print(f"Steps taken during algorithm traversal: {steps}\n\n")
    print(f"Algorithm reached a max elevation of: {elevation}\n\n")
    print(f"Algorithm ended at coordinates: {coords}\n\n")


def write_output(path, algorithm):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    output_directory = os.path.join(root, "outputs")
    directory_name = algorithm.replace(" ", "_").lower()
    os.makedirs(os.path.join(output_directory, directory_name), exist_ok=True)

    with open(
        f"{output_directory}/{directory_name}/output_{timestamp}.txt", "w"
    ) as file:
        file.write(f"Algorithm being ran is {algorithm}\n\n")
        file.write("\n".join(str(entry) for entry in path))
    print(
        f"\nFull path log saved to: {output_directory}/{directory_name}/output_{timestamp}.txt"
    )
