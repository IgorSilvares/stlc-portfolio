## **The software**

Webshop, with the following basic functionalities:

- Register and login functionality
- Searching for products, sorting on price, categories of products
- Add products to favorites
- Add products to basket
- Check-out process: billing and sending information in a form, choose payment method. Calculation of costs (calculate total price)

## New features

### **1. Product Rating System**

**Vague Requirement:** 
- Users should be able to rate products with a 5-star system and have the option to add written feedback.

**Questions**:
  - Can users edit or delete their ratings and feedbacks after submission?
  - What happens if a user tries to submit feedback without providing a rating?
  - How is written feedback field validated (character limit, forbidden words...)?
  - Where will the user find the product rating functionality?
  - Who can submit a rating?
    
    
### **2. Age Verification for Alcoholic Products**

**Vague Requirement:** 
- Alcoholic products require age verification. A modal should appear when navigating to the alcoholic products category asking if the user is 18+. Users must input their age before accessing the alcoholic products.

**Questions**:
  - What is the user experience for those who fail the age verification?
  - Where will the message asking for the user's age be displayed?
  - How the system will store the data from the user's age?
  - Does the message only appear when the user tries to navigate to the alcoholic products category?
  - How should de age be verified(e.g., simple input, date picker...)
    
### **3. Shipping Cost Changes**

**Vague Requirement:** 
- Free shipping for orders above a certain amount. Orders below this amount will incur a shipping fee.

**Questions**:
  - Is the shipping cost calculated after each item is added and removed, or is it calculated after the order is closed?
  - Is the free shipping policy clearly communicated to the user?
  - Is the amount needed to reach free shipping shown to the user?
  - Is the system prepared for sudden price changes from delivery partners?
