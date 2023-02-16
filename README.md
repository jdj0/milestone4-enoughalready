<h1 align="center">Enough Already</h1>

![Mock ups](confessify/static/images/rm-imgs/mock-up.png)

Enough Already is a full stack ecommerce web application that follows real world business logic, aiming to fulfil the needs of users and customers with various aims.

View live site [here](https://enough-already.herokuapp.com/).

# Features 
- Interactive web application that is responsive on all display sizes
- Authentication system, provided through django allauth
- A full ecommerce application that displays products, allows the user to add them to a shopping bag before checking out and purchasing the items
- Payments through STRIPE integration
- SQL Database (PostgreSQL)
- Demonstrates full CRUD functionality
    - Create orders
    - Read product details
    - Update delivery details in user account
    - Delete products from shopping bag


# UX

## User Stories
- First Time Visitor
    - I want to understand what the business is and their core values.
    - I want to see the products that the business offers.
    - I may want to create an account with the business if I am interested in the brand.

- Returning Visitor
    - I want to be able to view individual product details to inform a purchase decision.
    - I want to be able to purchase items by adding them to a shopping bag, then processing through a checkout.

- Frequent User
    - I want to create an account to enhance my shopping experience.
    - In my account I want to be able to view my order history.
    - I want to be able to store my delivery information to make the checkout process faster and easier. 

## Frontend Design
- Design Choices
    - The web app follows the principles of minimalist design — simple, uncluttered, beautiful. This is done in the hope of making the navigation of the app clear and obvious, whilst keeping the ‘spotlight’ on what matters — the products and the aims of the business. 

- Colour Scheme
    - There are 4 main colours that make up the theme of the site: #efddd4, #2d0e19, #9a115f, #d3adc5

![Colours](static/media/colour-scheme.png)

- Typography
    - There are two fonts used for font styling. ‘Palanquin’ is used for all headings and ‘Roboto’ is used for paragraphs, with both having a backup font of ‘sans-serif’. Both fonts are provided by Google fonts.

![Fonts](static/media/fonts.png)

- Wireframes<br>
The following wireframes were used to guide the frontend development of the e-commerce site. Below are the wireframes for the desktop and mobile layout. 

## Desktop
    - Home
![wireframe](static/media/home.png)
    - Products
![wireframe](static/media/products.png)
    - Product
![wireframe](static/media/product.png)
    - Shopping Bag
![wireframe](static/media/bag.png)
    - Checkout
![wireframe](static/media/checkout.png)
    - Account
![wireframe](static/media/account.png)


## Mobile
- Home<br>
<img src="static/media/mobile-home.png" width="900px">
- Products<br>
<img src="static/media/mobile-products.png" width="300px">
- Product<br>
<img src="static/media/mobile-product.png" width="300px">
- Shopping Bag<br>
<img src="static/media/mobile-bag.png" width="300px">
- Checkout<br>
<img src="static/media/mobile-checkout.png" width="300px">
- Account<br>
<img src="static/media/mobile-account.png" width="300px">

# Backend Design
## Products app models:
The item model, found in the products app, is used to store the details for each individual product sold in the store. This data is used throughout the app, displaying various product information when useful. The following fields make up the model.

- Item Model
    - title = a charfield that allows a title up to 99 characters.
    - description = a textfield to store the item’s description.
    - price = a decimal field to store the item price. Allows a maximum of six digits with two decimal places.
    - category = a charfield that draws on a predefined tuple (‘CATEGORY_CHOICES’).
    - size = a charfield that, again, draws on a predefined tuple that provides sizing option. 
    - quantity = an integerfield that simply stores the quantity of the product. As the store specialises in ‘one-off’ items, this is set with a default value of ‘1’.
    - image = an imagefield that stores a photo of the item.

## Checkout app models:
The ‘Order’ and ‘OrderLineItem’ model, found in the checkout app, allows the user to create an order from products created in the item model. An OrderLineItem is made up of data from the Item model, storing it's id, quantity and total. An Order is made up of OrderLineItems, totalling a grand total, and attaching shipping information and a user to the order.
- Order Model
    - user_account = a foreign key to the UserAccount model. This represents the user that placed the order.
    - order_number = This field generates a unique order number for the order and cannot be edited by the user.
    - full_name = a charfield that stores the name of the user ordering.
    - email = an emailfield that stores the email address of the user.
    - phone_number = a charfield for a contact number for the order.
    - country =  a countryfield that uses the CountryField package from django. Used to display a list of countries to simplify and make valid the address input. 
    - postcode = a charfield hat allows a postcode to be attached to an order.
    - town_or_city = a charfield to attach a town or city to the order.
    - street_address1 = a charfield to attach an address line to the order.
    - street_address2 = a charfield to attach an address line to the order.
    - county = a charfield to attach a county to the order.
    - date = a datetimefield that automatically generates when the order is placed.
    - delivery_cost =  a DecimalField that allows a delivery cost to be set. This is set with a default of zero as the business promotes free delivery on all orders.
    - order_total =  a DecimalField that stores the total of the items in the order.
    - grand_total =  a DecimalField that is generated from the order total and the delivery cost.
    - original_bag = a TextField that stores the items that were in the bag when the order was placed.
    - stripe_pid = stores the payment ID necessary for stripe integration. 
<br>
<br>
- Order Line Item Model
    - order = Foreign Key to the Order Model.
    - item = Foreign Key to the Item Model.
    - quantity = an integer that represents the quantity of the item in the order.
    - lineitem_total = a DecimalField that is not editable and is set by the save method of the model, which in turn, updates the - grand_total field in the order model.

## Accounts app models:
The UserAccount model, found in the accounts app, allows the user to create an account, where one can view their order history and update their default delivery address which will automatically appear when the logged in user progresses to the checkout page.

- UserAccount Model
    - user = a OneToOneField that connects to the built-in User model.
    - default_phone_number = a CharField that stores the account holder’s default phone number.
    - default_street_address1 = a CharField that stores the account holder’s default address number.
    - default_street_address2 = a CharField that stores the account holder’s default address number.
    - default_postcode = a CharField that stores the account holder’s default postcode.
    - default_town_or_city = a CharField that stores the account holder’s default town or city.
    - default_county = a CharField that stores the account holder’s default county.
    - default_country =  a CharField that stores the account holder’s default country, by selecting the country from the dropdown menu.

# Technologies

## Languages and Frameworks
- HTML5
- CSS3
- JavaScript ES6
- Python
- Django
- Postgresql (production) and SQLite (development)
- Django Templating
- Bootstrap 5

## Other Tools
- Google Fonts
- Font Awesome
- Git
- GitHub
- Unsplash
- Balsamiq
- Get CSS Scan

# Testing
## Project Tests
A test driven development process was used during this project, evidenced in the commit history. The following testing was performed manually when the site was deployed. Green was given to an area if the site performed as expected. Red if there was an unexpected outcome.
- Expectation: 
    - Functionality - Could products be viewed, added to bag, checked out? Could the user create an account?
    - Appearance - Did all elements display as intended?
    - Links - Do all links work and direct the user where they are supposed to? Do footer links open in a new tab?

<img src="static/media/manual-testing.png" width="900px">
<br>
<br>

## Code Tests
- CSS used in this application was passed through the Jigsaw CSS Validator and passed with no errors.

    <img style="border:0;width:88px;height:31px"
        src="http://jigsaw.w3.org/css-validator/images/vcss-blue"
        alt="Valid CSS!">
    </img>

- HTML was passed through the official W3C validator with no issues.<br>
<img src="static/media/html-val.png" width="400px">

     