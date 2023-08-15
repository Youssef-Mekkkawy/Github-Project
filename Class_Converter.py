import math

class Converter:

    def __init__(self):
        self.size_names = ("B", "KB", "MB", "GB", "TB", "PB")

    def get_size_index(self, unit):
        unit = unit.upper()
        if unit in self.size_names:
            return self.size_names.index(unit)
        return None

    def convert_bytes(self, size_bytes, unit="B", base=1000):
        size_index = self.get_size_index(unit)
        
        if size_index is None:
            return "Error: Unsupported unit"
        
        power = math.pow(base, size_index)
        size = round(size_bytes / power, 2)
        
        return size, self.size_names[size_index]

    def convert_bytes_advanced(self, input_str, base=1000):
        try:
            size_str, unit = input_str.split()
            size_bytes = float(size_str)
        except ValueError:
            return "Error: Input should be in the format '10GB'"

        size_index = self.get_size_index(unit)
        
        if size_index is None:
            return "Error: Unsupported unit"
        
        power = math.pow(base, size_index)
        size = round(size_bytes * power, 2)
        
        return size, self.size_names[size_index]

# Example usage
converter = Converter()
print(converter.convert_bytes(1024, "KB"))  # Output: (1.0, 'KB')
print(converter.convert_bytes_advanced("10GB"))  # Output: (10000000000.0, 'GB')
