from users import *
import datetime

##send("kebabbles", 'Jake')

introEmail = """
Hello, %s!
You've been matched with %s from %s!
Say hi at: %s

They are interested in:
%s

Here is their introduction:
%s
"""

applicationEmail = """
So far I plan to match everyone with one other person automatically, exactly once a week, at a set time.
Since matches are limited, people will value them more and put more effort into getting to know the person.  At least, that is the hope.

If you want to include pictures, you can add imgur (or some other image hosting) links in the introduction box.

Please complete this survey to join:
If you want to change your information in the future, just complete the form again with the same password.
>google form link<"""

# [email, name, gender, location, introduction, interests, personality]


matchedThisWeek = False
matchDay = 6

while True:    
    day = datetime.datetime.today().weekday()
    
    latest = getLatest()
    sub = getSubject(latest).lower()
    msg = getString(latest)
    auth = getAuthor(latest)
    if sub == 'mail matcher application' or ('mail' in sub and 'matcher' in sub and 'application' in sub):
        send(applicationEmail,
             'Welcome to Mail Matcher!',
             auth, False)
        
    if day == matchDay and not matchedThisWeek:
        print('Match day!')
        for male in userClass.males:
            female = match(male)
            send(introEmail % (male.name, female.name, female.location, female.email, female.interests, female.introduction),
                 "Meet %s" % female.name,
                 male.email)
            send(introEmail % (female.name, male.name, male.location, male.email, male.interests, male.introduction),
                 "Meet %s" % male.name,
                 female.email)
    matchedThisWeek = day == matchDay
        
##        addNewUser(bio) 
        
    
