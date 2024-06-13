import django_setup
from django_project.models import User

# user1 = User(
#     name = "Матвій",
#     email = "matviy@gmail.com",
#     role = "admin"
# )
# user1.save()

while True:
    print("\n1. Додати юзера")
    print("2. Змінити роль")
    print("3. Вийти")

    choice = input("Оберіть опцію (1-7): ")

    if choice == "1":
        name = input("Вкажи ім'я")
        email = input("Вкажи електронну пошту")
        role = input("Вкажи свою роль")
        new_user = User(name=name, email=email, role=role)
        new_user.save()
    if choice == "2":
        user_id = input("Вкажи айді юзера")
        update_user = User.objects.filter(id = user_id).first()
        if update_user:
            new_role = input("Вкажи нову роль")
            update_user.role = new_role
            update_user.save()
        else:
            print("Не знайдено користувача")
    if choice == "3":
        break






