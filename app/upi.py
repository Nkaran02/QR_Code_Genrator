from decimal import Decimal
from urllib.parse import urlencode

import qrcode

def create_upi_uri(upi_id : str, name: str, amount: Decimal, note: str | None = None) -> str:
    params = {
        "pa": upi_id,
        "pn":name,
        "am":f"{amount:.2f}",
        "cu":"INR",
    }


    if note:
        params["tn"] = note

    return "upi://pay?" + urlencode(params)


def create_qr_code(upi_uri:str) -> bytes:
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,   
    )

    qr.add_data(upi_uri)
    qr.make(fit=True)

    image = qr.make_image()

    from io import BytesIO

    buffer = BytesIO()
    image.save(buffer, format="PNG")

    return buffer.getvalue()



