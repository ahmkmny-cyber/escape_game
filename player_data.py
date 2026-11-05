import csv


FILE_NAME = "users.csv"
def update_room_badge(
    username,
    room_number,
    badge
):

    rows = []

    with open(
        FILE_NAME,
        "r",
        newline=""
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:

            if row["username"] == username:

                badge_column = (
                    "room"
                    + str(room_number)
                    + "_badge"
                )

                row[badge_column] = badge

            rows.append(row)

    with open(
        FILE_NAME,
        "w",
        newline=""
    ) as file:

        fieldnames = [
            "username",
            "password",
            "room1_badge",
            "room2_badge",
            "room3_badge"
        ]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        writer.writerows(rows)


# =========================================================
# GET PLAYER DATA
# =========================================================

def get_player_data(username):

    with open(
        FILE_NAME,
        "r",
        newline=""
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:

            if row["username"] == username:

                return row

    return None