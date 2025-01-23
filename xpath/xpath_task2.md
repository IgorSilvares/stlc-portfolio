## Task 2

Go the https://grocerymate.masterschool.com 

1. Write the XPath for the highlighted icon/button given in the image below.

![image1](https://github.com/user-attachments/assets/2943ea31-e73a-4b07-9f94-af043f6daa51)

2. Now, open https://grocerymate.masterschool.com/auth. 

![image2](https://github.com/user-attachments/assets/b657a2e6-bb8f-49e9-9b1b-26f5384802e3)

Write the XPath of all input fields, sign in button, Create a new account link, and Go to Home link

3. Now, on the same link as in Part 2, click on Create a new account, you will see the following UI:

![image3](https://github.com/user-attachments/assets/908631b1-8bea-4925-9956-5b7f6ff059d1)

Write the XPath for all input fields, Sign Up button.

4. Go to https://grocerymate.masterschool.com/store, you will see the following UI:
   
![image4](https://github.com/user-attachments/assets/dd1b0943-40d1-4228-935f-d2c4feb18e55)

Write the XPath of **Confirm** button which you can see in the Modal. 

5. Go to the **Shop** page, write the XPath for quantity input of Oranges, Add to cart button for Oranges, and add to wish list for Oranges


# Solutions

## 1. Header Icon
- //div[@class='headerIcon'][1]

## 2. Login Form
- Email: //form/input[@type='email']
- Password: //form/input[@type='password']
- Submit Button: //form/button[@type='submit']

### Links
- Create a New Account link: //a[@class='switch-link']
- Go to Home link: //a[@class='home-link']

## 3. Sign Up Form
- Full Name: //input[@type='text']
- Email address: //input[@type='email']
- Password: //input[@type='password']
- Sign Up button: //button[@class='submit-btn']

## 4. Confirm Button
- Confirm Button: //button[text()='Confirm']

## 5. Oranges
- Quantity input of Oranges: //img[@alt='Oranges']/ancestor::div[@class='card']//input[@type='number']
- Add to cart button for Oranges: //img[@alt='Oranges']/ancestor::div[@class='card']//button[@class='btn btn-primary btn-cart']
- Add to wish list for Oranges: //img[@alt='Oranges']/ancestor::div[@class='card']//button[@class='btn btn-outline-dark ']
