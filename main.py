import linuxTUI
import cloudfrontcliaws
import clienthadoop
import pyttsx3
import os
import speech_recognition as sr

pyttsx3.speak("\t\t\tWelcome to my tools")
print("\t\t\tWelcome to my tools")
print("\t\t\t-------------------")
r=sr.Recognizer()
while True:
	with sr.Microphone() as source:
		print("Start saying..")
		audio = r.listen(source)
		print("\t\t\twe got it, plz wait....")

	ch=r.recognize_google(audio)

	if ("hello" in ch):
		pyttsx3.speak("hello user")
		pyttsx3.speak("What can I do for you")
	elif ("Tell" in ch or "tell" in ch or "me" in ch ) and ("about" in ch or "yourself" in ch):
		pyttsx3.speak("I am your tech friend and will help u to know about some linux commands , docker , hadoop , Amazon Web Services (AWS) ")
		print("\t\t\tLearn some basic commands of linux")
		print("\t\t\tOperate the docker tool with your voice")
		print("\t\t\tLearn hadoop through your voice")
		print("\t\t\toperate the AWS services with your voice")
		print("\t\t\tsay exit to close the program") 
	elif (("learn" in ch) or ("interested" in ch)) and (("linux" in ch) or ("Linux" in ch)):
		pyttsx3.speak("That's great")
		linuxTUI.linux()
	elif (("learn" in ch) or ("interested" in ch) or ("operate" in ch)) and (("docker" in ch) or ("Docker" in ch)):
		pyttsx3.speak("Nice choice , let's move to docker")
		dockertui.docker()
	elif (("learn" in ch) or ("interested" in ch) or ("operate" in ch)) and (("aws" in ch) or ("AWS" in ch) or ("Amazon" in ch)):
		pyttsx3.speak("Amazon Web Services (AWS) is the world's most comprehensive and broadly adopted cloud platform, offering over 175 fully featured services from data centers globally.")
		cloudfrontcliaws.aws()
	elif (("learn" in ch) or ("interested" in ch) or ("operate" in ch)) and (("hadoop" in ch) or ("Hadoop" in ch)):
		pyttsx3.speak("Hadoop is an open-source software framework for storing and processing Big data and running applications on clusters of commodity hardware. ")
		clienthadoop.hadoop()
	elif ("exit" in ch) or ("close" in ch):
		exit()
	a=input("press enter to continue...")
	os.system("cls")

