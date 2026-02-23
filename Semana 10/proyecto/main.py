from menu import menu


def main():
    try:
        menu()
    except Exception as error:
        print(f'An unexpected error occurred in main(): {error}')

main()