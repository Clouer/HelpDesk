def register_user(model, cleaned_form):
    model.objects.create_user(
        username=cleaned_form['username'],
        password=cleaned_form['password'],
        first_name=cleaned_form['first_name'],
        last_name=cleaned_form['last_name']
    )
