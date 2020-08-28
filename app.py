from utils.open_currency_site import OpenCurrencySite
from utils.history import open_history, show_history

PROMPT = "Enter any key to continue or 'q' to quit: "

APP_ID = "7574eaca503b40b99671d8f49a19a703"

exchange_rates = OpenCurrencySite(APP_ID)

prompt = ''

open_history()

while prompt.lower().strip() != 'q':
    try:
        from_currency = input('From which currency?(Please provide with correct currency abbreviation): ').upper().strip()
        from_amount = float(input('How much?: '))
        to_currency = input('To which currency?(Please provide with correct currency abbreviation): ').upper().strip()
        if from_amount > 0:
            result = exchange_rates.convert(from_amount, from_currency, to_currency)
            print(result)
            prompt = input(PROMPT)
        else:
            print('Sorry, negative value cannot be converted. Please try again.')
    except ValueError:
        print('Invalid entry. Please try again.')
        prompt = input(PROMPT)
    except KeyError:
        print('Invalid entry. Please try again.')
        prompt = input(PROMPT)

prompt_history = input('Do you want to see what you searched?(y/n): ').lower().strip()

if prompt_history != 'n':
    show_history()

print("\nThank you for using the app. Have a nice day!")

