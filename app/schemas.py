from decimal import Decimal
from pydantic import BaseModel, Field

class PaymentRequest(BaseModel):
    upi_id: str = Field(
        min_length=3,
        max_length=100
    )

    name: str = Field(
        min_length=1,
        max_length=100
    )


    amount: Decimal = Field(
        gt=0,
        decimal_places=2,
        max_digits=4
    )

    note: str | None = Field(
        default=None,
        max_length=300
    )