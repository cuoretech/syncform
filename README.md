SyncForm
========

#### Coordination Efficiency Platform

## <a name='TOC'>Table of Contents</a>

  1. [Intro](#intro)
  2. [High Level Description](#high-level-dis)
  3. [Overview](#overview)

## <a name='intro'> Intro

Cuore's Coordination Efficiency Platform, a set of web services developed in the the "Unholy Trinity" Python, Neo4j and Pyramid Web Framework. ([@CuoreTech](https://twitter.com/CuoreTech))

## <a name='high-level-dis'> High Level Description
* The event that we are going to describe involves a user that goes shopping any day of the week. We will suppose that this user has already enrolled in the Cuore system and is following a workout plan. Along with this plan, in order to improve his performance, he has also started following a diet that he found on one of the Cuore servers. (For example, another user from New York that, as a nutritionist, offers sample diet plans online for our systems to promote her business). This new diet involves a very strict regime that our sample user is not yet familiarized with. 

* Let us suppose that this new user is driving on his way back home. He wants to stop for groceries, but he doesn’t know where would be the most convenient place for him. The first thing that he does is to check what ingredients he needs to buy for tonight’s dinner. After a quick view, he sees that the only ingredients that he needs are a box of almond milk and some bread. The system checks the surrounding area and sees that there are two stores in Cuore’s system that offer these items: Safeway and Trader Joe’s. But the system also sees that our user cannot buy any given bread, due to the fact that he is gluten-intolerant. After checking the inventory, the system rules out every non gluten-free item, and only Safeway is left. Therefore, the user is lead to that supermarket. 

* Once in the supermarket, the system displays the different ingredients that our user needs to buy. Due to the fact that there is no restriction on the almond milk, the system will merely display this ingredient as “Almond milk”, giving the user the option to generate a recommendation by clicking the icon if he wishes. On the other hand, due to the restriction on the bread, the system will display a special icon on the user’s screen providing the brand image and name of the particular bread that he must buy. 

* Once the user buys these items, he can mark them as such in the system. The system will then calculate the average consumption rate that this particular user will consume these items under the diet that he is following and, when the time comes, it will generate a notification warning the user that he is running low on this particular item.


## <a name='overview'> Overview

* Before we engage in the system functioning, let us have an overall look at the complete system structure and see the different components and modules of our framework.

* The database is the main component and core of our system. It is where all the synchronization and coordination takes place and the entire system relies upon it. Our system is currently implemented using neo4j, a graph database specially design to exploit the power of data relationships and to optimize data mining and recommendation queries. We will have two main different type of database clusters in our system.

* User database: This is the database that each user will have access to, their own personal database. No matter if it is a large corporation or a single person, they will each have these models of databases. The user will be able to specify what data he or she wants to make public, what data is to be shared with a specific group of users or what data must remain private. 

* Type database: This are the databases that will be controlled by Cuore. These data servers will not hold any personal or business-related data, but only item types. For example, if Safeway introduces a new item that it’s half bread, half fruit, they will have to select a subcategory in which to include that item (either fruit or bread or both.) Once the system provides them with a pre-specified item type, they will be able to include it in their own database. The purpose of these servers is to provide a standardized nomenclature for item-naming and classification throughout the system. New item types can be included if requested, but only after being approved by the Cuore team. 

* More information and detailed architecture can be found in the Data Model Design document.
