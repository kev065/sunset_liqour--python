import click
from decimal import Decimal
from Main import session, Customer, Company, Brand,Rating,Comment
from view_brands import view_all_drinks
from view_all_comments import view_all_comments
from view_all_ratings import view_all_ratings
from view_all_companies import view_all_companies


@click.command()
def customer_input():
    name = click.prompt(click.style("Name", fg='blue'), type=str)
    age = click.prompt(click.style("Age", fg='blue'), type=int)
    email = click.prompt(click.style("Email", fg='blue'), type=str)
    address = click.prompt(click.style("Address", fg='blue'), type=str)
    loyalty_points = click.prompt(click.style("Loyalty Points", fg='blue'), type=int)
    discount_percentage = min(5 + (loyalty_points // 100) * 5, 20)
    discount_message = click.style(f"You will get a {discount_percentage}% discount on your next purchase!", fg='green')

    if age >= 18:
        click.echo(click.style(f"Hello {name}, thank you for choosing us. Your satisfaction is our priority.", fg='green'))
        click.echo(discount_message)

        new_customer = Customer(name=name, age=age, email=email, address=address, loyalty_points=loyalty_points)
        session.add(new_customer)
        session.commit()
        click.echo("Customer details added to the database.")
    else:
        click.echo(click.style("Sorry, we cannot process your order.", fg='red'))
        click.echo(click.style("Alcohol is for persons above the age of 18.", fg='red'))

    main_menu()    



@click.command()
def brand_input():
    brand_name = click.prompt(click.style("Brand Name", fg='blue'), type=str)
    company_id = click.prompt(click.style("Company ID", fg='blue'), type=int)
    category = click.prompt(click.style("Category", fg='blue'), type=str)
    price = click.prompt(click.style("Price", fg='blue'), type=float)
    customer_id = click.prompt(click.style("Customer ID", fg='blue'), type=int)

    new_brand = Brand(name=brand_name, company_id=company_id, category=category, price=price, customer_id=customer_id)
    
    session.add(new_brand)
    session.commit()

    click.echo(click.style(f"Brand '{brand_name}' has been added to the database.", fg='green'))

    main_menu()




@click.command()
def company_input():
    company_name = click.prompt(click.style("Company Name", fg='blue'), type=str)
    location = click.prompt(click.style("Location", fg='blue'), type=str)
    established_year = click.prompt(click.style("Established Year", fg='blue'), type=int)
    revenue = click.prompt(click.style("Revenue", fg='blue'), type=float)

   
    new_company = Company(name=company_name, location=location, established_year=established_year, revenue=revenue)
    session.add(new_company)
    session.commit()

    click.echo(click.style(f"Company '{company_name}' has been added to the database.", fg='green'))

    main_menu()

@click.command()
def add_comment():
    brand_id = click.prompt(click.style("Brand ID", fg='blue'), type=int)
    customer_id = click.prompt(click.style("Customer ID", fg='blue'), type=int)
    comment_text = click.prompt(click.style("Comment", fg='blue'), type=str)
    new_comment = Comment(brand_id=brand_id, customer_id=customer_id, text=comment_text)
    session.add(new_comment)
    session.commit()
    click.echo(click.style(f"Your comment has been added.", fg='green'))

    main_menu()


@click.command()
def add_rating():
    brand_id = click.prompt(click.style("Brand ID", fg='blue'), type=int)
    customer_id = click.prompt(click.style("Customer ID", fg='blue'), type=int)
    rating_score = click.prompt(click.style("Rating (1-5)", fg='blue'), type=int)
    new_rating = Rating(brand_id=brand_id, customer_id=customer_id, score=rating_score)
    session.add(new_rating)
    session.commit()
    click.echo(click.style(f"Your rating has been added.", fg='green'))

    main_menu()

@click.command()
def view_drinks():
    brands = session.query(Brand).all()
    for brand in brands:
        click.echo(click.style(f"{brand.name} - ${brand.price}", fg='green'))

    main_menu()

@click.command()

def search_brands():
    search_term = click.prompt(click.style("Enter a search term", fg='blue'), type=str)
    matching_brands = session.query(Brand).filter(Brand.name.contains(search_term)).all()

def search_all():
    search_term = click.prompt(click.style("Enter a search term", fg='blue'), type=str)
    matching_customers = session.query(Customer).filter(Customer.name.contains(search_term)).all()

    for customer in matching_customers:
        click.echo(click.style(f"Customer Name: {customer.name}, Email: {customer.email}", fg='green'))
    matching_brands = session.query(Brand).filter(Brand.name.contains(search_term)).all()
    for brand in matching_brands:
        click.echo(click.style(f"Brand: {brand.name}, Price: {brand.price}, Category: {brand.category}", fg='green'))

    matching_companies = session.query(Company).filter(Company.name.contains(search_term)).all()
    for company in matching_companies:
        click.echo(click.style(f"Company Name: {company.name}, Location: {company.location}", fg='green'))
    for brand in matching_brands:
        price = Decimal(brand.price) 
        click.echo(click.style(f"Brand: {brand.name}, Price: {price}, Category: {brand.category}", fg='green'))

    main_menu()


@click.command()
def main_menu():
    while True:
        click.echo("Welcome to sunset liqour store:")
        click.echo("1. Add customer details")
        click.echo("2. Add brand details")
        click.echo("3. Add company details")
        click.echo("4. Add a comment")
        click.echo("5. Add a rating")
        click.echo("6. View all drinks")
        click.echo("7. View all comments")
        click.echo("8. View all ratings")
        click.echo("9. View all companies")
        click.echo("10. Search brands")
        click.echo("11. Search all") 
        click.echo("12. Exit")  

        choice = click.prompt("Your choice", type=int)

        if choice == 1:
            customer_input()
        elif choice == 2:
            brand_input()
        elif choice == 3:
            company_input()
        elif choice == 4:
            add_comment()
        elif choice == 5:
            add_rating()
        elif choice == 6:
            view_all_drinks()
        elif choice == 7:
            view_all_comments()
        elif choice == 8:
            view_all_ratings()
        elif choice == 9:
            view_all_companies()
        elif choice == 10:
            search_brands()
        elif choice == 11:
            search_all()  
        elif choice == 12:
            break  
        else:
            click.echo("Invalid choice. Please choose a number between 1 and 12.")

if __name__ == '__main__':
    main_menu()



   