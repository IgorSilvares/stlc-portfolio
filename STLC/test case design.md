# Test Case Design

## Feature 1: Product Rating System

**Test Design Techniques**: Boundary Value Analysis (BVA), Equivalence Partitioning (EP), Error Guessing

### Test Cases:

### Boundary Value Analysis:

**Test Case**: Verify submitting a 5-star rating.
- **Input**: 5 stars.
- **Expected Outcome**: Rating is saved and displayed correctly.

**Test Case**: Verify submitting a 6-star rating.
- **Input**: 6 stars.
- **Expected Outcome**: Rating is not saved and an appropriate message is displayed.

**Test Case**: Verify submitting a -1-star rating.
- **Input**: -1 stars.
- **Expected Outcome**: Rating is not saved and an appropriate message is displayed.

**Test Case**: Verify submitting written feedback with 100 characters.
- **Input**: Enter feedback with 100 characters.
- **Expected Outcome**: Feedback is saved and displayed correctly.

**Test Case**: Verify submitting written feedback with 101 characters.
- **Input**: Enter feedback with 101 characters.
- **Expected Outcome**: Feedback is not saved and an appropriate message is displayed.

**Test Case**: Verify submitting written feedback with 0 characters.
- **Input**: Enter feedback with 0 characters.
- **Expected Outcome**: The rating will be saved without a feedback.

### Equivalence Partitioning:

**Test Case**: Verify submitting a 3-star rating.
- **Input**: 3 stars.
- **Expected Outcome**: Rating is saved and displayed correctly.

### Error Guessing:

**Test Case**: Verify updating rating and feedback.
- **Input**: Update the star rating and feedback.
- **Expected Outcome**: Updated rating and feedback are saved and displayed correctly.

## Feature 2: Age Verification for Alcoholic Products

**Test Design Techniques**: Decision Table Testing, Equivalence Partitioning (EP), Error Guessing

### Test Cases:

### Decision Table Testing:

**Test Case**: Verify age verification modal appears.
- **Input**: Navigate to the alcoholic products category.
- **Expected Outcome**: The modal appears asking for age verification.

### Equivalence Partitioning:

**Test Case**: Verify access with valid age.
- **Input**: Enter age 25.
- **Expected Outcome**: Access to alcoholic products is granted.

**Test Case**: Verify access denial with invalid age.
- **Input**: Enter age 16.
- **Expected Outcome**: Access is denied, and an appropriate message is displayed.

### Error Guessing:

**Test Case**: Verify system behavior when no age is entered.
- **Input**: Leave age input field empty.
- **Expected Outcome**: Access is denied, and an appropriate message is displayed.

## Feature 3: Shipping Cost Changes

**Test Design Techniques**: Boundary Value Analysis (BVA), Error Guessing, Use Case Testing

### Test Cases:

### Boundary Value Analysis:

**Test Case**: Verify free shipping for high-value orders.
- **Input**: Add products to exceed the free shipping threshold.
- **Expected Outcome**: No shipping cost is applied.

**Test Case**: Verify shipping fee for low-value orders.
- **Input**: Add products below the free shipping threshold.
- **Expected Outcome**: Correct shipping fee is applied.

### Error Guessing:

**Test Case**: Verify system behavior when removing items to drop below the free shipping threshold.
- **Input**: Add products above the free shipping threshold, then remove items to drop below the threshold.
- **Expected Outcome**: Shipping cost is applied correctly based on the new order total.

### Use Case Testing:

**Test Case**: Verify that the free shipping policy is visible in the cart.
- **Input**: A registered user navigate to the cart page.
- **Expected Outcome**: The registed user should be able to see the free-shipping policy on the cart page.
