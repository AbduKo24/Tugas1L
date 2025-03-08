def hitung_biaya_pengiriman(berat, jarak, jenis_pengiriman, is_member):

# Biaya dasar
biaya_dasar = 10000
total_biaya = biaya_dasar
Tambahan biaya berdasarkan beratif berat > 5:
total_biaya += 5000Tambahan biaya berdasarkan jarakif jarak > 10:
total_biaya += 8000Tambahan biaya untuk pengiriman expressif jenis_pengiriman.lower() == 'express':
total_biaya += 20000Diskon untuk memberif is_member:
total_biaya *= 0.9  # Diskon 10%
return total_biaya
