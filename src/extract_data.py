import re
import json
from datetime import datetime
from src.owner_info import OwnerInfo
from src.inventory import Inventory

def extract_data(aligned_content):
    owner_info = OwnerInfo()
    inventory_list = []
    possible_areas = {'Living Room', 'Kitchen', 'Garage', 'Office', 'Bedroom', 'Dining Room'}
    possible_sources = {'Target', 'Walmart', 'Wayfair', 'Home Depot', 'Amazon', 'Best Buy'}
    reading_inventory = False
    for line in aligned_content:
        if line.startswith("Name"):
            owner_info.owner_name = line.split("Name", 1)[1].strip()
        elif line.startswith("Address"):
            street_no_name = line.split("Address", 1)[1].strip()
        elif "Phone Number" in line:
            owner_info.owner_telephone = line.split("Phone Number", 1)[1].strip()
        elif line.startswith("City, Zip, Address"):
            city_zip_address = line.split("City, Zip, Address", 1)[1].strip()
            owner_info.owner_address = f"{street_no_name}, {city_zip_address}"
        elif line.startswith("S/N") and "Item Description" in line:
            reading_inventory = True
            continue
        
        # Process inventory items
        elif reading_inventory:
            stripped_line = line.replace('$', '').strip()
            if not re.match(r'^\d+\s', stripped_line):
                continue
            tokens = stripped_line.split()
            sn = tokens[0]
            remaining_tokens = tokens[1:]

            # Extract Area
            area = None
            if len(remaining_tokens) >= 2 and ' '.join(remaining_tokens[:2]) in possible_areas:
                area = ' '.join(remaining_tokens[:2])
                remaining_tokens = remaining_tokens[2:]
            elif remaining_tokens and remaining_tokens[0] in possible_areas:
                area = remaining_tokens[0]
                remaining_tokens = remaining_tokens[1:]
            else:
                continue

            # Extract Source
            source = None
            source_found = False
            sorted_sources = sorted(possible_sources, key=lambda x: len(x.split()), reverse=True)
            for candidate in sorted_sources:
                parts = candidate.split()
                parts_len = len(parts)
                for i in range(len(remaining_tokens) - parts_len + 1):
                    if remaining_tokens[i:i+parts_len] == parts:
                        source = candidate
                        description_tokens = remaining_tokens[:i]
                        remaining_tokens = remaining_tokens[i+parts_len:]
                        source_found = True
                        break
                if source_found:
                    break
            if not source:
                continue

            # Extract Description
            description = ' '.join(description_tokens) if description_tokens else ''

            # Remaining fields
            if len(remaining_tokens) < 4:
                continue
            date_str, style, serial_number, value_str = remaining_tokens[:4]
            try:
                purchase_date = datetime.strptime(date_str, "%d/%m/%Y").isoformat()
            except ValueError:
                continue

            try:
                value = float(value_str.replace('$', '').replace(',', ''))
            except ValueError:
                continue

            source_style_area = f"{source}, {style}, {area}"
            inventory = Inventory(purchase_date, serial_number, description, source_style_area, value)
            inventory_list.append(inventory)

        
        final_response = {
            "owner_name": owner_info.owner_name,
            "owner_address": owner_info.owner_address,
            "owner_telephone": owner_info.owner_telephone,
            "data": [
                {
                    "purchase_date": inv.purchase_date,
                    "serial_number": inv.serial_number,
                    "description": inv.description,
                    "source_style_area": inv.source_style_area,
                    "value": inv.value
                }
                for inv in inventory_list
            ]
        }
        final_response_json = json.dumps(final_response, indent=4)
    return final_response_json