import os
import time
import glob

i=1
for audio in glob.glob("/Users/ryanzrymiak/Downloads/output_voice*.mp3"):
        
        f = open("/Users/ryanzrymiak/Downloads/survey_responses.txt", "a")
        f.write("\nVoice " + str(i) + " >> ")

        print("Please listen carefully to the audio sample.")
        time.sleep(3)
        os.system("afplay " + audio)

        a = 0
        e = 0
        while(a == 0):
            print("How agreeable do you feel with this voice? Would you do as it says?")
            print("1) Not agreeable at all")
            print("2) Slightly agreeable")
            print("3) Moderately agreeable")
            print("4) Very agreeable")
            print("5) Extremely agreeable")
            agree = input("Please input your choice (1,2,3,4,5): ")
            if(agree.strip() == '1' or agree.strip() == '2' or agree.strip() == '3'
               or agree.strip() == '4' or agree.strip() == '5'):
                a = 1
                f.write("Agreeableness: " + agree + ", ")
            else:
                print("Please input a valid choice")

        while(e == 0):
            print("How engaged did you feel while listening to this voice? Would you listen seriously/earnestly?")
            print("1) Not engaged at all")
            print("2) Slightly engaged")
            print("3) Moderately engaged")
            print("4) Very engaged")
            print("5) Extremely engaged")
            engage = input("Please input your choice (1,2,3,4,5): ")
            if(engage.strip() == '1' or engage.strip() == '2' or engage.strip() == '3'
               or engage.strip() == '4' or engage.strip() == '5'):
                e = 1
                f.write("Engagement: " + engage + ", ")
            else:
                print("Please input a valid choice")
        i+=1
        total = int(agree)+int(engage)
        f.write("Total Score: " + str(total) + ", ")    

'''
d = 0   
while(d == 0):
    print("Which voice did you find the most memorable in terms of how effective they sounded?")
    best = input("Please input your choice (1,2,3): ")
    if(best.strip() == '1' or best.strip() == '2' or best.strip() == '3'):
        d = 1
        f.write("\nBest:" + best + ", ")
    else:
        print("Please input a valid choice")
'''

comments = input("Are there any additional comments you would like to share about the voices you heard? ")
f.write("Comments: " + comments + "\n")
f.close()
print("Thank you for your participation in this survey.")
