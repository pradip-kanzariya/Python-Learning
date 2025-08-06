# 5. Testing and Debugging

# Practice Task : 2 | Debug a buggy program and log the outputs to identify errors.
import logging

def calculate_average(scores):
    total = 0
    count = 0
    for score in scores:
        if isinstance(score, (int,float)):
            count += 1
            total += score
        else:
            logging.warning(f"Invalid Item : {score} in Scores: {scores}")
    try:
        result = total / count
        return result
    except Exception as e:
        logging.error(e)

def process_scores(student_scores):
    for student, scores in student_scores.items():
        logging.debug(f"Processing scores for {student} : {scores}")
        if scores:
            avg = calculate_average(scores)
            logging.info(f"Student: {student} Average: {avg:.2f}")
        else:
            logging.error(f"Student {student} score is Empty.")


# Practice Task : 2.1 | Debug a buggy program and log the outputs to identify errors.
import logging

def calculate_total(cart):
    total = 0
    for item in cart:   
        logging.debug(f"Processing: {item['name']}, Items: {item['quantity']}, Price: {item['price']}")
        if item['price'] == "free":
            logging.warning(f"Invalid price for {item['name']} so counting it 0.")
            item['price'] = 0
        total += item['price'] * item['quantity']
    return total

def apply_discount(total, discount_code):
    if discount_code == "SAVE10":
        discount = total * 0.1
        logging.info(f"Discount applied ({discount_code}): -{discount}")
        total = total - discount
    elif discount_code == "SAVE20":
        discount = total * 0.2
        logging.info(f"Discount applied ({discount_code}): -{discount}")
        total = total - discount
    elif discount_code == "SAVE50":
        discount = total * 0.5
        logging.info(f"Discount applied ({discount_code}): -{discount}")
        total = total - discount
    else:
        logging.warning("No valid discount applied.")
    logging.info(f"Final total: {total}")
    return total

def checkout(cart, discount_code):
    total = calculate_total(cart)
    total = apply_discount(total, discount_code)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    student_scores = {
        "Alice": [85, 90, 78],
        "Bob": [70, 80, "error"],
        "Charlie": []
    }
    process_scores(student_scores)

    shopping_cart = [
        {"name": "Book", "price": 250, "quantity": 2},
        {"name": "Pen", "price": 20, "quantity": 5},
        {"name": "Notebook", "price": "free", "quantity": 1}
    ]
    checkout(shopping_cart, "SAVE50")
