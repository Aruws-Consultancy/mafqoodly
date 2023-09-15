class Options:
    general = {
        "gender": (
            ("male", "ذكر"),
            ("female", "انثى"),
        ),
        "blod_type": (
            ("O+", "O+"),
            ("O-", "O-"),
            ("A+", "A+"),
            ("A", "-"),
            ("B+", "B+"),
            ("B", "B-"),
            ("AB", "AB+"),
            ("AB-", "AB-"),
        ),
    }

    mafqood = {
        "status": (
            ("missing", "Missing"),
            ("found", "Found"),
            ("deceased", "Deceased"),
        ),
    }

    people = {
        "status": (
            ("injured", "Injured"),
            ("deceased", "Deceased"),
            ("buried", "Buried"),
            ("idp", "IDP"),
        )
    }

    volunteer = {
        "status": (
            ("active", "Active"),
            ("inactive", "InActive"),
        )
    }
