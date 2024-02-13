from django.apps import AppConfig


class DashboardConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "dashboard"




# 2 model  -> Done
# list api -> status filter add
# api documentation
# unit test case


# POST endpoints x2
# Auth routh + JWT



# search 
#     /api/items?search='dhan' 
#     value = self.request.query_params.get('search')
#     DB Query => where clause name = value

# sort
#     /api/items?sort='ASC/DESC' 
#     value = self.request.query_params.get('sort')
#     DB Query => order by clause value

# filter
#     /api/items?sort='ASC/DESC' 
#     value = self.request.query_params.get('sort')
#     DB Query => order by clause value

# [
#     {
#         "id": 1111,
#         "sku": "1111",
#         "name": "ascac",
#         "category": "ZAA",
#         "tags": "axxs",
#         "stock_status": "ACTIVE",
#         "available_stock": 12
#     },
#      {
#         "id": 1111,
#         "sku": "1111",
#         "name": "ascac",
#         "category": "ZAA",
#         "tags": "axxs",
#         "stock_status": "ACTIVE",
#         "available_stock": 12
#     },
#      {
#         "id": 1111,
#         "sku": "1111",
#         "name": "ascac",
#         "category": "ZAA",
#         "tags": "axxs",
#         "stock_status": "ACTIVE",
#         "available_stock": 12
#     }
# ]

