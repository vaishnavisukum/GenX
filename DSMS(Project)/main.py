import sys
import os

def create_table(cmd_list:list):

  if cmd_list=="INTO":
    file=open("./"+cmd_list[3]+"/untitled.csv","w") 
    file.close()
  else:
    file_name=cmd_list[1]
    file=open("./"+cmd_list[3]+file_name,"w")

    file.close()
  

#This is root(entry point function)-->
#Date - 15-03-2026

def main():

  if len(sys.argv)>=2:
    if sys.argv[1]=="--h":

     print(''' 
          to crate a new DB : CREATE_DB <database_name>
          to create a table : CREATE_TABLE <table_name> INTO <db_name>
          ''')
    
  terminate= False
  while terminate== False:
    cmd=input()
    splited_cmd=cmd.split(" ")

    if cmd =="exit":
      break 
    if splited_cmd[0]=="CREATE_DB": 
      if len(splited_cmd)<2:
        db_name="Untitled"
      else:
        db_name = splited_cmd[1]
      
      os.makedirs("./root/"+db_name)

    elif splited_cmd[0] =="CREATE_TABLE":
       create_table(splited_cmd)

if __name__=="__main__":
  main()