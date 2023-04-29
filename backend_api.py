import openai

# open the key.txt file and add its contents to the api_key variable
with open('key.txt', 'r') as file:
    api_key = file.read().replace('\n', '')

openai.api_key = api_key


def generate_response(prompt):
    # Call the OpenAI API to generate a response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system",
                   "content": "I am a twitter post writer for the ifo Institute. They post short, professional posts with hashtags and links in German "},
                  {'role': 'user', 'content': prompt}],
        max_tokens=512,
        n=1,
        temperature=1,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
    )
    # Get the response text from the API response
    response_text = response['choices'][0]['message']['content']

    return response_text


def twitter_text(pr_text):
    prompt = "generate a very short german twitter post text out of this press release for the ifo institute: " + pr_text
    output_text = generate_response(prompt)
    return output_text

def keyword(pr_text):
    prompt = "generate one simple keyword in english, related to economy and understandable for a child, for a fitting background image for a twitter post to this press release:" + pr_text
    output_text = generate_response(prompt)
    return output_text


#temp = keyword(
 #   "Pressemitteilung - 28. April 2023 Konsum und Industrie senden gegensätzliche Impulse für deutsche Konjunktur „Die deutsche Konjunktur ist zu Jahresbeginn gespalten.“ Mit dieser Einschätzung hat ifo Konjunkturchef Timo Wollmershäuser auf die Meldung des Statistischen Bundesamtes reagiert, dass die Wirtschaftsleistung im ersten Quartal 2023 stagniert hat. „Auf der einen Seite profitiert die Industrie von nachlassenden Lieferengpässen sowie von gesunkenen Energiepreisen und ist auf einen Wachstumskurs eingeschwenkt. Auf der anderen Seite zehrt die hohe Inflation an der Kaufkraft der privaten Haushalte und lässt den Konsum schrumpfen“, fügt Wollmershäuser an. In der Industrie dürfte der Aufwärtstrend auch im weiteren Verlauf des Jahres anhalten. Das Geschäftsklima hat sich bereits sechs Mal in Folge verbessert und ist mittlerweile positiv. Die Auftragsbücher sind prall gefüllt, und die allmähliche Belebung der Weltkonjunktur wird die Neuaufträge weiter zunehmen lassen. Damit stehen die Zeichen für eine Ausweitung der Exporte und der Ausrüstungsinvestitionen gut. Die Konsumkonjunktur wird sich nur langsam berappeln. Zwar beschleunigt sich der Anstieg der Einkommen der privaten Haushalte, weil Tariflöhne angehoben und Inflationsprämien ausgezahlt werden. Aber die Inflation dürfte in den kommenden Monaten hartnäckig hoch bleiben. Ein Reallohnplus dürfte es daher erst in der zweiten Jahreshälfte geben. Die Stimmung der konsumnahen Dienstleister und Einzelhändler hat sich zwar bis zuletzt verbessert, ist aber mehrheitlich noch negativ. Die Bauwirtschaft erlebte zu Jahresbeginn durch die milde Witterung eine vorübergehende Sonderkonjunktur, nachdem der Dezember noch ausgesprochen kalt war. An dem Abwärtstrend, der vor allem durch den Wohnungsbau getrieben wird, dürfte sich im weiteren Verlauf des Jahres nichts ändern. Hohe Finanzierungs- und Baukosten haben die Neuaufträge einbrechen und die Stornierungen bestehender Aufträge zunehmen lassen. Das Geschäftsklima unter den Bauunternehmern ist so schlecht wie zuletzt nach der Weltfinanzkrise im Jahr 2010.")
#print(temp)

