
resource "azurerm_storage_account" "cloudguard_demo" {
  name                     = "cloudguarddemostorage123"
  resource_group_name      = "demo-rg"
  location                 = "East US"
  account_tier             = "Standard"
  account_replication_type = "LRS"

allow_nested_items_to_be_public = false
https_traffic_only_enabled     = true
min_tls_version = "TLS1_2"
}
