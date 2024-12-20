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



