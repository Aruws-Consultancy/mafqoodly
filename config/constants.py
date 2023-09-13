class Options:
    mafqood = {
        "gender": (
            ("O+", "O+"),
            ("O-", "O-"),
            ("A+", "A+"),
            ("A", "-"),
            ("B+", "B+"),
            ("B", "B-"),
            ("AB", "AB+"),
            ("AB-", "AB-"),
        ),
        "blod_type": (
            ("male", "ذكر"),
            ("female", "انثى"),
        ),
        "status": (
            ("missing", "Missing"),
            ("found", "Found"),
            ("deceased", "Deceased"),
        )
    }
