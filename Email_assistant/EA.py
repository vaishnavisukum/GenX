import pandas as pd
import pickle
import imaplib
import email
import smtplib
import re
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# =====================
# CONFIG
# =====================

EMAIL = "your_email@gmail.com"
PASSWORD = "your_app_password"
DEFAULT_NAME = "Vaishnavi"


# =====================
# TRAIN MODEL
# =====================

def train_model():
    df = pd.read_csv("data.csv")

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(df["text"])

    model = LogisticRegression(max_iter=200)
    model.fit(X, df["label"])

    pickle.dump(model, open("model.pkl", "wb"))
    pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

    print("Model trained successfully")


# =====================
# LOAD MODEL
# =====================

def load_model():
    model = pickle.load(open("model.pkl", "rb"))
    vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
    return model, vectorizer


def classify_email(text, model, vectorizer):
    X = vectorizer.transform([text])
    return model.predict(X)[0]


# =====================
# FETCH EMAILS
# =====================

def fetch_emails(username, password, start_time):
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(username, password)
    mail.select("inbox")

    status, messages = mail.search(None, "ALL")
    email_ids = messages[0].split()

    emails = []

    for e_id in email_ids:
        status, msg_data = mail.fetch(e_id, "(RFC822)")
        msg = email.message_from_bytes(msg_data[0][1])

        try:
            email_time = parsedate_to_datetime(msg["Date"])
            if email_time.tzinfo is None:
                email_time = email_time.replace(tzinfo=timezone.utc)
        except:
            continue

        if email_time <= start_time:
            continue

        subject = msg.get("subject", "No Subject")
        sender = msg.get("from", "Unknown Sender")
        body = ""

        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True).decode(errors="ignore")
                    break
        else:
            body = msg.get_payload(decode=True).decode(errors="ignore")

        emails.append({
            "sender": sender,
            "subject": subject,
            "body": body
        })

    mail.logout()
    return emails


# =====================
# SUMMARY
# =====================

def summarize(text):
    return text[:120]


# =====================
# REPLY GENERATOR
# =====================

def get_user_name(default_name):
    choice = input(f"Use default name '{default_name}'? (y/n): ")
    if choice.lower() == "y":
        return default_name
    return input("Enter your name: ")


def generate_reply(choice, summary, category, default_name):
    user_name = get_user_name(default_name)

    if choice == "1":
        return (
            "Dear Hiring Team,\n\n"
            "Thank you for sharing this opportunity. I am interested in learning more about the role.\n\n"
            "Please share more details regarding the next steps.\n\n"
            f"Best regards,\n{user_name}"
        )

    elif choice == "2":
        return (
            "Hello,\n\n"
            "Thank you for your message. Could you please provide more details regarding the requirements and timeline?\n\n"
            "This will help me respond better.\n\n"
            f"Best regards,\n{user_name}"
        )

    elif choice == "4":
        custom = input("Enter what you want to say: ")
        return (
            f"Hello,\n\n"
            f"Regarding your email: {summary}\n\n"
            f"{custom}\n\n"
            f"Best regards,\n{user_name}"
        )

    return None


# =====================
# SEND EMAIL
# =====================

def extract_email(sender):
    match = re.search(r"<(.+?)>", sender)
    if match:
        return match.group(1)
    return sender


def send_email(username, password, to, subject, body):
    to_email = extract_email(to)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(username, password)

    message = f"Subject: {subject}\n\n{body}"
    server.sendmail(username, to_email, message)
    server.quit()

    print("Email sent successfully")


# =====================
# MAIN FUNCTION
# =====================

def main():
    print("1. Train Model")
    print("2. Run Email Assistant")

    option = input("Enter choice: ")

    if option == "1":
        train_model()
        return

    model, vectorizer = load_model()
    start_time = datetime.now(timezone.utc)

    emails = fetch_emails(EMAIL, PASSWORD, start_time)

    for e in emails:
        full_text = e["subject"] + " " + e["body"]
        category = classify_email(full_text, model, vectorizer)
        summary = summarize(full_text)

        print("\n-------------------")
        print("From:", e["sender"])
        print("Category:", category)
        print("Summary:", summary)

        print("\n1. Interested")
        print("2. Ask Info")
        print("3. Skip")
        print("4. Custom Reply")

        choice = input("Enter choice: ")

        if choice == "3":
            continue

        reply = generate_reply(choice, summary, category, DEFAULT_NAME)

        if reply:
            print("\nGenerated Reply:\n")
            print(reply)

            send_choice = input("Send email? (y/n): ")
            if send_choice.lower() == "y":
                send_email(
                    EMAIL,
                    PASSWORD,
                    e["sender"],
                    "Re: " + e["subject"],
                    reply
                )


if __name__ == "__main__":
    main()
