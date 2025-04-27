class OwnerInfo:
    """
    A class representing the information of an owner.

    Attributes:
        owner_name (str, optional): The name of the owner. Defaults to None.
        owner_address (str, optional): The address of the owner. Defaults to None.
        owner_telephone (str, optional): The telephone number of the owner. Defaults to None.

    Methods:
        __init__(self, owner_name=None, owner_address=None, owner_telephone=None):
            Initializes an instance of the OwnerInfo class with the provided owner details.
    """

    def __init__(self, owner_name=None, owner_address=None, owner_telephone=None):
        """
        Initializes an instance of the OwnerInfo class.

        Args:
            owner_name (str, optional): The name of the owner. Defaults to None.
            owner_address (str, optional): The address of the owner. Defaults to None.
            owner_telephone (str, optional): The telephone number of the owner. Defaults to None.
        """
        self.owner_name = owner_name
        self.owner_address = owner_address
        self.owner_telephone = owner_telephone
