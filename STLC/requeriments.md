## **The Software**

Webshop with the following basic functionalities:

- Register and login functionality
- Searching for products, sorting on price, categories of products
- Add products to favorites
- Add products to basket
- Check-out process: billing and sending information in a form, choose payment method. Calculation of costs (calculate total price)

## New Features

### **1. Product Rating System**

**Vague Requirement:** 
- Users should be able to rate products with a 5-star system and have the option to add written feedback.

**Questions:**
1. Can users edit or delete their ratings and feedbacks after submission?
2. What happens if a user tries to submit feedback without providing a rating?
3. How is the written feedback field validated (character limit, forbidden words, etc.)?
4. Where will the user find the product rating functionality?
5. Who can submit a rating?

**Detailed Requirement:**
The product rating system should allow users to rate products using a 5-star system and optionally add written feedback. Users should be able to edit or delete their ratings and feedback after submission. The feedback field must be validated to ensure it does not exceed a set character limit (e.g., 500 characters) and does not contain forbidden words. The rating functionality should be prominently located on the product page, near the product description, and only registered users who have purchased the product should be able to submit ratings and feedback.

### **2. Age Verification for Alcoholic Products**

**Vague Requirement:** 
- Alcoholic products require age verification. A modal should appear when navigating to the alcoholic products category asking if the user is 18+. Users must input their age before accessing the alcoholic products.

**Questions:**
1. What is the user experience for those who fail the age verification?
2. Where will the message asking for the user's age be displayed?
3. How will the system store the data from the user's age verification?
4. Does the message only appear when the user tries to navigate to the alcoholic products category?
5. How should the age be verified (e.g., simple input, date picker)?

**Detailed Requirement:**
When a user navigates to the alcoholic products category, a pop-up should appear asking for age verification by inputting the user's date of birth using a date picker. The system should verify that the user is 18 years or older and, if under 18, display an error message and deny access to the alcoholic products. The system must securely store the age verification data in compliance with privacy regulations. If age verification fails, users should be redirected to the main shopping area with a clear message explaining the restriction.

### **3. Shipping Cost Changes**

**Vague Requirement:** 
- Free shipping for orders above a certain amount. Orders below this amount will incur a shipping fee.

**Questions:**
1. Is the shipping cost calculated after each item is added and removed, or is it calculated after the order is closed?
2. Is the free shipping policy clearly communicated to the user?
3. Is the amount needed to reach free shipping shown to the user?
4. Is the system prepared for sudden price changes from delivery partners?

**Detailed Requirement:**
The system should dynamically calculate the shipping cost after each item is added or removed from the basket. The free shipping policy and the threshold amount should be clearly communicated to the user on cart page and during checkout. As users add items to their basket, the amount needed to reach free shipping should be displayed prominently. The system must be capable of handling sudden price changes from delivery partners, ensuring that shipping costs are updated in real-time.
