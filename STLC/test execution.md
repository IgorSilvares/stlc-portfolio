| Test ID | Test Case Description | Test Data | Expected Result | Actual Result | Status |
|---------|------------------------|-----------|-----------------|---------------|--------|
| TC001   | Verify submitting a 5-star rating | 5-star rating | Rating should be submitted successfully | PASS | DONE |
| TC002   | Verify submitting a 6-star rating | 6-star rating | Error message should be displayed | PASS | DONE |
| TC003   | Verify submitting written feedback with 100 characters | 100 characters feedback | Feedback should be submitted successfully | FAIL | DONE |
| TC004   | Verify submitting written feedback with 501 characters | 501 characters feedback | Error message should be displayed | PASS | DONE |
| TC005   | Verify submitting a 3-star rating | 3-star rating | Rating should be submitted successfully | PASS | DONE |
| TC006   | Verify updating rating and feedback | Updated rating and feedback | Rating and feedback should be updated successfully | PASS | DONE |
| TC007   | Verify access with valid age | Valid age (e.g., 18+) | User should gain access | PASS | DONE |
| TC008   | Verify access with invalid age | Invalid age (e.g., under 18) | Error message should be displayed | PASS | DONE |
| TC009   | Verify system behavior when no age is entered | Blank age field | Error message should be displayed | PASS | DONE |
| TC010   | Verify free shipping for high-value orders | Cart value above free shipping threshold | Free shipping should be applied | PASS | DONE |
| TC011   | Verify shipping fee for low-value orders | Cart value below free shipping threshold | Shipping fee should be applied | PASS | DONE |
| TC012   | Verify system behavior when removing items to drop below free shipping threshold | Updated cart value below threshold | Shipping fee should be applied | FAIL | DONE |
