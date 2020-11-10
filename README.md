# StripeMe

## Introduction

Stripe Me is an e-commerce and portfolio website about web-development and design services. This project is a Python-Django web application, backed by a Postgres and squlite3 database, and deployed via the Heroku PaaS. Stripe Me uses the Stripe Checkout API (in testing mode: not currently taking real card payments) and is a lightweight, responsive website designed with the Bootstrap Grid Systems.  

-   [View the Stripe Me Heroku App](https://kika-stripe-me.herokuapp.com/)
-   [View the repository on GitHub](https://github.com/kescardoso/stripeme)
  
As you read this document, you will find my complete development process, from UX strategy to deployment. Thank you for reading! -- [Kes Cardoso](https://github.com/kescardoso)

![](https://raw.githubusercontent.com/kescardoso/stripeme/master/media/project-present.png)

## Contents table

1.  [UX](https://github.com/kescardoso/stripeme#ux)
    
    -   [Wireframe](https://github.com/kescardoso/stripeme#wireframe)
        
    -   [User and Their Goals](https://github.com/kescardoso/stripeme#user-and-their-goals)
	    - [User Avatar](https://github.com/kescardoso/stripeme#user-avatar)
	    - [User's Main Challenges](https://github.com/kescardoso/stripeme#users-main-challenges)
	    - [User Stories](https://github.com/kescardoso/stripeme#user-stories)
        
2.  [Features](https://github.com/kescardoso/stripeme#features)
    
    -   [Existing Features](https://github.com/kescardoso/stripeme#existing-features)
        
    -   [Features Left to Implement](https://github.com/kescardoso/stripeme#features-left-to-implement)
        
3.  [Technologies Used](https://github.com/kescardoso/stripeme#technologies-used)
    
4.  [Testing](https://github.com/kescardoso/stripeme#testing)
    
5.  [Deployment](https://github.com/kescardoso/stripeme#deployment)
    
6.  [Credits](https://github.com/kescardoso/stripeme#credits)
    

## UX

### Wireframe

Link to the wireframe on [Figma](https://www.figma.com/file/onwkxg3NFMtijcRfl83X8N/StripeMe?node-id=0%3A1)

### User and Their Goals

Since Covid-19 became a global pandemic, many people around the world began to live through lockdowns. Many began to work from home; others lost their jobs. With uncertainty becoming a norm, we can't know when, or if, our societies will return to normal and what consequences the pandemic will leave behind.

Overall, Covid-19 has normalized remote work, and a significant part of our global population is looking for online alternatives for their income: either by creating a new online entrepreneurial project, or by improving the one already in place, or by transferring their main activity from a physical, local organization to an online shop.

For many people, including artists, artisans, small business owners or independent contractors this technological transition can be challenging and expensive, specially during these troubling times.

Stripe Me provides easy and straightforward web-development, graphic design and digital marketing consultancy services for English-speaking users around the world (payments in US dollar). This project gears towards freelancers, entrepreneurs, and small to medium business alike, leveraging their online inception and profits during pandemic crisis.

Here, available services are already formatted and able to be personalized: they are presented with a starter model and options, and the user can customize their order in terms of color scheme, dimensions, and content. Consultancy sessions are also available for users who wish to have higher control and a more professionally involved approach to their digital business development. By setting up basic formats and options that can be personalized, Stripe Me keeps prices affordable and delivery time optimized, and is therefore a great digital services provider for the pandemic times.

#### User Avatar

- Cross-cultural English-speaking men and women, affected or not by Covid-19;
- Freelancers, entrepreneurs, small business owners looking for online alternatives for their jobs of entrepreneurial projects;
- Travelers, digital nomads, independent culture and art contractors, without a business address and interested in building an online presence for their income activities.

#### User's Main challenges

Some of the main challenges regular people and non-technical professionals encounter are:

- They find websites hard to understand and to build.
- They don't have time to learn new technologies.
- Their budget is limited due to current Covid-19 and the economic crisis.
- They rely on free or limited website building services, but they miss the UX and development quality they desire.
- They are not sure what they need in technological terms, and they appreciate guidance.
- They need a personalized e-commerce project that still keeps features basic and affordable.
- They feel intimidated by traditional digital agencies, and they prefer a more friendly, one-to-one approach.

#### User Stories

![](https://raw.githubusercontent.com/kescardoso/stripeme/master/media/user-stories.png)

## Features

### Existing Features

1. **Navbar:** contains the logo, search box, and links to access user profile and shopping bag.
2. **Menu:** just under the main nav, the menu contains links for easy access to services and portfolio pages, in lists by category, price, rating, and name.
3. **Search Box:** dynamic search connected to the database.   
4. **Discount Banner:** it is a notification system on the home page, as well as on the checkout toast and bag page, to tell users that they can get 10% off when total purchase is $500 or more.
5. **Service Option Fields:** on each service detail page, there are boolean fields with color scheme, dimensions and user message options to be entered by the user. These are used to send information to the owner about desired user's customizations addressed to that service. The fields color and dimensions are not dynamic and currently in development.