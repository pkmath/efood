<br />
<p align="center">
  <a>
    <img src="https://thetotalbusiness.com/wp-content/uploads/2020/11/efood-the-total-business.png" alt="Logo" width="250" height="150">
  </a>
  <h3 align="center">Insights Analyst Main Assessment</h3>
</p>

# Table of Contents

* [Project Structure](#project-structure)
* [Part I SQL](#part-i–sql)
* [Part II - Analyze Users](#use-the-api)
* [Future Considerations](#future-considerations)

* [Part III - Visualization](#future-considerations)

* [Clone the Application](#clone-the-application)
* [Contributing](#contributing)





# Project Structure


    ├── Efood                    
    │   ├── SQL             # Functionality/features
    │   └── Python          # Testing endpoints  

    


## Part I SQL 



* Dataset created at GCP BigQuery from orders.csv file according to given instructions.

* Query1: part1.sql file in SQL directory.

* Query2: part2.sql file in SQL directory.

* In order to test the above sql queries, please change the dataset's path (efood2023-376511.main_assessment.orders) to yours GCP dataset path.


## Part II - Analyze Users

Python used for the second part of the assessment. I have imported the dataset (orders.csv) in my repo. Make sure to change the path inside the script to your suitable dataset path.

* First I performed exploratory analysis to check the dataset. It consisted from 534,270 rows and 7 columns. There are 121943 unique users across 46 citites and 4 different cuisine types. 

<br />

![pie_chart1](https://user-images.githubusercontent.com/36280746/216691126-ed675005-e0eb-4468-b0ee-e2d797c14311.png)

Looking at the above pie chart, almost 40% are Breakfast orders.

<br />

![pie_chart2](https://user-images.githubusercontent.com/36280746/216691422-e77261a8-e529-415b-9caa-8634669df3f4.png)

The second pie shows the share of users who made even once a Breakfast order versus the users who never ordered Breakfast.

* I created some metrics to better analyze and understand the users:
-Total number of orders per user
-Total breakfast orders per user
-Total Non-breakfast orders per user
-Average amount spent per user 
-Average amount of breakfast orders per user
-Average amount of Non-breakfast orders per user

![hist1](https://user-images.githubusercontent.com/36280746/216692327-c7ba7934-af32-47a8-a744-fce8a1349fa1.png)

Looking at total breakfast orders density, it looks like it follows a left-skewed Gaussian distribution.

![hist2](https://user-images.githubusercontent.com/36280746/216693301-9138051f-56ad-4a1b-9d47-4b0247c9deec.png)

Same conclusion to Non-breakfast orders.

![hist3](https://user-images.githubusercontent.com/36280746/216693717-9c44963e-04db-4149-ade8-231de3a95091.png)

Average breakfast amount Density looks like a mixed distribution, with a first spike to lower values and then a Gaussian on the right side.


![hist4](https://user-images.githubusercontent.com/36280746/216694214-e8bd1ef9-a16b-47fe-90af-4904dba30468.png)

Same conclusion to Non-breakfast amount.


* The group of users who never made a breakfast order is around 54% of total users. I will consider this group the most promising to get involved into breakfast ordering.


![corr1](https://user-images.githubusercontent.com/36280746/216695030-b0a7d415-230f-4093-b6a9-d95cdfa33f8e.png)

At the above plot we can see that total Non-breakfast orders are strongly related to breakfast orders.
This is a strong indicator that users who make orders of different efood cuisines tend to make also breakfast orders.


![line2](https://user-images.githubusercontent.com/36280746/216697224-6fb77ded-2f1e-4274-8102-4ef6da1d0936.png)

Above line plot shows that the share of users who made at least one breakfast order, drops as the Non-breakfast orders increase.
More specifically, the larger number of breakfast users (~30%) made no more than 5 orders to Non-breakfast cuisines.

The above users group that I described is around 38% of total users. This is the target group that I would choose for the marketing campaign. 


## Future Considerations

* Further analysis based on timestamps 
* Order patterns based on the time and day (i.e more breakfast orders during weekends and morning hours).
* Define user patterns based on city location (i.e more breakfast orders at Thessaloniki compared to Volos).
* Weather reports could add value to ordering patterns (increased orders during rainy days).
* Statistical learning models to test and predict users behavior (Linear/Logistic regression).


## Part III - Visualization

![viz1](https://user-images.githubusercontent.com/36280746/216702320-0add1981-df24-42df-90f1-1e46e980ae44.png)


![viz2](https://user-images.githubusercontent.com/36280746/216702546-bbfeda23-6265-4d01-83c7-1fa5c9ff9542.png)



## Clone the Application

``
git clone github.com/pkmath/efood.git
``


## Contributing

1. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
