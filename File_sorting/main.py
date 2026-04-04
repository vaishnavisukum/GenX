from pathlib import Path
import schedule
import os
import time

Folder="c:\\Users\\Dell\\Desktop"

def file_sort():
   path=Path(Folder)
   for file in path.iterdir():
    ext=str(file).split(".")
    file_name=str(file).split("\\")

    if len(ext)>1:
       if not os.path.exists(Folder+"\\"+ext[-1]):
         os.makedirs(Folder+"\\"+ext[-1])
         new_location=Folder+"\\"+ext[-1]+"\\"+file_name[-1]
         print("old location :" ,str(file))
         print("New location :",new_location)
         os.rename(str(file),new_location)
       
       else:
        new_location=Folder+"\\"+ext[-1]+"\\"+file_name[-1]
        print("old location :" ,str(file))
        print("New location :",new_location)
        os.rename(str(file),new_location)

def main():
  schedule.every(1).minute.do(file_sort)
  
  while(True):
    schedule.run_pending()
    time.sleep(1)


if __name__ == "__main__":
    main()