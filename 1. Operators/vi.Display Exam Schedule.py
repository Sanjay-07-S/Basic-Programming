# Write a Python program to display the examination schedule. (extract the date from     exam_st_date).
   # exam_st_date = (11, 12, 2014)
    #Sample Output : The examination will start from : 11 / 12 / 2014


exam_st_date = (11,12,2014)

day,month,year = exam_st_date

date_formate = f"{day}/{month}/{year}"

print(f"The examination will start from: ",date_formate)


