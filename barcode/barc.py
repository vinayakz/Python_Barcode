import barcode
from barcode.writer import ImageWriter
hr =barcode.get_barcode_class('code39')
Hr = hr('1234567891011',writer=ImageWriter())
qr=Hr.save('1234')