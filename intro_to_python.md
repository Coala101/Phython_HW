# Introduction to Python
## Exercise 1
### a
- print("Hello World!")
- Hello World!
### b
- my_text="Hello World!"
- print(my_text)
- Hello World!

## Exercise 2
### a
- glass_of_water=3
- print("I drank", glass_of_water, "glasses of water today.")
- I drank 3 glasses of water today.
### b
- glass_of_water
- 3
- glass_of_water=glass_of_water + 1
- print(glass_of_water)
- 4

## Exercise 3
### a
- men_stepped_on_the_moon=7
- print(men_stepped_on_the_moon)
- 7
### b
- my_reason_for_coding="Hello Niko"
- print(my_reason_for_coding)
- Hello Niko
### c
- global_mean_sea_level_2018=21
- global_mean_sea_level_2018=global_mean_sea_level_2018 + 0.36
- print(global_mean_sea_level_2018)
- 21.36

## Exercise 9
### a
- str="It's always darkest before dawn."
- print(str)
- It's always darkest before dawn.
### b
- print(str)
- It's always darkest before dawn.
- ans_1=str[0]+str[2]+str[-1]
- print(ans_1)
- I'.
### c
- print(str)
- It's always darkest before dawn.
- str.replace(".","!")
- "It's always darkest before dawn!"
- print(str)
- It's always darkest before dawn.

## Exercise 10
### a
- lst=[11, 10, 12, 101, 99, 1000, 999]
- answer_1=len(lst)
- print(answer_1)
- 7
### b
- msg="Be yourself, everyone else is taken."
- msg_length=len(msg)
- print(msg_length)
- 36
### c
- dict={"Real Madrid": 13,"AC Milan": 7,"Bayern Munich":5 ,"Barcelona": 5, "Liverpool": 5}
- ans_1=len(dict)
- print(ans_1)
- 5

## Exercise 11
### a
- lst=[11, 100, 99, 1000, 999]
- lst.sort()
- print(lst)
- [11, 99, 100, 999, 1000]
### b
- lst=["Ukraine", "Japan", "Canada", "Kazakhstan", "Taiwan", "India", "Belize"]
- lst.sort()
- print(lst)
- ['Belize', 'Canada', 'India', 'Japan', 'Kazakhstan', 'Taiwan', 'Ukraine']
### c
- lst=[11, 100, 101, 999, 1001]
- lst.sort(reverse = True)
- print(lst)
- [1001, 999, 101, 100, 11]

## Exercise 11
### a
- lst=[11, 100, 99, 1000, 999]
- popped_item=lst.pop()
- print (popped_item)
- 999
- print(lst)
- [11, 100, 99, 1000]
### b
- lst=["milk", "banana", "eggs", "bread", "broccoli", "lemons"]
- item=lst.pop(-2)
- print(lst, item)
- ['milk', 'banana', 'eggs', 'bread', 'lemons'] broccoli
### c
- GDP_2018={"US": 21, "China": 16, "Japan": 5, "Germany": 4, "India": 3, "France": 3, "UK": 3, "Italy": 2}
- italy_gdp=GDP_2018.pop("Italy")
- print (GDP_2018)
- {'US': 21, 'China': 16, 'Japan': 5, 'Germany': 4, 'India': 3, 'France': 3, 'UK': 3}
- print(italy_gdp, "trillion USD")
- 2 trillion USD