import logging
import sentry_sdk
from sentry_sdk import configure_scope
    

sentry_sdk.init(
    "https://cdbd416fe76449d7aeabe35121dd82ea@o1036395.ingest.sentry.io/6025122",
    sample_rate=1.0, 
    traces_sample_rate=1.0, # What is the difference between the two? Does traces_sample_rate include sample_rate?
    send_default_pii=False,
)


def main():

    with sentry_sdk.start_span(op="bucket", transaction="full of sand") as span:
        span.set_tag('personal_info', "{'password': '12838dhdj3', 'secret': 18273732, \
        'credentials': {'name': 'Alex', 'ID': 'xajsk'}, 'private': 'tell me more', \
            'email' : 'abc@email.com'}")

    with configure_scope() as scope:
        scope.user = {"id": 41, "email": "sandcastle@hotmail.com"}

    logging.error("Hello Sentry from sentrybox.")
    logging.error("190.190.190.2")
    logging.error("Password: ahdh3j2(27%")
    #sentry_sdk.capture_message("{'password': '12838dhdj3', 'secret': 18273732, \
    #     'credentials': {'name': 'Alex', 'ID': 'xajsk'}, 'private': 'tell me more', \
    #         'email' : 'abc@email.com'}")
    
    with configure_scope() as scope:
        scope.transaction = "shovel"
        scope.user = {"id": 42, "email": "john.doe@example.com", "ip_address": "190.109.29.2"}
        scope.set_tag("my-tag", "my value")


    try:
        1/0
    except ZeroDivisionError as z:
        raise z
    

if __name__ == "__main__":
    main()