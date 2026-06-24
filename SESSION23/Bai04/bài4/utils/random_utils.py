import random
import string as st


def generate_assignment_code():

    characters = st.ascii_uppercase + st.digits

    code = "".join(
        random.choices(characters, k=4)
    )

    return "PY-" + code