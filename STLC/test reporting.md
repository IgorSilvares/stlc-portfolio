### Scenario 1: Verify submitting a 5-star rating

Input: 5 stars.

Expected Outcome: Rating is saved and displayed correctly.

| Action                                                      | Expected outcome                            | OK/NOK | URL                                                                                | Link to issue |
|-------------------------------------------------------------|---------------------------------------------|--------|------------------------------------------------------------------------------------|---------------|
| Go to login page Grocery Mate                               | Login page appears                          | OK     | [https://grocerymate.masterschool.com/auth](https://grocerymate.masterschool.com/auth) |               |
| Log in with email: user@user.com and password: user123      | You are logged and redirected to home page  | OK     |                                                                                    |               |
| Go to shop page                                             | Shop page appears                           | OK     | [https://grocerymate.masterschool.com/store](https://grocerymate.masterschool.com/store) |               |
| Click on Oranges                                            | Oranges page appears                        | OK     | [https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb4798f](https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb4798f) |               |
| Click on 5 stars                                            | 5 stars selected                            | OK     |                                                                                    |               |
| Click on Send                                               | Review sent                                 | OK     |                                                                                    |               |
| Check if rating appears on Orange page                      | 5 stars rating with no comments add         | OK     |                                                                                    |               |


![image](https://github.com/user-attachments/assets/e531b3fd-b835-400d-8f13-5ccde4982cdc)
![image](https://github.com/user-attachments/assets/63d88e69-582b-4cb1-8742-7f7b3026a915)


### Scenario 2: Verify submitting a 6-star rating

Input: 6 stars.

Expected Outcome: It's not possible to select 6 stars on rating.


| Action                                                      | Expected outcome                            | OK/NOK | URL                                                                                | Link to issue |
|-------------------------------------------------------------|---------------------------------------------|--------|------------------------------------------------------------------------------------|---------------|
| Go to login page Grocery Mate                               | Login page appears                          | OK     | [https://grocerymate.masterschool.com/auth](https://grocerymate.masterschool.com/auth) |               |
| Log in with email: user@user.com and password: user123      | You are logged and redirected to home page  | OK     |                                                                                    |               |
| Go to shop page                                             | Shop page appears                           | OK     | [https://grocerymate.masterschool.com/store](https://grocerymate.masterschool.com/store) |               |
| Click on Oranges                                            | Oranges page appears                        | OK     | [https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb4798f](https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb4798f) |               |
| Click on 6 stars                                            | 6 stars cannot be selected                            | OK     |                                                   

![image](https://github.com/user-attachments/assets/e531b3fd-b835-400d-8f13-5ccde4982cdc)


### Scenario 3: Verify submitting written feedback with 100 characters

Enter feedback with 100 characters.

Expected Outcome: Feedback is saved and displayed correctly.


| Action                                                      | Expected outcome                            | OK/NOK | URL                                                                                | Link to issue |
|-------------------------------------------------------------|---------------------------------------------|--------|------------------------------------------------------------------------------------|---------------|
| Go to login page Grocery Mate                               | Login page appears                          | OK     | [https://grocerymate.masterschool.com/auth](https://grocerymate.masterschool.com/auth) |               |
| Log in with email: user@user.com and password: user123      | You are logged and redirected to home page  | OK     |                                                                                    |               |
| Go to shop page                                             | Shop page appears                           | OK     | [https://grocerymate.masterschool.com/store](https://grocerymate.masterschool.com/store) |               |
| Click on Oranges                                            | Oranges page appears                        | OK     | [https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb4798f](https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb4798f) |               |
| Enter feedback with 100 characters                                            |                             |      |                                                   
| Click on 3 stars                                            | 3 stars selected                            | OK     |                                                   
| Click on Send                                            | Review sent                            | OK     |                                                   
| Check if rating with the feedback appears on Orange page                                            | Review with 3 stars and 100 characters feedback                            | NOK     |                                        | https://github.com/IgorSilvares/stlc-portfolio/issues/1#issue-2752294148
![image](https://github.com/user-attachments/assets/b3c9d9f1-95f7-4fdd-9dd7-439d041f5709)

![image](https://github.com/user-attachments/assets/0abaeb73-9d17-4f9e-ba18-4d7c403f9045)

