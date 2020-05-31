on=0
off=0
task1=input("Enter what you want to do with Fan Switch: On or off? ")
while(task1.lower !="quit"): 
  if (task1.lower()=="quit"):
    break
  elif task1.lower()=='on':
    if (on):
      print ("Fan is already ON")
    else:
      print ("Fan is switched ON")
      on=1
      off=0
  elif task1.lower()=='off':
    if (off):
      print ("Fan is already OFF")
    else:
      print ("Fan is switched OFF")
      off=1
      on=0
  task1=input("Enter what you want to do with Fan Switch: On or off ? ")
