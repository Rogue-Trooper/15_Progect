import strong_password_task


def main():
    password = input("Input your strong password: ")

    result = strong_password_task.check_password(password)

    msg = f"You password is {result}" if isinstance(result, str) \
        else "User data invalid"

    print(msg)


if __name__ == "__main__":
    main()
