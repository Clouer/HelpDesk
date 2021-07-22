def register_user(model, cleaned_form):
    model.objects.create_user(
        username=cleaned_form['username'],
        password=cleaned_form['password'],
        first_name=cleaned_form['first_name'],
        last_name=cleaned_form['last_name']
    )


def create_request(model, cleaned_data):
    model.objects.create(
        title=cleaned_data['title'],
        description=cleaned_data['description'],
        owner=cleaned_data['owner']
    )


def close_request(model, request_id):
    request = model.objects.get(pk=request_id)
    request.status = 'closed'
    request.save()


def create_comment(model, message, owner_id, request_id):
    model.objects.create(
        message=message,
        owner=owner_id,
        request=request_id
    )
