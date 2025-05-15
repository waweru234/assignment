def file_processor():
    """
    This program:
    1. Asks user for a filename to read
    2. Handles various file-related errors
    3. Modifies the content (converts to uppercase in this example)
    4. Writes to a new file with '_modified' suffix
    5. Provides user feedback throughout the process
    """
    
    print("📁 File Processor Program 📁")
    print("This program will read a file, modify its content, and save a new version.")
    
    while True:
        try:
            # Get input filename from user
            input_filename = input("\nEnter the filename to read (or 'quit' to exit): ").strip()
            
            if input_filename.lower() == 'quit':
                print("👋 Exiting program...")
                break
            
            # Attempt to open and read the file
            try:
                with open(input_filename, 'r') as file:
                    content = file.read()
                
                print(f"\n✅ Successfully read: {input_filename}")
                
                # Process the content (example: convert to uppercase)
                modified_content = content.upper()
                
                # Create output filename
                output_filename = input_filename.split('.')[0] + '_modified.txt'
                
                # Write to new file
                try:
                    with open(output_filename, 'w') as file:
                        file.write(modified_content)
                    
                    print(f"✏️  Successfully wrote modified content to: {output_filename}")
                    print(f"🔍 Original file size: {len(content)} characters")
                    print(f"🔍 Modified file size: {len(modified_content)} characters")
                
                except PermissionError:
                    print(f"❌ Error: Permission denied when trying to write to {output_filename}")
                except OSError as e:
                    print(f"❌ Error writing file: {e}")
                
            except FileNotFoundError:
                print(f"❌ Error: The file '{input_filename}' does not exist.")
            except PermissionError:
                print(f"❌ Error: Permission denied when trying to read '{input_filename}'")
            except UnicodeDecodeError:
                print(f"❌ Error: Could not decode the file '{input_filename}'. It may be a binary file.")
            except IsADirectoryError:
                print(f"❌ Error: '{input_filename}' is a directory, not a file.")
            except OSError as e:
                print(f"❌ Unexpected error reading file: {e}")
        
        except KeyboardInterrupt:
            print("\n\n🛑 Program interrupted by user. Exiting...")
            break
        except Exception as e:
            print(f"\n❌ An unexpected error occurred: {e}")


if __name__ == "__main__":
    file_processor()