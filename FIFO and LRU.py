#This program takes in a page size from the user, and processes
#predefined word requests simulating both the FIFO pages swaping algorithm
#and the LRU page swapping algorithm


import math


def fifo(num_pages, pages, num_pf, page_size):
    #create a list that will act as the page frames
    print("The FIFO algorithm results:")
    page_frame = []
    page_fault = 0

    #load pages into the page frames
    for i in pages:
        if len(page_frame) < num_pf: #check to see if page frame is full
            if i not in page_frame: #check to see if i already in the page frame
                page_frame.append(i) 
                print("{} loaded".format(i))
                page_fault += 1
                
            else:  #if i in page frame skip it
                print("{} skipped, already in page frame.".format(i))

        else:  #if page frame is full
            if i not in page_frame: #if i not in page frame
                page_frame.pop(0) #pop the first element in the page frame
                page_frame.append(i) #append the new element to the list
                page_fault +=1
                print("{} loaded".format(i))

            else: #skip loading i if already in page frame
                print("{} skipped, already in page frame.".format(i))


    stats(page_fault,page_size,num_pages)

  

def lru(num_pages, pages, num_pf, page_size):
    #create a list that will act as the page frames
    print("The LRU algorithm results:")
    page_frame = []
    page_fault = 0

    #load pages into the page frames
    
    for i in pages:
        if len(page_frame) < num_pf: #check to see if page frame is full
            if i not in page_frame: #check to see if i is in page frame 
                page_frame.append(i)#if i not in page frame append
                print("{} loaded".format(i))
                page_fault += 1
                
            else: #if i is in page frame skip
                print("{} skipped, already in page frame.".format(i))
        else:
            if i in page_frame:  
                location = page_frame.index(i) #if i in page frame find i's index
                page_frame.pop(location) #pop i from the frame
                page_frame.append(i) #append it to the end 
                print("{} skipped, already in page frame.".format(i))
            else:
                page_frame.pop(0) #if i not in page frame, pop the first element and append i
                page_frame.append(i)
                page_fault +=1
                print("{} loaded".format(i))

    #call the stats function to print results.
    stats(page_fault,page_size,num_pages)

#calculate the transfer time.
def tr_time(page_size, page_fault):
    transfer_time = 0
    if page_size == 100:
        transfer_time = page_fault*1
    elif page_size == 200:
        transfer_time = page_fault*2
    else:
        transfer_time =page_fault*5
    print("Transfer time is {} seconds".format(transfer_time))

#calculate the hit ratio:
def hit_ratio(num_pages, page_fault):
    print("The hit ratio is {:.2%}.".format((num_pages - page_fault)/ num_pages))

#print the stats 
def stats(page_fault,page_size,num_pages):
    print("The number of page faults is {}".format(page_fault))
    tr_time(page_size, page_fault)
    hit_ratio(num_pages, page_fault)


print()       


              

def main():

    mem_size = 200 #this value was given in the problem statement
    
    page_size = eval(input("Please enter page size: ")) #request page size from user

    while page_size > mem_size:
        print("Your page size is larger than the memory size of 200, please enter a number less than 200")
        page_size = eval(input("Please enter page size: ")) 
        
    num_pf = mem_size / page_size #calculate the number of page frames
    
    word_request = [10,11,104,170,73,309,185,246,434,458,364] #these were given in the problem statement

    #Calculate what page each word is located on, and append it to a list called pages
    pages=[] 
    for i in word_request:
        pages.append(math.floor(i/page_size))

    print("The pages that will be loaded; {}".format(pages))

    num_pages = len(pages)

    results_fifo = fifo(num_pages, pages, num_pf, page_size)

    print()

    results_lru = lru(num_pages, pages, num_pf, page_size)


    


main()
