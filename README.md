# StripeMe

## Introduction

Stripe Me is an e-commerce and portfolio website offering communication services, including web-development, graphic design and branding consultancy. 

-   [View the Stripe Me Heroku App](https://kika-stripe-me.herokuapp.com/)
-   [View the repository on GitHub](https://github.com/kescardoso/stripeme)

![](https://raw.githubusercontent.com/kescardoso/stripeme/master/media/project-present.png)

This is my final project of four Milestone Projects that make up the Full-Stack Web Development Diploma Training at Code Institute. Project main requirements are: to build a full-stack website with the use of HTML, CSS, JavaScript, Python, Django and a relational database; as well as the implementation of a checkout functionality, which has been achieved through the use of Stripe.

Stripe Me is therefore a Python-Django web application, backed by a PostgreSQL (and SQLite3) database, and deployed via the Heroku PaaS. This project uses the Stripe Checkout API (for educational purposes only: not currently taking real card payments) and is styled using the Bootstrap Grid System. 

**NOTE:** If you would like to test the payment functionality of this project, please create an account and use the card number 4242 4242 4242 4242 with any address details, expiry date and CVC that you choose.

[Click here to view the project live.](https://kika-stripe-me.herokuapp.com/)
  
As you read this document, you will find my complete development process, from UX strategy to deployment. Thank you for reading! -- [Kes Cardoso](https://github.com/kescardoso)

## Contents table

 - [UX](https://github.com/kescardoso/stripeme#ux)
	 - [Wireframe](https://github.com/kescardoso/stripeme#wireframe)
	 - [Color Palette](https://github.com/kescardoso/stripeme#color-palette)
	 - [App Logo](https://github.com/kescardoso/stripeme#app-logo)
 - [User Stories](https://github.com/kescardoso/stripeme#user-stories)
	 - [User and Their Goals](https://github.com/kescardoso/stripeme#user-and-their-goals)
	 - [User Avatar](https://github.com/kescardoso/stripeme#user-avatar)
	 - [User's Main Challenges](https://github.com/kescardoso/stripeme#users-main-challenges)
 - [Database Structure](https://github.com/kescardoso/stripeme#database-structure)
 - [Features](https://github.com/kescardoso/stripeme#features)
	 - [Existing Features](https://github.com/kescardoso/stripeme#existing-features)
	 - [Features Left to Implement](https://github.com/kescardoso/stripeme#features-left-to-implement)
 - [Technologies Used](https://github.com/kescardoso/stripeme#technologies-used)
 - [Testing](https://github.com/kescardoso/stripeme#testing)
 - [Deployment](https://github.com/kescardoso/stripeme#deployment)
 - [Credits](https://github.com/kescardoso/stripeme#credits)

## UX

### Wireframe
Link to the wireframe on [Figma](https://www.figma.com/file/onwkxg3NFMtijcRfl83X8N/StripeMe?node-id=0%3A1)

### Color Palette
![enter image description here](https://raw.githubusercontent.com/kescardoso/stripeme/master/media/color-palette.png)

### App Logo
*Stripe Me Favicon*
![enter image description here](https://raw.githubusercontent.com/kescardoso/stripeme/master/media/SripeMe-Favicon.png)

## User Stories
*Click on the image to see it larger:*
![](https://raw.githubusercontent.com/kescardoso/stripeme/master/media/user-stories.png)


### User and Their Goals

Since Covid-19 became a global pandemic, many people around the world began to live through lockdowns. Many began to work from home; others lost their jobs. With uncertainty becoming a norm, we can't know when, or if, our societies will return to normal and what consequences the pandemic will leave behind.

Overall, Covid-19 has normalized remote work, and a significant part of our global population is looking for online alternatives for their income: either by creating a new online entrepreneurial project, or by improving the one already in place, or by transferring their main activity from a physical, local organization to an online shop.

For many people, including artists, artisans, small business owners or independent contractors this technological transition can be challenging and expensive, specially during these troubling times.

Stripe Me provides easy and straightforward web-development, graphic design and digital marketing consultancy services for English-speaking users around the world (payments in US dollar). This project gears towards freelancers, entrepreneurs, and small to medium business alike, leveraging their online inception and profits during pandemic crisis.

Here, available services are already formatted and able to be personalized: they are presented with a starter model and options, and the user can customize their order in terms of color scheme, dimensions, and content. Consultancy sessions are also available for users who wish to have higher control and a more professionally involved approach to their digital business development. By setting up basic formats and options that can be personalized, Stripe Me keeps prices affordable and delivery time optimized, and is therefore a great digital services provider for the pandemic times.

### User Avatar

- Cross-cultural English-speaking men and women, affected or not by Covid-19;
- Freelancers, entrepreneurs, small business owners looking for online alternatives for their jobs of entrepreneurial projects;
- Travelers, digital nomads, independent culture and art contractors, without a business address and interested in building an online presence for their income activities.
        
### User's Main challenges

Some of the main challenges regular people and non-technical professionals encounter are:

- They find websites hard to understand and to build.
- They don't have time to learn new technologies.
- Their budget is limited due to current Covid-19 and the economic crisis.
- They rely on free or limited website building services, but they miss the UX and development quality they desire.
- They are not sure what they need in technological terms, and they appreciate guidance.
- They need a personalized e-commerce project that still keeps features basic and affordable.
- They feel intimidated by traditional digital agencies, and they prefer a more friendly, one-to-one approach.

## Database Structure

Stripe Me is built on Django, and primarily uses the SQLite3 database during all development stages. Through the deployment to Heroku, the database was changed to a PostgresSQL database as that is provided by Heroku as an add-on for production.

The Django’s default user model for authorization is also in use, which allows the project to meet one of the main requirements of separating features by anonymous users, users in session and superusers.

The structure of the Checkout and Services apps are inspired by one of Code Institute's mini projects: _Boutique Ado_.

The main database structure models are documented below.

#### Profiles App -- **UserProfile Model**

| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | --- 
 User | user | OneToOneField 'User' |  on_delete=models.CASCADE
 Phone number | default_phone_number | CharField | max_length=20, null=True, blank=True
 Address Line1 | default_street_address1 | CharField | max_length=80, null=True, blank=True
 Address Line2 | default_street_address2 | CharField | max_length=80, null=True, blank=True
 Postcode | default_postcode | CharField | max_length=20, null=True, blank=True
 Town/City | default_town_or_city | CharField | max_length=40, null=True, blank=True
 County | default_county | CharField | max_length=80, null=True, blank=True
 Country | default_country | CountryField | blank_label='Country', null=True, blank=True

 