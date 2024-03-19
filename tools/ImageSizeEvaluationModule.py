import os

def assign_note(size):
    if size > 500 * 1024:  # Convert KB to bytes
        return 1
    else:
        return 10

def process_images(directory):
    notes = []
    for filename in os.listdir(directory):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.gif', '.svg')):  # Add more image formats if needed
            file_path = os.path.join(directory, filename)
            size = os.path.getsize(file_path)
            note = assign_note(size)
            notes.append((note, file_path))
    return notes

if __name__ == "__main__":
    directory = input("Enter the directory containing images: ")

    if not os.path.exists(directory):
        print("Directory does not exist.")
    else:
        notes = process_images(directory)
        print("Notes and URLs of images:")
        for note, file_path in notes:
            print(f"Note: {note}, Image URL: {file_path}")