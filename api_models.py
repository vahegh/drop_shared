from pydantic import BaseModel, EmailStr, PositiveFloat
from datetime import datetime
from uuid import UUID
from typing import Optional
from enums import PersonStatus, PaymentStatus, PaymentProvider


class VenueCreate(BaseModel):
    name: str
    address: Optional[str] = None
    latitude: float
    longitude: float
    google_maps_link: str
    yandex_maps_link: str


class VenueUpdate(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    google_maps_link: Optional[str] = None
    yandex_maps_link: Optional[str] = None


class VenueResponse(BaseModel):
    id: UUID
    name: str
    address: Optional[str]
    latitude: float
    longitude: float
    google_maps_link: str
    yandex_maps_link: str

    class Config:
        from_attributes = True


class PersonCreate(BaseModel):
    name: str
    email: EmailStr
    instagram_handle: Optional[str] = None
    telegram_handle: Optional[str] = None


class PersonUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    instagram_handle: Optional[str] = None
    telegram_handle: Optional[str] = None
    status: Optional[PersonStatus] = None


class PersonResponse(BaseModel):
    id: UUID
    name: str
    email: EmailStr
    instagram_handle: Optional[str]
    telegram_handle: Optional[str]
    status: PersonStatus

    class Config:
        from_attributes = True


class MemberCardCreate(BaseModel):
    person_id: UUID


class MemberCardResponse(BaseModel):
    id: UUID
    serial_number: int
    person_id: UUID
    apple_pass_url: str
    google_pass_url: str
    last_updated: datetime

    class Config:
        from_attributes = True


class EventCreate(BaseModel):
    name: str
    starts_at: datetime
    ends_at: Optional[datetime] = None
    early_bird_date: Optional[datetime] = None
    venue_id: UUID
    image_url: Optional[str] = None
    description: Optional[str] = None
    early_bird_price: Optional[int] = None
    general_admission_price: Optional[int] = None
    member_ticket_price: Optional[int] = None
    max_capacity: Optional[int] = None
    shared: Optional[bool] = False


class EventResponse(BaseModel):
    id: UUID
    name: str
    starts_at: datetime
    ends_at: Optional[datetime]
    early_bird_date: Optional[datetime] = None
    venue_id: UUID
    image_url: Optional[str]
    description: Optional[str]
    early_bird_price: Optional[int] = None
    general_admission_price: Optional[int] = None
    member_ticket_price: Optional[int]
    max_capacity: Optional[int]
    shared: bool

    class Config:
        from_attributes = True


class EventUpdate(BaseModel):
    name: Optional[str] = None
    starts_at: Optional[datetime] = None
    ends_at: Optional[datetime] = None
    early_bird_date: Optional[datetime] = None
    venue_id: Optional[UUID] = None
    image_url: Optional[str] = None
    description: Optional[str] = None
    early_bird_price: Optional[int] = None
    general_admission_price: Optional[int] = None
    member_ticket_price: Optional[int] = None
    max_capacity: Optional[int] = None
    shared: Optional[bool] = False


class EventTicketCreate(BaseModel):
    person_id: UUID
    event_id: UUID
    payment_order_id: Optional[int] = None


class EventTicketResponse(BaseModel):
    id: UUID
    person_id: UUID
    event_id: UUID
    payment_order_id: Optional[int] = None
    is_used: bool
    apple_pass_url: Optional[str] = None
    google_pass_url: Optional[str] = None
    last_updated: datetime
    is_sent: bool

    class Config:
        from_attributes = True


class RegistrationRequest(BaseModel):
    pushToken: str


class UpdatedPassesResponse(BaseModel):
    serialNumbers: list[UUID]
    lastUpdated: str


class LogRequest(BaseModel):
    logs: list[str]


class SendLink(BaseModel):
    email: str
    event_id: UUID


# class PaymentCreate(BaseModel):
#     person_id: UUID
#     event_id: UUID
#     request_id: str
#     pay_url: str

#     class Config:
#         from_attributes = True


# class PaymentResponse(BaseModel):
#     id: UUID
#     person_id: UUID
#     event_id: UUID
#     request_id: str
#     pay_url: str
#     status: PaymentStatus
#     created_at: datetime
#     updated_at: datetime

#     class Config:
#         from_attributes = True


# class PaylinkPaymentRequest(BaseModel):
#     requestType: str
#     amount: float
#     isFlexible: bool
#     allowAnonymous: bool
#     isActive: bool
#     backUrl: Optional[str] = f"{APP_BASE_URL}/success"
#     language: Optional[str] = 'en'
#     maxCount: Optional[int] = 1


class PaymentCreate(BaseModel):
    person_id: UUID
    event_id: UUID
    amount: PositiveFloat
    provider: PaymentProvider
    ticket_holders: list[UUID]


class PaymentResponse(BaseModel):
    order_id: int
    person_id: UUID
    event_id: UUID
    amount: float
    provider: PaymentProvider
    ticket_holders: list[UUID]
    upstream_payment_id: Optional[str] = None
    status: PaymentStatus
    created_at: datetime
    updated_at: Optional[datetime] = None


# payment providers
class VposInitPaymentRequest(BaseModel):
    ClientID: str
    Username: str
    Password: str
    Description: str
    OrderID: int
    Amount: float
    BackURL: Optional[str] = None
    Opaque: Optional[str] = None


class MyAmeriaCreateRequest(BaseModel):
    transactionAmount: float
    transactionId: Optional[str] = None
    merchantId: Optional[str] = None
    isBindingEnabled: bool = False
    userId: Optional[str] = None


class VPOSPaymentDetailsRequest(BaseModel):
    Username: str
    Password: str
    PaymentID: UUID


class VPOSPaymentDetailsResponse(BaseModel):
    Amount: Optional[float] = None
    ApprovedAmount: Optional[float] = None
    ApprovalCode: Optional[str] = None
    CardNumber: Optional[str] = None
    ClientName: Optional[str] = None
    ClientEmail: Optional[str] = None
    Currency: Optional[str] = None
    DateTime: Optional[str] = None
    DepositedAmount: Optional[float] = None
    Description: Optional[str] = None
    MerchantId: Optional[str] = None
    Opaque: Optional[str] = None
    OrderID: Optional[int] = None
    PaymentState: Optional[str] = None
    PaymentType: Optional[int] = None
    ResponseCode: Optional[str] = None
    rrn: Optional[str] = None
    TerminalId: Optional[str] = None
    TrxnDescription: Optional[str] = None
    OrderStatus: Optional[int] = None
    RefundedAmount: Optional[float] = None
    CardHolderID: Optional[str] = None
    MDOrderID: Optional[str] = None
    PrimaryRC: Optional[str] = None
    ExpDate: Optional[str] = None
    ProcessingIP: Optional[str] = None
    BindingID: Optional[str] = None
    ActionCode: Optional[str] = None
    ExchangeRate: Optional[float] = None


class MyameriaPaymentDetailsResponse(BaseModel):
    isSuccessful: bool
    amount: float
    transactionId: str
    paymentId: UUID
    merchantId: str
    createdDate: datetime
    paymentDate: datetime
    isRefunded: bool
    refundedAmount: float
    refundedDate: Optional[datetime] = None
    bindId: Optional[UUID] = None
    labels: Optional[dict] = None


class MyameriaPaymentDetailsRequest(BaseModel):
    transactionId: str
    paymentId: UUID
    merchantId: str


class PaymentConfirmRequest(BaseModel):
    order_id: int
    provider: PaymentProvider
    payment_id: Optional[UUID] = None


class PaymentConfirmResponse(BaseModel):
    order_id: int
    provider: PaymentProvider
    payment_id: Optional[UUID] = None
    status: PaymentStatus
    description: Optional[str] = None
    person_id: UUID
    event_id: UUID


class AttendanceResponse(BaseModel):
    id: UUID
    event_id: UUID
    person_id: UUID
    event_ticket_id: Optional[UUID] = None
    date_modified: Optional[datetime] = None


class ECRMPrintRequest(BaseModel):
    crn: int
    cardAmount: int
    cashAmount: int = 0
    partialAmount: int = 0
    prePaymentAmount: int = 0
    cashierId: int = 1
    mode: int = 3


class ECRMCheckConnRequest(BaseModel):
    crn: int


class ECRMResult(BaseModel):
    receiptId: str
    crn: str
    sn: str
    tin: str
    taxpayer: str
    address: str
    time: int
    fiscal: str
    total: int
    change: int
    qr: str


class ECRMResponse(BaseModel):
    code: int
    message: str
    result: ECRMResult | str
