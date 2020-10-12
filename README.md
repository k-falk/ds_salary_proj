
<!--
*** Thanks for checking out this README Template. If you have a suggestion that would
*** make this better, please fork the repo and create a pull request or simply open
*** an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->





<!-- PROJECT SHIELDS -->





  <h3 align="center">Glassdoor Salary Project</h3>

  <p align="center">
    Predicting 'data scientist' salary using glassdoor job postings
    <br />
    <a href="https://github.com/k-falk/ds_salary_proj"
    ><strong>Explore the docs »</strong></a>
    <br />
    <br />
    ·
    <a href="https://github.com/k-falk/ds_salary_proj/issues">Report Bug</a>
    ·
    <a href="https://github.com/k-falk/ds_salary_proj/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## About The Project

This is a data science project to analyze and predict the estimated salary of data scientist jobs on Glassdoor. I have done everything from scraping the data on glassdoor to building regression models to make salary predictions off the sata. 


### Built With
This project was done completely in python. The data scraping was done using Selenium. The data analysis was done using Pandas. And the machine learning modeling was done with sklearn. 
* [Selenium](https://www.selenium.dev/)
* [Pandas](https://pandas.pydata.org/)
* [Sklearn](https://scikit-learn.org/stable/)


<!-- Data Scraping-->
## Data Scraping

The data scraping was done using selenium. I used [this](https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905) glassdoor selenium scraper to do so. 
After scraping, here is the information we got: 
* Job Title
* Glassdoor Salary Estimate
* Job Description
* Rating
* Company Name
* Location
* Headquarters
* Company Size
* Year Company Founded
* Type of Ownership
* Industry
* Sector
* Revenue
* Competitors

<!-- Data Cleaning-->
## Data Cleaning
Unfortunately, I our data was somewhat incomplete. Some of the things we scraped were not available to us. Notably, number of competitors and headquarters was unable to be scraped using the scraper we used. 

Other things we did include:
Getting the company age from year founded, getting the average salary from the glassdoor salary range, getting simplified titles from the job names, and pulling out information from the job description such as different skills listed. 

<!-- EDA-->
## EDA

Our exploratory analysis gave us some insight into the data. We looked at the distributions of our variables and the average salaries of each title. We also did some data visualization such as mapping job locations and salaries on a map. The jupyter notebook can be found [here](https://github.com/k-falk/ds_salary_proj/blob/master/eda.ipynb)

Here are some highlights:

![Salary By Position Boxplot](https://github.com/k-falk/ds_salary_proj/blob/master/salary_title_boxplot.PNG)

![Corr Map](https://github.com/k-falk/ds_salary_proj/blob/master/corr_map.PNG)

![Statemap](https://github.com/k-falk/ds_salary_proj/blob/master/statemap.PNG)

![Salary by Title Pivot](https://github.com/k-falk/ds_salary_proj/blob/master/title_salary_pivot.PNG)

![Title Barchart](https://github.com/k-falk/ds_salary_proj/blob/master/title_barchart.PNG)
<!-- Model building -->
## Model building

For our model building, we used sklearn and its cross_val_score function to evaluate each model. We tried the following models and picked the best one: 
* Linear Regression
* Lasso Regression
* Random Forest
* Elastic Net
* K Neighbors
* Decision Tree
* Gradient Boosting

After running our models, the clear winner was Gradient Boosting with a MAE of 19.7. 

We then ran a Grid Search on that model to see if we can tune it for better results. After running Grid Search we were able to get that number down to 19.2


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Kevin Falk - [LinkedIn](in-k-falk) - [Github](github.com/k-falk) 
kevin.falk.631@gmail.com

Project Link: [https://github.com/k-falk/ds_salary_proj](https://github.com/k-falk/ds_salary_proj)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Glassdoor Selenium Scraper](https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905)
* [Ken Jeong's Similar Scraping Project](https://github.com/PlayingNumbers/ds_salary_proj) Inspiration was taken from this project and I used the same selenium scraper 
* [Stack Overflow](https://stackoverflow.com/) (A lot of stackoverflow was used on this project :) )
* 




