import re
import argparse

MIN_LENGTH = 8

def load_common_passwords(file_path="password_checker/common_passwords.txt"):
    try:
        with open(file_path, 'r') as file:
            return set(line.strip() for line in file)
    except FileNotFoundError:
        return set()
    
def check_password_strength(password, blacklist):
    score = 0
    feedback = []
    
    #length
    if len(password) >= MIN_LENGTH:
        score += 1
    else:
        feedback.append("Password is too short (minimum 8 characters).")
        
    #uppercase  
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")
        
    # digit
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one digit.")
        
    # special character
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    # blacklist
    if password.lower() in blacklist:
        feedback.append("Password is too common. Choose something unique.")
        score = 0
    
    if re.search(r"(.)\1\1", password):
        feedback.append("Avoid using the same character three or more times in a row.")

    return score, feedback

def Score(score):
    if score == 5:
        return "Very Strong"
    elif score == 4:
        return "Strong"
    elif score == 3:
        return "Moderate"
    elif score == 2:
        return "Weak"
    else:
        return "Very Weak"
    
def main():
    parser = argparse.ArgumentParser(description="Password Strength Checker")
    
    parser.add_argument("password",type=str, help="Password to check")
    
    arg = parser.parse_args()
    blacklist = load_common_passwords()
    score, feedback = check_password_strength(arg.password, blacklist)
    rating = Score(score)
    
    print("\n========== PASSWORD CHECK ==========")
    print(f"Password Strength: {rating}")
    print(f"Score: {score}/5")

    if feedback:
        print("\nSuggestions:")
        for msg in feedback:
            print(f" - {msg}")
    else:
        print("\nPerfect password. No issues found.")

    print("===================================\n")


if __name__ == "__main__":
    main()