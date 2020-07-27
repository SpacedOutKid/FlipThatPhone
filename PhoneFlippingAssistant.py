import openpyxl
wb = openpyxl.load_workbook('PhoneFlippingGradingScale.xlsx') #calls the excel sheel where the prices are located
sheet = wb.get_sheet_by_name('USED IPHONE') #calls the exact sheet in the excell sheet where the prices are located

#A class for the main border which iwll be used 
class MenuBorder(): 
    def border(self):
        print(' ')
        for i in range(30):
            print(" *", end='')
        print('\n')

#A class with the grading scale specifics 
class GradingScale():
    def gradingRubric(self):
        print('\n\n')
        for i in range(53): #specific border menu for the Grading scale
            print(" *", end = "")
        print('\n\n\t\t\t\t    📝 Grading Scale 📝:')
        print('\n\tA Grade: Fully functional, perfect condition, no dents or scratches')
        print('\tB Grade: Fully functional, dents or scratches present. No Heavy/deep scratches')
        print('\tC Grade: Fully functional, heavy dents or scratches, lcd lines/spots, NO blackout LCD')
        print('\tD Grade: Fully functional, heavy dents/scratches or cracked, lcd lines./spots, no missing parts\n')
        for i in range(53): #specific border menu for the Grading Scale
            print(" *", end = "")
#A class for confirmation to end program or continue 
class Confirmation():
    def confirmMsg(self):
        confirmationMesage = input('\nWould you like to check another phone? Enter Y for yes or an N for no: ').upper()


phoneOption = False #creates a variable for the following loop
while phoneOption == False: #loop for the program to stay in so the user can continue or exit after checking on one phone
    supportedPhones = {0: 'Grading Scale 📝', 1: 'iPhone 7 📱', 2: 'iPhone 7 Plus 📱', 3: 'iPhone 8 📱', 4: 'iPhone 8 Plus 📱', 5: 'iPhone X 📱', 6: 'iPhone XR 📱', 7: 'iPhone XS 📱', 8: 'iPhone XS Max 📱', 9: 'iPhone 11 📱', 10: 'iPhone 11 Pro 📱', 11: 'iPhone 11 Pro Max 📱'} #list of phones to choose from
    MenuBorder.border('*') #anytime you see this it is calling the Menu Border class to create a menu border 
    print('\t\t     🗳  Menu Options 🗳 :\n')
    for key, value in supportedPhones.items(): #Prints each items key and value in the supportedPhones Dict
        print('\t\t   ', key, ':', value)
    MenuBorder.border('*')
    yourOption = eval(input('\n\nEnter the number of the phone you would like a price for: '))
    if yourOption == 0:
        GradingScale.gradingRubric(print)
        print('\n\n')
        if Confirmation.confirmMsg('self') == 'N':
            print('Thanks for using this program')
            phoneOption = True
        