score = 0

# List of questions
questions = [
    {
        'question': '¿Sangra durante más de 7 días al mes?',
        'options': ['Sí', 'No'],
    },
    {
        'question': '¿Tiene 3 o más días de sangrado más abundante durante su menstruación?',
        'options': ['Sí', 'No'],
    },
    {
        'question': 'En general, ¿su regla le resulta especialmente molesta debido a su abundancia?',
        'options': ['Sí', 'No'],
    },
    {
        'question': '¿En algunos de los días de sangrado más abundante mancha la ropa por las noches; o la mancharía si no usase doble protección o se cambiase durante la noche?',
        'options': ['Sí', 'No'],
    },
    {
        'question': 'Durante los días de sangrado más abundante le preocupa manchar el asiento de su silla, sofá, etc?',
        'options': ['Sí', 'No'],
    },
    {
        'question': '¿En general, en los días de sangrado más abundante, evita (en la medida de los posible) algunas actividades, viajes o planes de ocio o planes de ocio porque debe cambiarse frecuentemente el tampón o la compresa?',
        'options': ['Sí', 'No'],
    }
]

def determine_alert(answers):
    confirmations = 0
    for answer in answers:
        if answer == 'Sí':
            confirmations += 1
    alert = ''
    # redirect to home
    if confirmations >= 3 and score >= 100 :
        alert = 'Debería ir a ver a un profesional'
    else:
        alert = 'Todo gucci'
    return '<script>alert("' + alert + '"); window.location.href = "/";</script>'
