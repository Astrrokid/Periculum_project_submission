class Inventory:
    """
    A class representing an inventory item.

    Attributes:
        purchase_date (str): The date the item was purchased.
        serial_number (str): The unique serial number of the item.
        description (str): A brief description of the item.
        source_style_area (str): The source, style, or area of the item.
        value (float): The monetary value of the item.

    Methods:
        __init__(self, purchase_date, serial_number, description, source_style_area, value):
            Initializes an instance of the Inventory class with the given attributes.
    """

    def __init__(self, purchase_date, serial_number, description, source_style_area, value):
        """
        Initializes an instance of the Inventory class.

        Args:
            purchase_date (str): The date the item was purchased.
            serial_number (str): The unique serial number of the item.
            description (str): A brief description of the item.
            source_style_area (str): The source, style, and area of the item.
            value (float): The monetary value of the item.
        """
        self.purchase_date = purchase_date
        self.serial_number = serial_number
        self.description = description
        self.source_style_area = source_style_area
        self.value = value
