import pyperclip

# Open a file in write mode
with open("C:/Users/Sorin Chirtoaca/Desktop/Aurl2.txt"
          , 'w') as file:
    while True:
        # Wait for user to copy text to the clipboard
        input("Copy your link(s) to the clipboard, then press Enter to save: ")
        
        # Retrieve contents of the clipboard
        clipboard_text = pyperclip.paste()
        
        # Write clipboard contents to the file
        file.write(clipboard_text + '\n')
        print("Link(s) saved to file!")
        
        # Ask the user if they want to continue or exit
        response = input("Press Enter to continue or type 'exit' to quit: ")
        if response.lower() == 'exit':
            break

# Close the file
file.close()
