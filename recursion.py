# File Finder

file_system = [
    [
        "nothing.txt",
        "dog_pic.png",
        [
            "secret_plan.pdf"
        ]
    ],
    "notion.app",
    "slack.app",
    [
        "fun.txt",
        [
            "meaningless_file.txt",
            "chicken_dinner.txt"
        ],
        "not_fun.txt"
    ],
    "zoom.app"
]

target = "chicken_dinner.txt"

def find_file(file_system, target):
    for file in file_system:
        if isinstance(file, list):
            if find_file(file, target):
                return True
        elif file == target:
            print("HOORAY")
            return True
    return False

find_file(file_system, target)