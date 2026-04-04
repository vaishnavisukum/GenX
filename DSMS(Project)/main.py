import sys
import os
from pathlib import Path

PATH=str(Path.cwd())


def create_table(cmd_list):

    if cmd_list[1]=="INTO":
       if os.path.exists(".\\root\\"+cmd_list[2]+"\\untitled.csv"):
           return f"MESSAGE:untitled.csv alredy exists in {cmd_list[2]}"
    else:
        file=open(PATH+"\\root\\"+cmd_list[3]+f"\\{cmd_list[1]}.csv","w") #open alwayas takes absolute path
        file.write("")
        file.close()

#this is root (entry point function)=name
#date -15-3-26
def main():
     if len(sys.argv) >= 2:
        if sys.argv[1]=="--h":    
        
         print('''
          to create a DB          : CREATE_DB <database_name>
          to create a table1      : CREATE_TABLE <table_name> INTO <db_name> 
          to use perticular DB    : use<db_name >
          to use perticular Table : use<Table_name> FROM <DB_name>
          to fill data into table : use<Table _name> FROM <DB_name>
                                   WRITE{
                                       <column_name>:<data>,....,<n_data>;
                                       <column_name>:<data>,....,<n_data>;  
                                          .
                                          . 
                                          .
                                       <column_name>:<data>,....,<n_data>;     
               } 
         to show elements in perticular column of perticular table:
                                 USE <Table_name> from <DB_name>
                                 SHOW<column_name>
               
         to show all columns present in table  
                                  USE <Table_name> from <DB_name>
                                  SHOW COLUMNS  
               
         to show all form a table:
                                USE <Table_name> from <DB_name>  
                                SHOW ALL
               
         to show all DB        :
                                SHOW DATA_BASES

        to search table name in all DB's:
                                   SEARCH <TABLE_Name>  
          ''')

     terminate=False
     while terminate==False:
        
         cmd=input()
         splited_cmd =cmd.split(" ")  #split string on the basis of space " "
         
         if cmd=="exit":
             break
         
         if splited_cmd[0]=="CREATE_DB":
              if len (splited_cmd)<2:
        
                  db_name="untitled"
              else:
                 db_name=splited_cmd[1]
              
              if os.path.exists(".\\root\\"+ db_name): #checks if file exists or not
                  print(f"MESSAGE :{db_name} data base already exists")  
             
              else:
                  os.makedirs(".\\root\\"+db_name)  #(.)=for coming out (/)= for adding there 
                                                  # this makes nucleus folder inside root foolder 
                                                  #if you run this and type CREATE_DB NUCLUS
         elif splited_cmd[0] =="CREATE_TABLE": 
             create_table(splited_cmd)

              
         
if __name__=="__main__":
        main()



# for making csv file type CREATE_TABLE STUDENTS INTO Nucleus in terminal