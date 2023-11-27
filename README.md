![image](https://github.com/DennisWainaina/Book-recommendation-system-project/assets/116555573/a7626926-c982-4b1a-bac0-8dc5ecaab791)

# BOOK RECOMMENDATION SYSTEM PROJECT

**Welcome to the Book Recommender System Project**

In Kenya, accessing a diverse range of affordable books has been a challenge, hindering the reading experience for many. *Lonestar Incorporated*, a forward-thinking startup, aims to change this narrative. With funding from Venture Capitalists, *Lonestar Inc.* is launching a website to provide a wide selection of books. To enhance the reading experience, the company has partnered with *Regex Inc.*, a startup specializing in data science. *Regex Inc.* is developing an advanced recommendation system to connect users with books tailored to their preferences. The collaborative effort between *Lonestar Inc.* and *Regex Inc.* seeks to transform the book landscape in Kenya, making diverse reading options accessible to all.

This README.md provides an overview of the project and its segments:
1. [OBJECTIVES](#objectives)
2. [BUSINESS UNDERSTANDING](#business-understanding)
3. [DATA UNDERSTANDING](#data-understanding)
4. [DATA PREPARATION](#data-preparation)
5. [EXPLORATORY DATA ANALYSIS](#exploratory-data-analysis)
6. [MODELLING](#modelling)
7. [CONCLUSION](#conclusion)
8. [RECOMMENDATIONS](#recommendations)

## OBJECTIVES
### 1.1 MAIN OBJECTIVE
To build a model that recommends books to users based on what they have read before and what other users with similar interests have also read and liked.

### 1.2 SPECIFIC OBJECTIVES
-	Design a sophisticated recommendation algorithm for book suggestions.

-	Utilize user profiles, reading history, and user-generated ratings for model training.

-	Ensure diverse book recommendations spanning different genres and interests.

-	Seamlessly integrate the recommendation system into Lonestar Incorporated's website.

-	Monitor and evaluate user engagement metrics, such as click-through rates and page views.

-	Analyze the impact of the recommendation system on book sales and revenue generation.

-	Comply with data protection regulations to safeguard user privacy.

-	Collaborate closely with the website development team for integration.

-	Deploy the recommendation model on the website for real-time book suggestions.

-	Prepare and deliver a comprehensive presentation to the Lonestar Inc. board members showcasing the project's results and impact.

## BUSINESS UNDERSTANDING
### 2.1 PROBLEM STATEMENT
Lonestar Incorporated, a Kenyan startup aiming to revolutionize the book market in Kenya, faces the challenge of providing an exceptional reading experience to their customers. The primary problem is the lack of a book recommendation system on their website. Users currently have no efficient way to discover books tailored to their preferences and reading history. Lonestar Inc. seeks to implement a recommendation system that can suggest books to users based on their previous purchases and ratings by users with similar interests. The problem at hand is to design, build, and deploy an effective book recommendation system that enhances user engagement, drives book sales, and improves the overall reading experience on their website.

### 2.2 MEASURE OF SUCCESS
To achieve as low RMSE as possible.

## DATA UNDERSTANDING
The dataset was sourced from https://maciejkula.github.io/spotlight/datasets/goodbooks.html. It contains various **csv files** as shown below. Here are the various csv files to be used:

### 3.1 RATINGS
We specifically examine this dataset, aiming to understand the distribution of user ratings, explore any trends, and identify potential outliers. This analysis is essential as it forms the basis for our recommendation system.

### 3.2 BOOKS
This dataset contains information about books, including details like book IDs, authors, original publication years, and various ratings and counts related to the books.

### 3.3 TAGS
The dataset contains information about tags, including their unique identifiers and tag names. Tags are commonly used in various contexts for categorizing and labeling items. This dataset is particularly useful for tasks that involve tagging, categorization, and classification.

## DATA PREPARATION

This was to ensure the dataset was in an optimium state for analysis/ modelling. The steps were as follows:

#### Combining Dataframes Using a Common Key

Since each csv file contained its own dataset, the csv files were combined into one dataset known as **combined_df** for easier analysis and modelling.

#### Handling Missing Values

Columns with missing values consisted of less than **6%** of the total values in the dataframe. Hence they were dropped.

#### Checking for Duplicates

The dataframe did not contain any duplicates

#### Checking for Wrong Datatypes

The dataframe did not contain any wrong datatypes

#### Checking for Outliers

The numeric columns in the dataframe exhibit numerous outliers. However, for ID-related columns like id and isbn13, each unique identifier can vary significantly, making it impractical to impose specific ranges. This rationale extends to other ID columns and numerical columns like original_publication_year and the ratings range of 1 to 5. Consequently, outlier removal will not be applied to this dataframe.

#### Feature Engineering

Feature engineering involves creating new features or modifying existing ones to capture valuable information. In this phase, we engineer features to enhance the recommendation system's ability to provide relevant suggestions.

The Data Preparation steps collectively prepare the dataset for the subsequent Exploratory Data Analysis and Modeling phases, ensuring that our analysis is based on clean, structured, and well-prepared data.

## EXPLORATORY DATA ANALYSIS

### Univariate Analysis

#### Top-Rated Books
![image](https://github.com/DennisWainaina/Book-recommendation-system-project/assets/116555573/89ac975a-1490-4d9a-8c04-3425bd08e6ca)
- Eight out of the top ten highest-rated books share the title "Calvin and Hobbes," created between 1985 and 1995, showcasing their exceptional popularity.

#### Books Published Over the Years
![image](https://github.com/DennisWainaina/Book-recommendation-system-project/assets/116555573/88dba430-ff4d-4029-913a-ba7d65bcfec6)
- The dataset indicates an exponential increase in the number of books published annually from 1750 to the 2000s, with a noticeable decline post-2000. Remarkably, books were released as early as 750 AD.

#### Common Book Tags
![image](https://github.com/DennisWainaina/Book-recommendation-system-project/assets/116555573/20ad2c24-2e3e-47e2-ab13-389c13d62ca0)
- The most frequent book tags reveal prevalent themes, providing insights into popular topics within the dataset.

### Bivariate Analysis

#### Correlation Between Ratings and Average Rating
![image](https://github.com/DennisWainaina/Book-recommendation-system-project/assets/116555573/cc33c1d6-001f-489c-8d18-bf0620cea01d)
- Higher average ratings tend to coincide with an increased number of ratings, with the majority falling between 3.5 and 4.5.

#### Impact of Publication Year on Ratings
![image](https://github.com/DennisWainaina/Book-recommendation-system-project/assets/116555573/80051185-3a59-4286-b8be-79170bd5a788)
- Books from the 1300s achieved the highest average ratings, while those from the year 1000 had the lowest.

#### Title Length and Average Rating
![image](https://github.com/DennisWainaina/Book-recommendation-system-project/assets/116555573/a73f8d0c-23e6-419b-9c8a-4e429fbc2197)
- Books with shorter titles, particularly those with less than 50 words, generally receive higher average ratings.

**These findings from the EDA phase offer valuable insights into the dataset, laying the groundwork for subsequent modeling endeavors.**

## MODELLING

### 5.1 Base Model

#### 5.1.1 Base Model Recommendation System
- The base model, utilizing Singular Value Decomposition (SVD), achieved a starting Root Mean Square Error (RMSE) of 0.8745.
- A recommendation system was successfully implemented, providing top book recommendations based on a given book title.

### 5.2 Model 2

#### 5.2.1 Model 2 Recommendation System
- After tuning parameters using GridSearchCV, the SVD model (Model 2) showed an increased RMSE of 0.9316.
- The recommendation system using Model 2 provided top book recommendations based on a given book title.

### 5.3 Model 3

#### 5.3.1 Model 3 Recommendation System
- The CoClustering model (Model 3) displayed the highest RMSE of 0.9463.
- After tuning and implementing parameters, the RMSE improved slightly to 0.9418.
- The recommendation system using Model 3 yielded top book recommendations based on a given book title.

### 5.4 Model 4

#### 5.4.1 Model 4 Recommendation System
- The KNNBasic model (Model 4) resulted in an RMSE of 0.9525.

**In summary, the base model demonstrated a reasonable starting point, but subsequent models and tuning efforts showed mixed results in terms of RMSE. Further exploration and fine-tuning may be necessary to enhance recommendation system performance.**

## CONCLUSION
In this project, we built and evaluated two collaborative filtering recommendation systems for book recommendations using the Surprise library. These systems were based on Singular Value Decomposition (SVD), and we fine-tuned one of the models to optimize its performance.

Key findings and insights from this project include:

- The initial SVD-based model (Model 1) achieved a reasonable Root Mean Square Error (RMSE) of approximately 0.8745, indicating its ability to provide accurate book recommendations based on user ratings.
  
- Model 1 provided meaningful recommendations for books based on user interactions. Users received book suggestions with predicted ratings, enhancing their reading experiences.
  
- Model 2, which was fine-tuned using GridSearchCV, did not yield a lower RMSE, indicating that the initial model performed quite well.

## RECOMMENDATIONS
Based on the insights from this project, here are some recommendations:

1. **Model 1 is a Good Starting Point:** The initial SVD-based model (Model 1) already provides useful book recommendations. Consider using this model as your primary recommendation system since it offers a good balance between accuracy and practical recommendations.

2. **Continual Evaluation:** Keep evaluating your recommendation system with real users. Collect feedback and ratings to fine-tune and enhance the quality of recommendations. 

3. **Explore Content-Based Filtering:** Consider implementing a content-based filtering system that takes into account book attributes, such as genres, authors, and topics. Combining collaborative and content-based filtering can further improve the personalization of recommendations.

4. **Experiment with Hybrid Models:** Explore the possibility of creating hybrid recommendation models that combine collaborative filtering with content-based filtering. This approach can provide a more comprehensive recommendation system by leveraging the strengths of both methods.

5. **Scaling the System:** As your user base grows, you may need to consider how to scale your recommendation system to handle a larger amount of data efficiently. Distributed computing and database optimization could be valuable here.

6. **Data Collection:** Collect additional user and book data, such as user demographics, browsing history, or book attributes, to enhance recommendation quality.

**With continual refininement and experimentation with the recommendation system it will be possible to provide users with the best possible recommendations based on their interests and what other users like.**
