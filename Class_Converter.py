import math

class Converter:

    def __init__(self):
        self.size_names_decimal = ("B", "KB", "MB", "GB", "TB", "PB")
        self.size_names_binary = ("B", "KiB", "MiB", "GiB", "TiB", "PiB")
        
    @staticmethod
    def if_size_equal_zero(size):
        if size == 0:
            return "0B", 0, "B"
    
    def bytes_calculation(self, size_bytes, unit="B", base=1000):
        try:
            unit = unit.upper()
        except Exception as e:
            return "Unit can't be empty"
        
        if unit in self.size_names_binary or unit in self.size_names_decimal:
            exponent = self.size_names_decimal.index(unit)
            multiplier = math.pow(base, exponent)
            calculated_size = size_bytes * multiplier
            size = round(calculated_size, 2)
            
            if base == 1000:
                size_name = self.size_names_decimal[exponent]
            elif base == 1024:
                size_name = self.size_names_binary[exponent]
            else:
                return "Please use Decimal (1000) or Binary (1024)"
            
            return size, size_name
        else:
            return "Unit not supported."

    def calculation(self, size_bytes, base=1000):
        exponent = int(math.floor(math.log(size_bytes, base)))
        multiplier = math.pow(base, exponent)
        size = round(size_bytes / multiplier, 2)
        
        if base == 1000:
            size_name = self.size_names_decimal[exponent]
        elif base == 1024:
            size_name = self.size_names_binary[exponent]
        else:
            return "Please use Decimal (1000) or Binary (1024)"
        
        return size, size_name

    def decimal_byte(self, size_bytes):
        self.if_size_equal_zero(size_bytes)
        size, size_name = self.calculation(size_bytes, 1000)
        return f"{size} {size_name}", size, size_name

    def binary_byte(self, size_bytes):
        self.if_size_equal_zero(size_bytes)
        size, size_name = self.calculation(size_bytes, 1024)
        return f"{size} {size_name}", size, size_name

if __name__ == "__main__":
    unit_converter = Converter()
    print(unit_converter.bytes_calculation(29929612))
    print(unit_converter.calculation(29929612))
