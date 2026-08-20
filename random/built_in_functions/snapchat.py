class Snapchat:
    usernames = {}
    def __init__(self,name,age,gender,psd,username):
        self.name=name
        self.age=age
        self.gender=gender
        self.psd=psd
        self.username=username
        Snapchat.usernames[username]=self
        self.logged=False
        self.friendslist=[]
        self.snaps=[]
    @classmethod
    def signup(cls):
        name=input("Enter name:")
        while True:
            username=input("Enter username:")
            if(username in cls.usernames.keys()):
                print("Username already exist,try another one")
                continue
            break
        while True:
            psd = input("Enter psd:")
            if(cls.validate_psd(psd)==False):
                continue
            break
        age = input("Enter age:")
        gender = input("Enter gender:")
        return cls(name,age,gender,psd,username)
    @staticmethod
    def validate_psd(psd):
        sp=['@','#','$','%','^','&','*','(',')','!']
        if(len(psd)>=8):
            u=list(filter(lambda x:x.isupper(),psd))
            s=list(filter(lambda x :x in sp,psd))
            d=list(filter(lambda x:x.isdigit(),psd))
            if u and s and d:
                print("strong password")
                return True
            else:
                print("weak password")
                return False
        else:
            print("Password must contain atleast 8 characters")
            return False
    def login(self):
        if self.logged:
            print("Already logged in")
        else:
            a=input("Enter Username:")
            b=input("Enter password:")
            if(a==self.username and b==self.psd):
                self.logged=True
                print("Login Successfull")
            else:
                print("Invalid Credentials")
    def logout(self):
        if self.logged:
            self.logged=False
            print("Logged out Successfull")
        else:
            print("Already logged out")
    def addfriend(self,x):
        if self.logged:
            if x not in self.friendslist:
                self.friendslist.append(x)
            else:
                print(f"{x} is already friend")
        else:
            print("Not Logged in")
    def removefriend(self,y):
        if self.logged:
            if y not in self.friendslist:
                print(f"{y} not found")
            else:
                self.friendslist.remove(y)
        else:
            print("Not Logged in")

    def view_friends(self):
        if self.logged:
            if len(self.friendslist) == 0:
                print("No friends added")
            else:
                for i, friend in enumerate(self.friendslist):
                    print(f"{i} : {friend.name}")
        else:
            print("Not Logged in")
    def profile(self):
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")
        print(f"Gender:{self.gender}")
    def send_snap(self,friend,snap):
        if self.logged:
            if friend in self.friendslist:
                friend.snaps.append((self,snap))
                print("snap sent successfully")
            else:
                print(f"{friend} is not found")
        else:
            print("Not Logged in")
    def view_snaps(self):
        if self.logged:
            if len(self.snaps)==0:
                print("no snaps")
            else:
                for i in range(len(self.snaps)):
                    print(self.snaps[i])
        else:
            print("Not Logged in")
s1 = Snapchat.signup()
s2 = Snapchat.signup()
s1.login()
s1.addfriend(s2)
s1.view_friends()
s1.send_snap(s2, "My first snap")
s1.profile()
s2.login()
s2.view_snaps()
s2.profile()
