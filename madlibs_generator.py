def madlibs_generator():
    # Madlibs template with blanks
    template = "I enjoyed {adjective} programming with {programming_language}"
    
    # Prompt the user for words to fill in the blanks
    adjective = input("Input an adjective: ")
    programming_language = input("Input programming language: ")
    
    # Fill in the blanks in the template
    madlibs_result = template.format(adjective=adjective, programming_language=programming_language)
    
    # Display the complete result
    print("\nYour Mad Libs:")
    print(madlibs_result)
    

if __name__ == "__main__":
    madlibs_generator()