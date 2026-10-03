# 1. Membuat dictionary bernama test_settings untuk menyimpan preferensi
test_settings = {
    "theme": "dark",
    "language": "indonesian",
    "notifications": "enabled"
}

# 2-8. Fungsi add_setting
def add_setting(settings, setting_tuple):
    # Mengubah key dan value menjadi lowercase (huruf kecil semua)
    key = setting_tuple[0].lower()
    value = setting_tuple[1].lower()
    
    # Jika key sudah ada, kembalikan pesan error
    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    
    # Jika belum ada, tambahkan ke dictionary dan kembalikan pesan sukses
    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"


# 9-15. Fungsi update_setting
def update_setting(settings, setting_tuple):
    # Mengubah key dan value menjadi lowercase
    key = setting_tuple[0].lower()
    value = setting_tuple[1].lower()
    
    # Jika key ada, update nilainya
    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    
    # Jika key tidak ada, kembalikan pesan error
    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


# 16-21. Fungsi delete_setting
def delete_setting(settings, key):
    # Mengubah key menjadi lowercase
    key = key.lower()
    
    # Jika key ada, hapus dari dictionary
    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"
    
    # Jika key tidak ada, kembalikan pesan error
    return "Setting not found!"


# 22-27. Fungsi view_settings
def view_settings(settings):
    # Jika dictionary kosong
    if not settings:
        return "No settings available."
    
    # Mulai string dengan "Current User Settings:" dan baris baru (\n)
    result = "Current User Settings:\n"
    
    # Loop melalui setiap item, capitalize huruf pertama key, dan akhiri dengan \n
    for k, v in settings.items():
        result += f"{k.capitalize()}: {v}\n"
    
    return result