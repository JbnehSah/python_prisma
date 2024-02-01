from typing import List
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from src.prisma import prisma
import json

router = APIRouter()


class Users(BaseModel):
  id:    int
  email: str
  name:  str | None = None
  phone: str | None = None

class Products(BaseModel):
  id:    int
  name:  str
  desc:  str | None = None
  price: int  

class AddonsCombo(BaseModel):
  id:       int
  name:     str
  desc:     str | None = None
  price:    str  
  products: List[Products]


@router.get("/users", tags=["users"])
async def read_users():
  result = await prisma.users.find_many()
  return result


@router.get("/users/{userId}", tags=["users"])
async def find_user_by_id(userId: int):
    found = await prisma.users.find_unique(
    where= {
        'id': userId
  },
)
    return found

    
@router.get("/users/mail/{email}", tags=["users"])
async def find_user(email: str):
    by_mail = await prisma.users.find_unique(
    where= {
        'email': email
    },
)
    return by_mail


@router.post("/users/create", tags=["users"])
async def user_and_contact(user:Users):

  created_user = await prisma.users.create(
    data = {
      'email': user.email,
      'name':  user.name,
      'phone': user.phone,
    },
  ),
  return created_user


@router.post("/addonscombo/create", tags=["addoncombo"])
async def create_addoncombo(addon: AddonsCombo):
  created_addons_combo = await prisma.addonscombo.create(
  data = {
    'name':     addon.name,
    'desc':     addon.desc,
    'price':    addon.price,
    'products': {
      'connectOrCreate': 
      addon.products,
    },
  },
),
  return created_addons_combo

@router.get("/products", tags=["products"])
async def read_products():
  result = await prisma.products.find_many()
  return result

@router.get("/products/{productId}", tags=["products"])
async def find_product_by_id(productId: int):
    user = await prisma.products.find_unique(
    where= {
        'id': productId
  }
)
    return user

@router.post("/products/create", tags=["products"])
async def create_product(product: Products):
  created_product = await prisma.products.create(
  data = {
    'name':  product.name,
    'desc':  product.desc,
    'price': product.price,
  },
),
  return  created_product
