from app.core.database import Base

# Пользователи и связанные таблицы
from app.models.user import User
from app.models.session import Session
from app.models.device_token import DeviceToken
from app.models.user_favorite import UserFavorite

# Владельцы и магазины
from app.models.shop import Shop
from app.models.owner_account import OwnerAccount
from app.models.owner_shop import OwnerShop
from app.models.shop_account import ShopAccount
from app.models.shop_device_token import ShopDeviceToken

# Меню и опции
from app.models.menu_item import MenuItem
from app.models.item_option_group import ItemOptionGroup
from app.models.item_option import ItemOption

# Временные слоты и резервы
from app.models.time_slot import TimeSlot
from app.models.slot_hold import SlotHold

# Заказы, позиции и платежи
from app.models.order import Order
from app.models.order_item import OrderItem
from app.models.order_item_option import OrderItemOption
from app.models.payment import Payment

