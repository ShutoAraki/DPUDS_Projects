from flask import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import urllib
from bs4 import BeautifulSoup
from textblob import TextBlob

#Most of the imports above are explained and can be read more in depth about through the README file. 

app = Flask(__name__)
#Create the flask App (the "app" can be called whatever)

#"App.route" creates the routing for which your pages show up (i.e. webapp.com/home or webapp.com/ 
# will will return the function below)
@app.route('/')
@app.route('/home')
def main():

	# render_template will simply open up the specified html file (located in the templates folder) -- home page in this case
    return render_template('/home.html')

#the POST method is used when a form element is used to post data -- in this case
# I am posting the data from the input elements (LinkedIn search)
@app.route('/results', methods=['POST'])
def results():

	#the 5 below lines will start up a chrome driver through selenium, and will allow you to manipulate
	#data on the specified webpage (in this case it will the linkedIn jobs search page using driver.get())
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument("--incognito")
	driver = webdriver.Chrome('/Users/Taras/bin/chromedriver', chrome_options=chrome_options)
	driver.get("https://www.linkedin.com/jobs")
	url = driver.current_url
	newURL = urllib.parse.unquote(url)
	#above line will escape the problem with having % in a URL

	if newURL != "https://www.linkedin.com/jobs/?trk=jobs-home-jobsfe-redirect":

		#not currently working, but will return the function specified below if it prompts me to sign In
		return redirect(url_for('signinResults'))
		
	else:
		assert "in" in driver.title

		#find the input element where you type in the Job Title
		elem = driver.find_element_by_name("keywords")

		#now find the location input element (and clear what is already on there)
		elem2 = driver.find_element_by_class_name("location-clear-icon")
		elem3 = driver.find_element_by_name("location")

		#retrieve the job and location search queries that the user specified on the page
		jobSearch = request.form['job']
		locSearch = request.form['loc']
		jobType = request.form['jobType']
		numResults = request.form['numRes']
		

		print("Running a search on the position of " + jobSearch + " in " + locSearch + ".")
		elem2.click()

		#now send the queries to the linkedIn page and type it in
		elem.send_keys(jobSearch)
		elem3.send_keys(locSearch)
		elem.send_keys(Keys.RETURN) #will click search

		#list of Languages that are relatively popular -- current method but might change
		plList = ['Java','C','C++','C#','Python','PHP','Javascript','Visual Basic', 'VB','.NET','Perl','Ruby',
		'R','Delphi','Swift','Assembly','Go','Objective-C','PL','SQL','Scratch','Dart','SAS','D','COBOL',
		'Ada','Erlang','Lisp','Prolog','LabVIEW', 'HTML','CSS','JQuery','ASP','Groovy','Clojure','Script','Node','Mongo']

		#find the job result
		linkElements = driver.find_elements_by_class_name("job-title-link")
		links = []

		#iterate through each job result and grab the link to that Job posting -- then append to links array
		for a in linkElements:
			linkHref= a.get_attribute("href")
			links.append(linkHref)

		#time.sleep(3)
		#driver.back()
		i=1

		#create the barebones of a dataframe where the job content will go into
		frame = pd.DataFrame( columns=[i], index=['Job Title', 'Company', 'Languages', 'Total Langs'])
		frame2 = pd.DataFrame(columns=[i], index=['Job Title', 'Company', 'Languages', 'Total Langs']) 

		#now in the links array created above, iterate through and open up each link (the driver.get() line )
		for link in links:
			driver.get(link)

			#will parse through all the HTML data on that page
			soup = BeautifulSoup(driver.page_source, "html.parser")

			#find the specific div element where the job description and details are located
			jobDesc = soup.find("div", class_="description-section").text
			
			#put into a textBlob 
			blob = TextBlob(jobDesc)

			#grab the jobTitle and companyName  element text
			jobTitle = driver.find_element_by_tag_name("h1").text
			companyName = driver.find_element_by_class_name("company").text

			companies = []
			companies.append(companyName)

			jobs = []
			jobs.append(jobTitle)
			
			languages = []

			count = 0 # of languages in each job posting

			#loop through each language in the list of languages and check if in textBlob. If so, append to array
			for lang in plList:
				if lang not in blob:
					continue
				elif lang in blob:
					languages.append(lang)
					count = count + 1

			jobs = ''.join(jobs)
			companies = ''.join(companies)
			languages = ', '.join(languages)

			#take out of individual arrays and put into finalArr
			finalArr = []
			finalArr.append(jobs)
			finalArr.append(companies)
			finalArr.append(languages)
			finalArr.append(count)
			if i > 13:
				frame2[i] = finalArr
			else:

			#set frame[i] (i = the id/result number from job search) = to finalArray
				frame[i] = finalArr

			
			if request.form['numRes']=='10':
				if i == 10:
					frame = frame.to_html()
					return render_template("/results.html", table=frame)
			i = i + 1

		if request.method == 'POST':

			frame = frame.to_html()
			frame2 = frame2.to_html()

			#send frame to results.html
			return render_template("/results.html", table=frame, table2= frame2)

# @app.route('/results', methods=['POST'])
# def signinResults():
# 	print("hello")
# 	driver = webdriver.Chrome('/Users/Taras/bin/chromedriver')
# 	signIn = urllib.parse.unquote("https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fjobs%2F%3Ftrk%3Djobs-home-jobsfe-redirect&fromSignIn=true&trk=uno-reg-join-sign-in")
# 	driver.get(signIn)
# 	email = driver.find_element_by_name("session_key")
# 	email.send_keys("")
# 	pwd = driver.find_element_by_name("session_password")
# 	pwd.send_keys("")
# 	signInBtn = driver.find_element_by_name("signin")
# 	signInBtn.click()
# 	input1 = driver.find_element_by_xpath("//input[@placeholder='Search jobs by title, keyword or company']")
# 	input2 = driver.find_element_by_xpath("//input[@placeholder='City, state, postal code or country']")
# 	search = driver.find_element_by_class_name("button-secondary-large-inverse")
# 	jobSearch = request.form['job']
# 	locSearch = request.form['loc']
# 	input1.send_keys(jobSearch)
# 	input2.send_keys(locSearch)
# 	search.click()

# 	plList = ['Java','C','C++','C#','Python','PHP','Javascript','Visual Basic', 'VB','.NET','Perl','Ruby',
# 	'R','Delphi','Swift','Assembly','Go','Objective-C','PL','SQL','Scratch','Dart','SAS','D','COBOL',
# 	'Ada','Erlang','Lisp','Prolog','LabVIEW', 'HTML','CSS','JQuery','ASP','Groovy','Clojure','Script','Node','Mongo']
	
# 	linkElements = driver.find_elements_by_class_name("job-title-link")
# 	links = []

# 	for a in linkElements:
# 		linkHref= a.get_attribute("href")
# 		links.append(linkHref)
# 	#time.sleep(3)
# 	#driver.back()

# 	i=1
# 	frame = pd.DataFrame( columns=['Job Title', 'Company', 'Languages', 'Total Langs'], index=[i])

# 	for link in links:
# 		driver.get(link)
# 		#jobDesc = driver.find_element_by_class_name("description-section")
# 		soup = BeautifulSoup(driver.page_source, "html.parser")
# 		jobDesc = soup.find("div", class_="description-section").text
# 		blob = TextBlob(jobDesc)
# 		#jobTitle1 = urllib.parse.unquote("h1.jobs-details-top-card__job-title.Sans-21px-black-85%-dense")
# 		jobTitle = driver.find_element_by_tag_name("h1").text
# 		companyName = driver.find_element_by_class_name("company").text
# 		companies = []
# 		companies.append(companyName)
# 		print(companies)
# 		#print(jobTitle.text) #works -- prints job title
# 		jobs = []
# 		jobs.append(jobTitle)
# 		#print(jobs)
		
# 		languages = []

# 		count = 0
# 		for lang in plList:
# 			if lang not in blob:
# 				continue
# 			elif lang in blob:
# 				languages.append(lang)
# 				count = count + 1
# 		jobs = ''.join(jobs)
# 		companies = ''.join(companies)
# 		languages = ', '.join(languages)
# 		finalArr = []
# 		finalArr.append(jobs)
# 		finalArr.append(companies)
# 		finalArr.append(languages)
# 		finalArr.append(count)
# 		frame[i] = finalArr
# 		print(frame.to_html())

# 		#print(frame)
# 		i = i + 1

# 	if request.method == 'POST':
# 		frame = frame.to_html()
# 		return render_template("/results.html", table = frame)

def before_request():
    app.jinja_env.cache = {}

@app.route('/indeed')
def indeed():
	return render_template("/indeed.html")

@app.route('/glassdoor')
def glassdoor():
	return render_template("/glassdoor.html")
	
@app.route('/about')
def about():
	return render_template("/about.html")



if __name__ == '__main__':
	app.before_request(before_request)
	
	app.run()