
'''
                              project introuduction
Today we are Create A strong Password Generator app.
Language:Python,
Library:Tkinter.
We use randint,choice functions from random for generateerate password randomly.
pastebinLink:https://pastebin.com/pMfcie6D
GithubLink:https://github.com/redoansaleh1/RedoPass
'''

#Let's import Required Modules

from tkinter import *
from random import randint,choice

class passwordGenerator():
    
    #use the constructor for take the name of this passwordGenerator.
    
    def __init__(self,name):
        self.name=name
    
    '''
    run method for run the main part of the app. 
    it create the window,button,Label etc. and running the mainloop of the window.
    '''                
    
    def run(self):
        
        #creating the window and title.
        
        self.root=Tk()
        self.root.title(self.name)
        
        #the Header Label.
        
        self.Title=Label(self.root,text='Generate Your Password',bg='black',fg='white')
        self.Title.grid(row=0,column=0)
        
        #Create Scale for input the length of password from user.
        
        self.askLengthLabel=Label(self.root,text='Length of Password: ',bg='black',fg='white')
        self.askLengthLabel.grid(row=1,column=0)
        self.lengthOfPassword = Scale(self.root,from_=8,to=50,orient=HORIZONTAL)
        self.lengthOfPassword.grid(row=1,column=1)
        
        #Create CheckButtons for asking the user that which character set the user want on the password.
        
        self.uppercase=IntVar()
        self.isUppercase=Checkbutton(self.root,text='include uppercase',variable=self.uppercase)
        self.isUppercase.grid(row=2,column=0)
        self.lowercase=IntVar()
        self.islowercase=Checkbutton(self.root,text='include lowercase',variable=self.lowercase)
        self.islowercase.grid(row=3,column=0)
        self.Number=IntVar()
        self.isNumber=Checkbutton(self.root,text='include Numbers',variable=self.Number)
        self.isNumber.grid(row=4,column=0)
        self.Symbols=IntVar()
        self.isSymbols=Checkbutton(self.root,text='include Symbols',variable=self.Symbols)
        self.isSymbols.grid(row=5,column=0)
        
        #Output Box where the Password displayed.
        
        self.output=Label(self.root,text='                                              ')
        self.output.grid(row=6,column=0)
        
        #Creating Required Buttons.
        
        self.generatePassword=Button(self.root,text='Generate',bg='black',fg='white',command=self.__generate,highlightcolor='green')
        self.generatePassword.grid(row=7,column=0)
        self.copyPassword=Button(self.root,text='Copy',bg='black',fg='white',command=self.__copy)
        self.copyPassword.grid(row=7,column=1)
        
        #running the loop for the root and change back-ground color.
        
        self.root.config(bg='black')
        self.root.mainloop()       
    
    '''
    __copy for the copy button.
    That copy the password on the clipboard. 
    '''
                    
    def __copy(self):self.root.clipboard_append(self.output['text'])    
    
    '''
    generateerate method generateerate the random password and display on output Label,
    when the user click the generateerate button.
    '''
    
    def __generate(self):
            
            #when no character set is selected.
            
            if self.lowercase.get()==0 and self.uppercase.get()==0 and self.Number.get()==0 and self.Symbols.get()==0:
                self.output['text']='no character set is selected'  
                return None
            else:self.output['text']='                                              '
            
            #when all character set is selected.
            
            if self.lowercase.get()==1 and self.uppercase.get()==1 and self.Number.get()==1 and self.Symbols.get()==1:
                self.password=''
                for _ in range(int(self.lengthOfPassword.get())):
                        self.password+=chr(randint(33,126))
                self.output['text']=self.password
                return None
                
            #when only lowercase character set is selected.
            
            if self.lowercase.get()==1 and self.uppercase.get()==0 and self.Number.get()==0 and self.Symbols.get()==0:
                self.password=''
                for _ in range(int(self.lengthOfPassword.get())):
                        self.password+=chr(randint(97,122))
                self.output['text']=self.password
                return None
            
            #when only uppercase character set is selected.     
                        
            if self.lowercase.get()==0 and self.uppercase.get()==1 and self.Number.get()==0 and self.Symbols.get()==0:
                self.password=''
                for _ in range(int(self.lengthOfPassword.get())):
                        self.password+=chr(randint(65,90))
                self.output['text']=self.password
                return None               

            #when only Number character set is selected.            

            if self.lowercase.get()==0 and self.uppercase.get()==0 and self.Number.get()==1 and self.Symbols.get()==0:
                self.password=''
                for _ in range(int(self.lengthOfPassword.get())):
                        self.password+=chr(randint(48,57))
                self.output['text']=self.password
                return None                                        
            
            #when only special character set is selected.
            
            if self.lowercase.get()==0 and self.uppercase.get()==0 and self.Number.get()==0 and self.Symbols.get()==1:
                self.password=''
                for _ in range(int(self.lengthOfPassword.get())):
                        self.char1=randint(33,47)
                        self.char2=randint(58,64)
                        self.char3=randint(91,96)
                        self.char4=randint(123,126)
                        self.final_char=choice((self.char1,self.char2,self.char3,self.char4))
                        self.password+=chr(self.final_char)
                self.output['text']=self.password
                return None      
            
            #when lowercase,uppercase character set is selected.
            
            if self.lowercase.get()==1 and self.uppercase.get()==1 and self.Number.get()==0 and self.Symbols.get()==0:
                self.password=''
                for _ in range(int(self.lengthOfPassword.get())):
                        self.char1=randint(97,122)
                        self.char2=randint(65,90)
                        self.final_char=choice((self.char1,self.char2))
                        self.password+=chr(self.final_char)
                self.output['text']=self.password
                return None      

            #when Numbers,uppercase character set is selected.
            
            if self.lowercase.get()==0 and self.uppercase.get()==1 and self.Number.get()==1 and self.Symbols.get()==0:
                self.password=''
                for _ in range(int(self.lengthOfPassword.get())):
                        self.char1=randint(48,57)
                        self.char2=randint(65,90)
                        self.final_char=choice((self.char1,self.char2))
                        self.password+=chr(self.final_char)
                self.output['text']=self.password
                return None    

            #when Numbers,lowercase character set is selected.
            
            if self.lowercase.get()==1 and self.uppercase.get()==0 and self.Number.get()==1 and self.Symbols.get()==0:
                self.password=''
                for _ in range(int(self.lengthOfPassword.get())):
                        self.char1=randint(48,57)
                        self.char2=randint(97,122)
                        self.final_char=choice((self.char1,self.char2))
                        self.password+=chr(self.final_char)
                self.output['text']=self.password
                return None    

            #when Special,lowercase character set is selected.                    
            
            if self.lowercase.get()==1 and self.uppercase.get()==0 and self.Number.get()==0 and self.Symbols.get()==1:
                self.password=''
                for _ in range(int(self.lengthOfPassword.get())):
                        self.char1=randint(33,47)
                        self.char2=randint(58,64)
                        self.char3=randint(91,96)
                        self.char4=randint(123,126)
                        self.char5=randint(97,122)
                        self.final_char=choice((self.char1,self.char2,self.char3,self.char4,self.char5))
                        self.password+=chr(self.final_char)
                self.output['text']=self.password
                return None    
            
            #when Special,uppercase character set is selected.                    
            
            if self.lowercase.get()==0 and self.uppercase.get()==1 and self.Number.get()==0 and self.Symbols.get()==1:
                self.password=''
                for _ in range(int(self.lengthOfPassword.get())):
                        self.char1=randint(33,47)
                        self.char2=randint(58,64)
                        self.char3=randint(91,96)
                        self.char4=randint(123,126)
                        self.char5=randint(65,90)
                        self.final_char=choice((self.char1,self.char2,self.char3,self.char4,self.char5))
                        self.password+=chr(self.final_char)
                self.output['text']=self.password
                return None    
            
            #when Special,Number character set is selected.                    
            
            if self.lowercase.get()==0 and self.uppercase.get()==0 and self.Number.get()==1 and self.Symbols.get()==1:
                self.password=''
                for _ in range(int(self.lengthOfPassword.get())):
                        self.char1=randint(33,47)
                        self.char2=randint(58,64)
                        self.char3=randint(91,96)
                        self.char4=randint(123,126)
                        self.char5=randint(48,57)
                        self.final_char=choice((self.char1,self.char2,self.char3,self.char4,self.char5))
                        self.password+=chr(self.final_char)
                self.output['text']=self.password
                return None                 
            
            #when Special,Number,lowercase character set is selected.                    
            
            if self.lowercase.get()==1 and self.uppercase.get()==0 and self.Number.get()==1 and self.Symbols.get()==1:
                self.password=''
                for _ in range(int(self.lengthOfPassword.get())):
                        self.char1=randint(33,47)
                        self.char2=randint(58,64)
                        self.char3=randint(91,96)
                        self.char4=randint(123,126)
                        self.char5=randint(48,57)
                        self.char6=randint(97,122)
                        self.final_char=choice((self.char1,self.char2,self.char3,self.char4,self.char5,self.char6))
                        self.password+=chr(self.final_char)
                self.output['text']=self.password
                return None                              

            #when Special,Number,uppercase character set is selected.                    
            
            if self.lowercase.get()==0 and self.uppercase.get()==1 and self.Number.get()==1 and self.Symbols.get()==1:
                self.password=''
                for _ in range(int(self.lengthOfPassword.get())):
                        self.char1=randint(33,47)
                        self.char2=randint(58,64)
                        self.char3=randint(91,96)
                        self.char4=randint(123,126)
                        self.char5=randint(48,57)
                        self.char6=randint(65,90)
                        self.final_char=choice((self.char1,self.char2,self.char3,self.char4,self.char5,self.char6))
                        self.password+=chr(self.final_char)
                self.output['text']=self.password
                return None 

            #when Special,uppercase,lowercase character set is selected.                    
            
            if self.lowercase.get()==1 and self.uppercase.get()==1 and self.Number.get()==0 and self.Symbols.get()==1:
                self.password=''
                for _ in range(int(self.lengthOfPassword.get())):
                        self.char1=randint(33,47)
                        self.char2=randint(58,64)
                        self.char3=randint(91,96)
                        self.char4=randint(123,126)
                        self.char5=randint(97,122)
                        self.char6=randint(65,90)
                        self.final_char=choice((self.char1,self.char2,self.char3,self.char4,self.char5,self.char6))
                        self.password+=chr(self.final_char)
                self.output['text']=self.password
                return None 

            #when Number,uppercase,lowercase character set is selected.                    
            
            if self.lowercase.get()==1 and self.uppercase.get()==1 and self.Number.get()==1 and self.Symbols.get()==0:
                self.password=''
                for _ in range(int(self.lengthOfPassword.get())):
                        self.char1=randint(48,57)
                        self.char2=randint(97,122)
                        self.char3=randint(65,90)
                        self.final_char=choice((self.char1,self.char2,self.char3))
                        self.password+=chr(self.final_char)
                self.output['text']=self.password
                return None                                                                                                                                                           

#running the app from this file.       
         
if __name__=='__main__':
    
    #create our password generateerator with name RedoPass
    
    RedoPass=passwordGenerator('RedoPass')
    
    #run RedoPass App.
    
    RedoPass.run()
