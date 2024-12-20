### Scenario 1: Verify submitting a 5-star rating

**Input:** 5 stars.

**Expected Outcome:** Rating is saved and displayed correctly.

| Action                                                      | Expected outcome                            | OK/NOK | URL                                                                                | Link to issue |
|-------------------------------------------------------------|---------------------------------------------|--------|------------------------------------------------------------------------------------|---------------|
| Go to login page Grocery Mate                               | Login page appears                          | OK     | [https://grocerymate.masterschool.com/auth](https://grocerymate.masterschool.com/auth) |               |
| Log in with email: user@user.com and password: user123      | You are logged and redirected to home page  | OK     |                                                                                    |               |
| Go to shop page                                             | Shop page appears                           | OK     | [https://grocerymate.masterschool.com/store](https://grocerymate.masterschool.com/store) |               |
| Click on Oranges                                            | Oranges page appears                        | OK     | [https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb4798f](https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb4798f) |               |
| Click on 5 stars                                            | 5 stars selected                            | OK     |                                                                                    |               |
| Click on Send                                               | Review sent                                 | OK     |                                                                                    |               |
| Check if rating appears on Orange page                      | 5 stars rating with no comments added       | OK     |                                                                                    |               |

![image](https://github.com/user-attachments/assets/e531b3fd-b835-400d-8f13-5ccde4982cdc)
![image](https://github.com/user-attachments/assets/63d88e69-582b-4cb1-8742-7f7b3026a915)

---

### Scenario 2: Verify submitting a 6-star rating

**Input:** 6 stars.

**Expected Outcome:** It's not possible to select 6 stars on rating.

| Action                                                      | Expected outcome                            | OK/NOK | URL                                                                                | Link to issue |
|-------------------------------------------------------------|---------------------------------------------|--------|------------------------------------------------------------------------------------|---------------|
| Go to login page Grocery Mate                               | Login page appears                          | OK     | [https://grocerymate.masterschool.com/auth](https://grocerymate.masterschool.com/auth) |               |
| Log in with email: user@user.com and password: user123      | You are logged and redirected to home page  | OK     |                                                                                    |               |
| Go to shop page                                             | Shop page appears                           | OK     | [https://grocerymate.masterschool.com/store](https://grocerymate.masterschool.com/store) |               |
| Click on Oranges                                            | Oranges page appears                        | OK     | [https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb4798f](https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb4798f) |               |
| Click on 6 stars                                            | 6 stars cannot be selected                  | OK     |                                                                                    |               |

![image](https://github.com/user-attachments/assets/e531b3fd-b835-400d-8f13-5ccde4982cdc)

---

### Scenario 3: Verify submitting written feedback with 100 characters

**Input:** Feedback text with 100 characters, 3-star rating.

**Expected Outcome:** Feedback text and 3-star rating are saved and displayed correctly.

| Action                                                      | Expected outcome                            | OK/NOK | URL                                                                                | Link to issue |
|-------------------------------------------------------------|---------------------------------------------|--------|------------------------------------------------------------------------------------|---------------|
| Go to login page Grocery Mate                               | Login page appears                          | OK     | [https://grocerymate.masterschool.com/auth](https://grocerymate.masterschool.com/auth) |               |
| Log in with email: user@user.com and password: user123      | You are logged and redirected to home page  | OK     |                                                                                    |               |
| Go to shop page                                             | Shop page appears                           | OK     | [https://grocerymate.masterschool.com/store](https://grocerymate.masterschool.com/store) |               |
| Click on Oranges                                            | Oranges page appears                        | OK     | [https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb4798f](https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb4798f) |               |
| Enter feedback with 100 characters                         | Feedback entered                            | OK     |                                                                                    |               |
| Click on 3 stars                                            | 3 stars selected                            | OK     |                                                                                    |               |
| Click on Send                                               | Review sent                                 | OK     |                                                                                    |               |
| Check if rating with the feedback appears on Orange page    | Review with 3 stars and 100 characters feedback | NOK  |                                                                                    | [https://github.com/IgorSilvares/stlc-portfolio/issues/1#issue-2752294148](https://github.com/IgorSilvares/stlc-portfolio/issues/1#issue-2752294148) |

![image](https://github.com/user-attachments/assets/b3c9d9f1-95f7-4fdd-9dd7-439d041f5709)
![image](https://github.com/user-attachments/assets/0abaeb73-9d17-4f9e-ba18-4d7c403f9045)

---

### Scenario 4: Verify submitting written feedback with 501 characters

**Input:** Feedback text with 501 characters.

**Expected Outcome:** Feedback text with more than 500 characters is not accepted.

| Action                                                      | Expected outcome                            | OK/NOK | URL                                                                                | Link to issue |
|-------------------------------------------------------------|---------------------------------------------|--------|------------------------------------------------------------------------------------|---------------|
| Go to login page Grocery Mate                               | Login page appears                          | OK     | [https://grocerymate.masterschool.com/auth](https://grocerymate.masterschool.com/auth) |               |
| Log in with email: user@user.com and password: user123      | You are logged and redirected to home page  | OK     |                                                                                    |               |
| Go to shop page                                             | Shop page appears                           | OK     | [https://grocerymate.masterschool.com/store](https://grocerymate.masterschool.com/store) |               |
| Click on Oranges                                            | Oranges page appears                        | OK     | [https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb4798f](https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb4798f) |               |
| Enter feedback with 501 characters                         | It's not possible to enter more than 500 characters | OK  |                                                                                    |               |

![image](https://github.com/user-attachments/assets/cb3b3594-ef2f-4df3-954d-8497d9fe0fe8)

---

### Scenario 5: Verify submitting a 3-star rating

**Input:** 3-star rating.

**Expected Outcome:** Rating is saved and displayed correctly.

| Action                                                      | Expected outcome                            | OK/NOK | URL                                                                                | Link to issue |
|-------------------------------------------------------------|---------------------------------------------|--------|------------------------------------------------------------------------------------|---------------|
| Go to login page Grocery Mate                               | Login page appears                          | OK     | [https://grocerymate.masterschool.com/auth](https://grocerymate.masterschool.com/auth) |               |
| Log in with email: user@user.com and password: user123      | You are logged and redirected to home page  | OK     |                                                                                    |               |
| Go to shop page                                             | Shop page appears                           | OK     | [https://grocerymate.masterschool.com/store](https://grocerymate.masterschool.com/store) |               |
| Click on Oranges                                            | Oranges page appears                        | OK     | [https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb4798f](https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb4798f) |                             |               |
| Click on 3 stars                                            | 3 stars selected                            | OK     |                                                                                    |               |
| Click on Send                                               | Review sent                                 | OK     |                                                                                    |               |
| Check if rating with the feedback appears on Orange page    | Review with 3 stars saved | OK  |                                                                                   

![image](https://github.com/user-attachments/assets/0abaeb73-9d17-4f9e-ba18-4d7c403f9045)

---

### Scenario 6: Verify Updating Rating and Feedback

**Input:** Update the star rating and feedback text.

**Expected Outcome:** Rating and feedback text is saved and displayed correctly.

| Action                                                      | Expected Outcome                            | OK/NOK | URL                                                                                | Link to Issue |
|-------------------------------------------------------------|---------------------------------------------|--------|------------------------------------------------------------------------------------|---------------|
| Go to login page Grocery Mate                               | Login page appears                          | OK     | [https://grocerymate.masterschool.com/auth](https://grocerymate.masterschool.com/auth) |               |
| Log in with email: user@user.com and password: user123      | You are logged in and redirected to home page  | OK     |                                                                                    |               |
| Go to shop page                                             | Shop page appears                           | OK     | [https://grocerymate.masterschool.com/store](https://grocerymate.masterschool.com/store) |               |
| Click on Oranges                                            | Oranges page appears                        | OK     | [https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb4798f](https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb4798f) |               |
| Click edit on the user's old rating                         | Edit Review pop-up appears                  | OK     |                                                                                    |               |
| Enter a new star rating and a new feedback text             | Review with new 4-star rating and new feedback text saved | OK     |                                                                                    |               |

![image](https://github.com/user-attachments/assets/823b76b8-d39d-470b-8bab-7fdf010916d3)
![image](https://github.com/user-attachments/assets/6074eec5-8c50-4dda-a31c-48b261fb51ad)
![image](https://github.com/user-attachments/assets/4b22d962-a04d-4732-a131-b882763eae84)

---

### Scenario 7: Verify Updating Rating and Feedback

**Input:** Navigate to the shop page

**Expected Outcome:** The pop-up appears asking for age verification.

| Action                                                      | Expected Outcome                            | OK/NOK | URL                                                                                | Link to Issue |
|-------------------------------------------------------------|---------------------------------------------|--------|------------------------------------------------------------------------------------|---------------|
| Go to shop page                                             |                                             |        | [https://grocerymate.masterschool.com/store](https://grocerymate.masterschool.com/store) |               |
| Wait for the Confirmation Age pop-up                        | Age confirmation message should appear      | OK     |                                                                                    |               |

![image](https://github.com/user-attachments/assets/b7f248cc-6e41-419c-bb65-4719eaaeb923)

---


### Scenario 8: Verify access with valid age

**Input:** enter date 20-12-1999 (25 years)

**Expected Outcome:** Access to alcoholic products is granted.

| Action                                                      | Expected Outcome                            | OK/NOK | URL                                                                                | Link to Issue |
|-------------------------------------------------------------|---------------------------------------------|--------|------------------------------------------------------------------------------------|---------------|
| Go to shop page                                             |                                             |        | [https://grocerymate.masterschool.com/store](https://grocerymate.masterschool.com/store) |               |
| Wait for the Confirmation Age pop-up                        | Age confirmation message should appear      | OK     |                                                       |               | 
| Enter the date 20-12-1999 and Click on confirm  |          |        |        |              |
|Click on Alocohol category |     Access granted to the page     |  OK      |        |              |

![image](https://github.com/user-attachments/assets/496f6530-cb2f-4a28-9d2e-1611f21d4e0f)

![image](https://github.com/user-attachments/assets/69ca4c2f-3582-432a-9300-1d112f72ebf9)


---


### Scenario 9: Verify Access with Invalid Age

**Input:** Enter date 20-12-2008 (16 years)

**Expected Outcome:** Access to alcoholic products is not granted.

| Action                                                      | Expected Outcome                            | OK/NOK | URL                                                                                | Link to Issue |
|-------------------------------------------------------------|---------------------------------------------|--------|------------------------------------------------------------------------------------|---------------|
| Go to shop page                                             |                                             |        | [https://grocerymate.masterschool.com/store](https://grocerymate.masterschool.com/store) |               |
| Wait for the Confirmation Age pop-up                        | Age confirmation message should appear      | OK     |                                                                                    |               | 
| Enter the date 20-12-2008 and click on confirm              |                                             |        |                                                                                    |               |
| Click on Alcohol category                                   | Access not granted to the page              | OK     |                                                                                    |               |

![image](https://github.com/user-attachments/assets/343227b2-a26b-45dd-93a0-6e8b441acddf)
![image](https://github.com/user-attachments/assets/8879d9dc-2147-4e25-9691-e051cca8f010)

---

### Scenario 10: Verify System Behavior When No Age Is Entered

**Input:** Leave age input field empty.

**Expected Outcome:** Access to alcoholic products is not granted.

| Action                                                      | Expected Outcome                            | OK/NOK | URL                                                                                | Link to Issue |
|-------------------------------------------------------------|---------------------------------------------|--------|------------------------------------------------------------------------------------|---------------|
| Go to shop page                                             |                                             |        | [https://grocerymate.masterschool.com/store](https://grocerymate.masterschool.com/store) |               |
| Wait for the Confirmation Age pop-up                        | Age confirmation message should appear      | OK     |                                                                                    |               | 
| Leave the age field empty and click on confirm              |                                             |        |                                                                                    |               |
| Click on Alcohol category                                   | Access not granted to the page              | OK     |                                                                                    |               |

![image](https://github.com/user-attachments/assets/cfc8d11c-7f38-4de2-8096-8fe1f0b72d04)
![image](https://github.com/user-attachments/assets/8879d9dc-2147-4e25-9691-e051cca8f010)


---

### Scenario 11: Verify free shipping for high-value orders

**Input:** Add products to exceed the free shipping threshold.

**Expected Outcome:** No shipping cost is applied.

| Action                                                      | Expected Outcome                            | OK/NOK | URL                                                                                | Link to Issue |
|-------------------------------------------------------------|---------------------------------------------|--------|------------------------------------------------------------------------------------|---------------|
| Go to login page Grocery Mate                               | Login page appears                          | OK     | [https://grocerymate.masterschool.com/auth](https://grocerymate.masterschool.com/auth) |               |
| Log in with email: user@user.com and password: user123      | You are logged and redirected to home page  | OK     |                                                                                    |               |
| Go to shop page                                             |                                             |        | [https://grocerymate.masterschool.com/store](https://grocerymate.masterschool.com/store) |               |
| Enter 100 Celery and click Add to Cart                        | Item added to cart      | OK     |                                                                                    |               | 
| Click on the cart button              |                                             |        |       https://grocerymate.masterschool.com/checkout                                                                             |               |
| Verify the shipment cost                                  | Shipment cost must be 0$              | OK     |                                                                                    |               |

![image](https://github.com/user-attachments/assets/9534852a-8e06-4c35-a158-20adbc28e67d)

![image](https://github.com/user-attachments/assets/baa44f84-4c7b-4f20-9e92-8cd4bc329d82)


---

### Scenario 12: Verify shipping fee for low-value orders

**Input:** Add products below the free shipping threshold.

**Expected Outcome:** Correct shipping fee is applied.

| Action                                                      | Expected Outcome                            | OK/NOK | URL                                                                                | Link to Issue |
|-------------------------------------------------------------|---------------------------------------------|--------|------------------------------------------------------------------------------------|---------------|
| Go to login page Grocery Mate                               | Login page appears                          | OK     | [https://grocerymate.masterschool.com/auth](https://grocerymate.masterschool.com/auth) |               |
| Log in with email: user@user.com and password: user123      | You are logged and redirected to home page  | OK     |                                                                                    |               |
| Go to shop page                                             |                                             |        | [https://grocerymate.masterschool.com/store](https://grocerymate.masterschool.com/store) |               |
| Enter 10 Celery and click Add to Cart                        | Item added to cart      | OK     |                                                                                    |               | 
| Click on the cart button              |                                             |        |       https://grocerymate.masterschool.com/checkout                                                                             |               |
| Verify the shipment cost                                  | Shipment cost must be presented              | OK     |                                                                                    |               |

![image](https://github.com/user-attachments/assets/cb0bd09a-ff6d-4028-a8ac-c11d22fa51bc)

![image](https://github.com/user-attachments/assets/b8c5c872-d0ae-4a3a-9a2f-780a1c073290)


---

### Scenario 13: Verify system behavior when removing items to drop below the free shipping threshold

**Input:** Add products above the free shipping threshold, then remove items to drop below the threshold.

**Expected Outcome:** Shipping cost is applied correctly based on the new order total.

| Action                                                      | Expected Outcome                            | OK/NOK | URL                                                                                | Link to Issue |
|-------------------------------------------------------------|---------------------------------------------|--------|------------------------------------------------------------------------------------|---------------|
| Go to login page Grocery Mate                               | Login page appears                          | OK     | [https://grocerymate.masterschool.com/auth](https://grocerymate.masterschool.com/auth) |               |
| Log in with email: user@user.com and password: user123      | You are logged and redirected to home page  | OK     |                                                                                    |               |
| Go to shop page                                             |                                             |        | [https://grocerymate.masterschool.com/store](https://grocerymate.masterschool.com/store) |               |
| Enter 29 Celery and click Add to Cart                        | Item added to cart      | OK     |                                                                                    |               | 
| Click on the cart button              |                                             |        |       https://grocerymate.masterschool.com/checkout                                                                             |               |
| Verify the shipment cost                                  | Shipment cost must 0$             | OK     |                                                                                    |               |
| Click on the "-" button to remove one Celary                                  | Shipment cost must be presented              | NOK     |                                                                                    |      https://github.com/IgorSilvares/stlc-portfolio/issues/2#issue-2752549816         |


![image](https://github.com/user-attachments/assets/891d98fd-d973-4d98-9738-b74cea2e3542)

![image](https://github.com/user-attachments/assets/d441c461-d1cc-4f30-8d53-987e27e50baf)

![image](https://github.com/user-attachments/assets/b0e54d1c-5f4f-4627-b558-af7074fbe241)

