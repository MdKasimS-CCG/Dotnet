import subprocess

OLD_EMAIL = "kasim@cornerstone-consulting.io"
OLD_NAME = "kasimccg"

NEW_NAME = "MdKasimSAsus"
NEW_EMAIL = "itskasimsache@gmail.com"

try:
    current_name = subprocess.check_output(
        ["git", "config", "--global", "user.name"],
        text=True
    ).strip()

    current_email = subprocess.check_output(
        ["git", "config", "--global", "user.email"],
        text=True
    ).strip()

    print(f"Current: {current_name} <{current_email}>")

    if current_email == OLD_EMAIL:
        subprocess.run(
            ["git", "config", "--global", "user.name", NEW_NAME],
            check=True
        )
        subprocess.run(
            ["git", "config", "--global", "user.email", NEW_EMAIL],
            check=True
        )

        print(f"Updated to: {NEW_NAME} <{NEW_EMAIL}>")
    else:
        print("Old email does not match. No changes made.")

except subprocess.CalledProcessError as e:
    print(f"Error: {e}")