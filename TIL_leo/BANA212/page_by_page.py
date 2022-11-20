#Inspired By https://github.com/yjeong5126/glassdoor_data_analyst/blob/master/glassdoor_scraping_selenium.ipynb


import pandas as pd
import numpy as np
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException, StaleElementReferenceException

# Create a function to scrape job postings
def scraping_jobs(keyword):
    
    # Create a list to contain the scraped job posting info
    jobs=[]
    
    # scrape job postings nationwide

    
    # Open Chrome using webdriver
    driver = webdriver.Chrome(r"C:/Users/Haesung Lee/Desktop/VS_Code/glassdoor_scraping/chromedriver.exe")
    
    # Go to the job search page in the Glassdoor
    url = "https://www.glassdoor.com/Job/san-jose-data-scientist-jobs-SRCH_IL.0,8_IC1147436_KO9,23_IP8.htm?radius=50&includeNoSalaryJobs=true"
    driver.get(url)
    driver.maximize_window()
    


    
    # loop until the page reaches the page number you set

    
    # wait until the job postings are completely opened in the screen (4 seconds) 
    time.sleep(4)
    
    # # First click the selected job posting
    #try: 
    #     driver.find_element_by_xpath('//*[@id="MainCol"]/div[1]/ul/li[1]').click()
    #except (NoSuchElementException, StaleElementReferenceException):
    #    pass
    #time.sleep(.5)
    
    # Close the pop-up window to ask you to log in the site
    try:
        driver.find_element_by_xpath('//*[@id="JAModal"]/div/div[2]/span').click()
        print(' x out worked')
    except (NoSuchElementException, StaleElementReferenceException):
        print(' x out failed')
        pass
    


    # Find the job posting elements (about 30 postings) and store into the 'job_buttons'
    job_buttons = driver.find_elements_by_xpath('//*[@id="MainCol"]/div[1]/ul/li')

    # loop for each jop posting
    for job_button in job_buttons:
        
        # Click the job posting
        try:
            job_button.click()
        except (ElementNotInteractableException, StaleElementReferenceException):
            print('Error number 01')
            pass
        
        # Wait for the relevant job posting to be downloaded in the screen
        time.sleep(3)

        # Scrape the name of the company for the posting (check)
        try:
            company = driver.find_element_by_xpath('//*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[1]').text
        except (IndexError, ElementNotInteractableException, StaleElementReferenceException):
            company = ''
            print('Error number 02')
            pass
            
            
        # Scrape the job title (check)    
        try:    
            title = driver.find_element_by_xpath('//*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[2]').text
        except IndexError:
            title = ''
            print('Error number 03')
            
        # Scrape the location of the job (check)    
        try:
            location = driver.find_element_by_xpath('//*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[3]').text
        except IndexError:
            location = ''
            print('Error number 04')
    
        # Scrape the salary information for the job
        try:
            salary = driver.find_element_by_xpath('//*[@id="JDCol"]/div/article/div/div[1]/div/div/div/div/div[1]/div[4]/span').text
        except NoSuchElementException:
            salary = ""
            print('Error number 05')
            
        # Scrape the rating of the company (check)   
        try:
            rating = driver.find_element_by_xpath('//*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[1]/span').text
        except NoSuchElementException:
            rating = ""
            print('Error number 06')
        
        # click the button for the full job description (check)
        try:
            driver.find_element_by_xpath('//*[@id="JobDescriptionContainer"]/div[2]/span').click()
        except (ElementNotInteractableException, StaleElementReferenceException):
            print('Error number 07')
            pass
        time.sleep(3)
            
        # Scrape the job description (check)
        try:
            job_description = driver.find_element_by_xpath('.//div[@class="jobDescriptionContent desc"]').text
        except NoSuchElementException:
            job_description = ''
            print('Error number 08')
            
        # Scrape the company size (check)
        try:
            size = driver.find_element_by_xpath('//*[@id="EmpBasicInfo"]/div[1]/div/div[1]/span[2]').text
        except NoSuchElementException:
            size = ''
            print('Error number 09')
        # Scrape the company type (check)
        
        try:
            c_type = driver.find_element_by_xpath('//*[@id="EmpBasicInfo"]/div[1]/div/div[3]/span[2]').text
        
        except NoSuchElementException:
            c_type = ''
            print('Error number 10')

        # Scrape the company industry (check)
        
        try:
            industry = driver.find_element_by_xpath('//*[@id="EmpBasicInfo"]/div[1]/div/div[4]/span[2]').text
        
        except NoSuchElementException:
            industry = ''
            print('Error number 11')

        
        # Scrape the company sector (check)
        
        try:
            sector = driver.find_element_by_xpath('//*[@id="EmpBasicInfo"]/div[1]/div/div[5]/span[2]').text
        
        except NoSuchElementException:
            sector = ''
            print('Error number 12')
            
            
        # Scrape the company revenue (check)
        
        try:
            revenue = driver.find_element_by_xpath('//*[@id="EmpBasicInfo"]/div[1]/div/div[6]/span[2]').text
        
        except NoSuchElementException:
            revenue = ''
            print('Error number 13')
                
    
        # Put the scraped info from the job posting into the list named 'jobs'
        jobs.append({'company':company, 
                        'title':title, 
                        'location':location, 
                        'salary':salary, 
                        'rating':rating, 
                        'size':size,
                        'c_type':c_type,
                        'industry':industry,
                        'sector':sector,
                        'revenue':revenue,
                        'job_description':job_description})
    

            
    return pd.DataFrame(jobs).to_csv(keyword + '.csv')

