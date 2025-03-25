import os

files = [file for file in os.listdir() if os.path.isfile(os.path.join(os.getcwd(), file))]

if 'main.py' in files:
    files.remove('main.py')

if not files:
    print("No files to organize.")
    exit()

def avoid_redundancy(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move_files(files, folder):
    count = 0
    for file in files:
        destination = os.path.join(folder, file)
        if not os.path.exists(destination):  # Avoid overwriting
            os.replace(file, destination)
            count += 1
    return count

extension_images = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg']
extension_documents = ['.txt', '.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx']
extension_programs = ['.exe', '.py', '.js', '.html']

avoid_redundancy('Images')
avoid_redundancy('Documents')
avoid_redundancy('Programs')
avoid_redundancy('Others')

images = [file for file in files if os.path.splitext(file)[1].lower() in extension_images]
documents = [file for file in files if os.path.splitext(file)[1].lower() in extension_documents]
programs = [file for file in files if os.path.splitext(file)[1].lower() in extension_programs]



# for documents in documents:
#     os.replace(documents, f'Documents/{documents}') 

# for images in images:
#     os.replace(images, f'Images/{images}')

# for programs in programs:
#     os.replace(programs, f'Programs/{programs}')

# for others in Others:  
#     os.replace(others, f'Others/{others}')




Others = []
for file in files:
    other_extension = os.path.splitext(file)[1].lower()
    if (
        other_extension not in extension_images
        and other_extension not in extension_documents
        and other_extension not in extension_programs
    ):
        Others.append(file)

images_count = move_files(images, 'Images')
documents_count = move_files(documents, 'Documents')
programs_count = move_files(programs, 'Programs')
others_count = move_files(Others, 'Others')

print(f"Files moved to 'Images': {images_count}")
print(f"Files moved to 'Documents': {documents_count}")
print(f"Files moved to 'Programs': {programs_count}")
print(f"Files moved to 'Others': {others_count}")