from pyscript import document, display

math_members= [
    ["Arianne", "Salamat"],
    ["Audrey", "Dela Cruz"],
    ["Daniella", "Guintu"],
    ["Joaquin", "Marquez"],
    ["Kaylie", "Manalansan"],
    ["Maia", "Rodolfo"],
    ["Renelito", "Bucad"],
    ["Sophia", "Joson"],
    ["Sydney", "de Leon"]
]

def check_name(e):
    first= document.getElementById("first_name").value.strip()
    last= document.getElementById("last_name").value.strip()
    message= document.getElementById("message")

    full_name= first + " " + last

    if first == "" or last == "":
        message.innerHTML= "please enter first name and last name."

    else:
        found = False

        for person in math_members:
            member_name = person[0] + " " + person[1]

            if full_name == member_name:
                found = True

        if found:
            message.innerHTML = "Congratulations " + full_name + "! You are now part of the Mathematics Club."
            message.style.backgroundColor = "#d4edda"
            message.style.color = "#155724"

        else:
            message.innerHTML = "Sorry " + full_name + ", your name is not on the list."
            message.style.backgroundColor = "#f8d7da"
            message.style.color = "#721c24"