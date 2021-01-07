#emp.csv
import csv
with open("emp.csv","w",newline='') as f:
 w=csv.writer(f) # returns csv writer object
 w.writerow(["ID","NAME","SAL"])
 w.writerow(["101","Anna","5500"])
 w.writerow(["\t","Jones","4500"])
 w.writerow(["102","smith","\t"])
 w.writerow(["103","\t","6500"])
 w.writerow(["104","Alice","3500"])
print("Total Employees data written to csv file successfully")
