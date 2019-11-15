# Menu Notification
# https://jhu.cafebonappetit.com/cafe/fresh-food-cafe/2019-11-08/
# Conner Delahanty
import requests

def readFFC(month, day, year):
    menu_items = []
    menu_url = 'https://jhu.cafebonappetit.com/cafe/fresh-food-cafe/'+year+'-'+month+'-'+day+'/'
    menu_items.append(menu_url)
    
    try:
        data = requests.get(menu_url)
    except:
        print("Error loading FFC Menu")
        return [menu_url]
    
    data = str(data.text)
    
    label_pos = data.find("dinner") # initialization value
    record_word = False
    
    while (label_pos != -1):
        label_pos = data.find('"label":', label_pos + 1) # +1 to avoid same position
        # get the word
        word_of_interest = data[label_pos + 9: data.find("\"", label_pos + 9)]

        # skip if not lowercase
        if (word_of_interest[0].upper() == word_of_interest[0]):
            continue
        
        # if the word contains"pizza" we want the next items until scratch
        if (word_of_interest.find("pizza") != -1):
            record_word = True
            
            
        if (record_word):
            if (word_of_interest.find("scratch") != -1): # "scratch" is the stopping point
                break
            if (word_of_interest.find("pizza") == -1): # if it is not pizza
                menu_items.append(word_of_interest)
                
    return menu_items


def readNolans(month, day, year):
    num_items = 6
    menu_items = []
    menu_url = 'https://jhu.cafebonappetit.com/cafe/nolans-on-33rd/'+year+'-'+month+'-'+day+'/'
    menu_items.append(menu_url)
      
    try:
        data = requests.get('https://jhu.cafebonappetit.com/cafe/nolans-on-33rd/'+year+'-'+month+'-'+day+'/')
    except:
        print("Error loading Nolan's Menu")
        return [menu_url]
    
    data = str(data.text)
    
    label_pos = data.find("dinner") # initialization value
    record_word = False
    first_word = True
    second_word = False
    
    while (label_pos != -1):
        label_pos = data.find('"label":', label_pos + 1) # +1 to avoid same position
        # get the word
        word_of_interest = data[label_pos + 9: data.find("\"", label_pos + 9)]

        # skip if not lowercase
        if (word_of_interest[0].upper() == word_of_interest[0]):
            continue
        
        if (second_word): # we want the second menu item (that is the burger section)
            menu_items.append(word_of_interest)
            second_word = False  
        
        if (first_word): # ignore the first word
            second_word = True
            first_word = False
            
        # if the word contains "sauces" we want the next items until scratch
        if (word_of_interest.find("sauces") != -1):
            record_word = True
            
            
        if (record_word):
            if (word_of_interest.find("passport") != -1): # "scratch" is the stopping point
                break
            if (word_of_interest.find("sauces") == -1 and len(menu_items) < num_items): # if it is not sauces
                menu_items.append(word_of_interest)   
                
    return menu_items
