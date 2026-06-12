import secrets
import string

def generate_secure_password(length : int = 12 , include_uppercase : bool = True, include_digits: bool = True , include_specialchar: bool = True) -> str:
    if length <= 4:
        raise ValueError("Password length must be atleast 4")
    
    uppercase_pool = string.ascii_uppercase if include_uppercase else ""
    lowercase_pool = string.ascii_lowercase
    digits_pool =  string.digits if include_digits else ""
    special_char_pool = string.punctuation if include_specialchar else ""
    
    combined_pool = uppercase_pool + lowercase_pool + digits_pool + special_char_pool

    if not combined_pool:
        raise ValueError("Atleast one character set must be included")
    
    pass_char = [secrets.choice(lowercase_pool)]
    
    if include_uppercase:
        pass_char.append(secrets.choice(uppercase_pool))
    if include_digits:
        pass_char.append(secrets.choice(digits_pool))
    if include_specialchar:
        pass_char.append(secrets.choice(special_char_pool))
        
    
    remaining_slot =length - len(pass_char)
    
    pass_char.extend(secrets.choice(combined_pool) for _ in range(remaining_slot))
    
    secure_shuffler = secrets.SystemRandom()
    secure_shuffler.shuffle(pass_char)

    return "".join(pass_char)
    

passs = generate_secure_password()
print(passs)