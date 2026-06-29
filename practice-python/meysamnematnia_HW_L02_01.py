import getpass

#-------------------------گرفتن یوسر نیم از کاربر-------------------------
while True:
    username = input("Enter a username: ").strip()
    if username == "":
        print("Username cannot be empty. Please try again.")
    else:
        break
#------------------------------سال تولد----------------------------------
while True:
    birth_year = input("Enter a year of birth: ")
    if birth_year == "":
        print("year of birth cannot be empty. Please try again.")
    elif not birth_year.isdigit():
        print("onle use number")
    else:
        break
#--------------------------گرفتن پسورد از کاربر---------------------------
while True:
    password = getpass.getpass("Enter a password: ").strip()
    if password == "":
        print("Password cannot be empty. Please try again.")
    else:
        break
#------------------------------------------------------------------
score = 9
power = []
# -----------------------------------پسورد هایی که نباید استفاده شود------------------------------
password_dont = [
    "123456", "12345678", "12345", "111111", "123456789", "qwerty", "asdfgh", "zxcvbnm", "password", "admin", "P@s$w0rd"
]
#--------------------پرینت نام کاربری و رمز عبور------------------------------------------------------
print("----------------------Password Strength Checker---------------------------")
print(f" 👤 username: {username}")
print(f" 🎉 year of birth: {birth_year}")
print(f" 🔑 password: {password}")
print(" \n✅ filter checks:")
# -------filter1---------------------------طول پسورد بیشتر از 8 کارکتر-------------------
if len(password) >= 8:
    print("✅ Password is longer than 8 characters.")
    power.append("long password")
else:
    print("❌ Password is shorter than 8 characters")
    score -= 1
#-----------filter2-------------------------------حداقل یک حرف انگلیسی داشته باشد-----------------
one_word = False
for ch in password:
    if ch.isalpha():
        one_word = True
        break

if one_word:
    print("✅ Password contains at least one English letter.")
    power.append("use english word")
else:
    print("❌ Password does not contain any English letters.")
    score -= 1
#-----------filte3---------------------------------کارکتر خاص-----------------------
special_character = False
for ch in password:
    if ch in "$@!":
        special_character =True
        break
    
if special_character:
    print("✅ Password contains at least one special character.")
    power.append("use special word")
else:
    print("❌ Password does not contain any special characters.")
    score -= 1
#---------filter4---------------------------حرف بزرگ------------------------------------
upper_case = False
for ch in password:
    if ch.isupper():
        upper_case = True
        break
    
if upper_case:
    print("✅ Password contains at least one uppercase letter.")
    power.append("capitalization")
else:
    print("❌ Password does not contain any uppercase letters.")
    score -= 1
#---------filte5-----------------------------پسورد نام کاربری نباشد----------------------
if password == username:
    print("❌ Password is identical to the username.")
    score -=1
else:
    print("✅ Password is not identical to the username.")
    power.append("likeness")
#---------filter6------------------(swapcase) پسورد نسخه بزرگ و کوچک شده یوسرنیم نباشد------------------------
if password == username.swapcase():
    print("❌ Password is the swapcase version of the username.")
    score -= 1
else:
    print("✅ Password is not the swapcase version of the username.")
    power.append("dont use swapcase in username")
#---------filter7--------------پسورد نباید نسخه نام کاربری حروف خاص باشد----------------------------
base_username = username.lower()
base_username = base_username.replace("a", "@")
base_username = base_username.replace("i", "!")
base_username = base_username.replace("s", "$")
base_username = base_username.replace("o", "0")

if password.lower() == base_username:
    print("❌ Password is a special-character version of the username.")
    score -= 1
else:
    print("✅ Password is not a special-character version of the username.")
    power.append("dont use specila charectes version in username")
#---------filter8------------------پسورد های رایح نباشد----------------------------------------
if password in password_dont:
    print("❌ Password is one of the most common passwords.")
    score -= 1
else:
    print("✅ Password is not one of the most common passwords.")
    power.append("Not a common password")
#------filter9-------------------------پسورد شامل سال تولد نباشد-----------------------------------
if birth_year in password:
    print("❌password includes year of birth")
    score -= 1
else:
    print("✅password does not include the year of birth")
    power.append("dont use year birth in password")
#------------------------------بخش امتیاز---------------------------------------------------
if score == 9:
    level_score = "very strong"
elif score >= 7:
    level_score = "strong"
elif score >= 5:
    level_score = "medium"
elif score >= 3:
    level_score = "weak"
else:
    level_score = "very weak"
#-----------------------------------نشان دادن امتیاز ها و قدرت پسورد -----------------------------------------------
print(f"🔐 Final Score: {score}")
print(f"🔒 Security Level: {level_score}")

#---------------------------------------نوشتن نکته--------------------------------------------------
if score == 8:
    print("📌 Tip: Your password is very strong and well protected.")
elif score >= 6:
    print("📌 Tip: Your password is good, but you can make it even stronger.")
elif score >= 4:
    print("📌 Tip: Your password is medium acceptable, but it needs improvement.")
elif score >= 2:
    print("📌 Tip: Your password is weak. Add more letters, symbols, and uppercase characters.")
else:
    print("📌 Tip: Your password is too simple and easy to guess. Use a mix of letters, numbers, and symbols.")
#--------------------------print-power----------------------------------
print("💪power💪")
if len(power) == 0:
    print("none")
else:
    for item in power:
        print("-", item)


