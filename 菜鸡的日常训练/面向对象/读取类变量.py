class ReadClassName():
    SHIPPER_STATE = "B21"
    SHIPPER_ENTERPRISE = "B22"
    SHIPPER_EMAIL = "B23"
    SHIPPER_TEL = "B24"

    CONSIGNEE_STATE = "D21"
    CONSIGNEE_ENTERPRISE = "D22"
    CONSIGNEE_EMAIL = "D23"
    CONSIGNEE_TEL = "D24"

    NOTIFY_STATE = "F21"
    NOTIFY_ENTERPRISE = "F22"
    NOTIFY_EMAIL = "F23"
    NOTIFY_TEL = "F24"

print(ReadClassName.__dict__.items())

