# Test Plan for New Features of the Webshop: GroceryMate

## 1. Analyze the Product

### Objective
The primary objective of the product is to enhance the existing webshop by introducing new features while ensuring the smooth functioning of existing functionalities.

### User Base
The product will be used by existing and new users of the webshop, including individuals looking for a convenient online grocery shopping experience.

### Hardware and Software Specifications

- **Hardware Requirements:**
    - Devices: PCs, laptops, smartphones, tablets
    - Specifications: Standard configurations for Android and iOS devices, desktops with minimum 4GB RAM, 2GHz processor
- **Software Requirements:**
    - Operating Systems: Windows, macOS, Android, iOS
    - Browsers: Chrome, Firefox, Safari, Edge
    - Dependencies: Backend services, payment gateways, third-party rating and age verification services

### Product Functionality

The product allows users to:
- Register and log in
- Search for products, sort on price, and browse categories
- Add products to favorites
- Add products to the basket
- Complete the checkout process: billing, form submission, and payment method selection
- Calculate the total price

## 2. Design the Test Strategy

### Scope of Testing

- **In Scope:**
    - Register and login functionality
    - Product search, sorting, and categorization
    - Adding products to favorites and basket
    - Checkout process and cost calculation
    - New features: Product Rating System, Age Verification for Alcoholic Products, Shipping Cost Changes
- **Out of Scope:**
    - Backend database operations not affecting the user interface
    - Non-functional aspects of third-party integrations unless directly related to user experience

### Type of Testing

- Functional Testing
- Usability Testing

### Risks and Issues

- **Delays in development**
    - Mitigation: Implement a buffer period in the schedule.
- **Lack of test data**
    - Mitigation: Create mock data sets for testing purposes.
- **Resource unavailability**
    - Mitigation: Identify backup resources.

### Test Logistics

- **Igor Silvares** - Test Manager
- **John Doe** - QA Engineer (Functional Testing)
- **Alice Johnson** - QA Engineer (Usability Testing)
- **Robert Brown** - QA Engineer (Functional Testing)
- **Maria Garcia** - End User for UAT

## 3. Define Test Objectives

### Objectives

- **Functionality:** Ensure new features and existing functionalities work as intended.
- **GUI:** Verify the graphical user interface for usability and consistency.
- **Usability:** Assess the user-friendliness of the platform.

### Expected Outcomes

- **Functionality:** All features perform correctly according to specifications.
- **GUI:** The interface is intuitive, responsive, and free of defects.
- **Usability:** Users can navigate and use the platform easily.

## 4. Define Test Criteria

### Suspension Criteria

- Testing will be suspended if critical defects are found that block further testing.
- Lack of necessary resources or test environment failures.

### Exit Criteria

- All planned tests have been executed.
- Pass Rate: At least 90% of executed test cases have passed.
- All critical and high-priority defects have been resolved and closed.
- No severity 1 or severity 2 defects are open.
- User acceptance testing has been completed, and sign-off has been obtained.

## 5. Resource Planning

- **Human Resources:** QA team, development team, end users for UAT
- **Hardware:** PCs, laptops, smartphones, tablets
- **Software:** Browsers (Chrome, Firefox, Safari, Edge), operating systems (Windows, macOS, Android, iOS)
- **Infrastructure:** Test environments, automation tools

## 6. Plan Test Environment

- **Test Environments:** Real devices installed with real browsers and operating systems to simulate user conditions.
- **Environments:** Development (DEV), Testing (TEST), Acceptance (ACC), Production (PROD)

## 7. Schedule and Estimation

| Activity             | Start Date | End Date   | Environment | Responsible Person | Estimated Effort |
|----------------------|------------|------------|-------------|--------------------|------------------|
| Test Planning        | 01/08/2025 | 05/08/2025 | All         | Test Manager       | 10 hours         |
| Test Case Design     | 06/08/2025 | 15/08/2025 | All         | QA Team            | 20 hours         |
| Unit Testing         | 16/08/2025 | 25/08/2025 | DEV         | Development Team   | 30 hours         |
| Integration Testing  | 26/08/2025 | 30/08/2025 | TEST        | QA Team            | 20 hours         |
| System Testing       | 01/09/2025 | 10/09/2025 | TEST        | QA Team            | 40 hours         |
| Usability Testing    | 11/09/2025 | 15/09/2025 | TEST        | QA Team            | 20 hours         |
| UAT                  | 22/09/2025 | 30/09/2025 | ACC         | End Users          | 30 hours         |
| Production Release   | 01/10/2025 | 01/10/2025 | PROD        | DevOps Team        | 10 hours         |

## 8. Determine Test Deliverables

Documents/tools that must be created to support testing activities in the project:

- **Test Plan Document**
- **Test Cases and Test Scripts**
- **Test Data**
- **Test Reports**
- **Defect Reports**
- **UAT Sign-off Document**
