import math 

class Conveter:

    def __init__(self):

        self.size_name = ("B", "KB", "MB", "GB", "TB", "PB")

        self.Values = {
            
            "B":0, 
            "KB":1,
            "MB":2, 
            "GB":3, 
            "TB":4, 
            "PB":5
        }

        
    # Check if Size Equal Zero.
    def if_Size_Equal_Zero(self, Size):
        
        if Size == 0:
            return "0B", "0", "B"

    """ 

        This Function Convert KB, MG, GB, TB ,PB To Byte.
        Depend on What You Add in Unit.

    """
    def Bytes_Calulation(self, size_bytes:int, UNIT:str = [ "B" , "KB" , "MG" , "GB" ,"TP" , "PB" , "KIB" , "MIB" , "GIB", "TB" , "PB"], Type:int = 1000 | 1024):
        UNIT = UNIT.upper()

        if UNIT in self.size_name:
            if self.Values[UNIT]:
                i = self.Values[UNIT]
                
            else:
                return "Not Supported."
        else:
            return "Error Found: Be Sure You Choose Alright Unit\nYour Input Should Like That {10GB or 10gb or 10 GB}\n"
        
        p = math.pow(Type, i)
        s = size_bytes * p
        size = round(s, 2)

        if Type == 1000:
            return size, self.size_name[0]

        elif Type == 1024:
            return size, self.size_name[0]

        else:
            return "Please Use Decimal-> {1000} or Binary-> {1024}"

    def Bytes_Calulation_Advanced(self, size_bytes, UNIT:str = None, Type:int = 1000 | 1024):

        if UNIT == None: 
            try:
                UNIT:str = ''.join([i for i in size_bytes if not i.isdigit()]).strip()
                size_bytes:float = float(''.join([i for i in size_bytes if not i.isalpha()]).strip())
            except Exception as e:
                return f"Error Found: Be Sure You Choose Alright Unit\nYour Input Should Like That 10GB or 10gb or 10 GB\n {e}"

        UNIT = UNIT.replace(".", "").upper().strip()

        if UNIT in self.size_name:
            if self.Values[UNIT]:
                i = self.Values[UNIT]
            else:
                return "Not Supported."
        else:
            return "Error Found: Be Sure You Choose Alright Unit\nYour Input Should Like That {10GB or 10gb or 10 GB}\n"


        p = math.pow(Type, i)
        s = size_bytes * p
        size = round(s, 2)
        if Type == 1000:
            return size, self.size_name[0]
        elif Type == 1024:
            return size, self.size_name[0]
        else:
            return "Please Use Decimal-> {1000} or Binary-> {1024}"
    """ 
    
        This Function Convert Byte To KB, MG, GB, TB ,PB.

    """
    def Size_Calulation(self, size_bytes:int, Type:int = 1000 | 1024) -> tuple:

        i = int(math.floor(math.log(size_bytes, Type)))
        p = math.pow(Type, i)

        size = round(size_bytes / p, 2)

        if Type == 1000:
            return size, self.size_name[i]

        elif Type == 1024:
            return size, self.size_name[i]

        else:
            return "Please Use Decimal-> {1000} or Binary-> {1024}"
        
    """ 
    
        This Function Convert Byte To KB, MG, GB, TB ,PB. By Using Decimal {1000}

    """

    def decimal_byte(self, size_bytes:int):

        Conveter.if_Size_Equal_Zero(self, size_bytes)
        size, SIZE_NAME = Conveter.Size_Calulation(self, size_bytes, 1000)

        return f"{size} {SIZE_NAME}", size, SIZE_NAME

    """ 
    
        This Function Convert Byte To KIB, MIG, GIB, TIB ,PIB. By Using Binary {1024}

    """
    def binary_byte(self, size_bytes:int):

        Conveter.if_Size_Equal_Zero(self, size_bytes)
        size, SIZE_NAME = Conveter.Size_Calulation(self, size_bytes, 1024)

        return f"{size} {SIZE_NAME}", size, SIZE_NAME








