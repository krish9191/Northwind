from extension import db

from model.regions import Region, Territory
from flask import jsonify, request


def to_str_date(model_date):
    str_date = model_date.strftime('%Y/%m/%d')
    return str_date


def byte_array_to_json(byte_array):
    new_array = byte_array.decode('utf8')
    return new_array


def add_region(description):
    region_description = description
    region = Region(region_description)
    id = region.region_id
    db.session.add(region, id)
    db.session.commit()
    return jsonify(
        region_description=description
    )


def add_territory(region_id):
    region = Region.find_by_id(region_id)
    data = request.get_json()
    territory_description = data["description"]
    territory = Territory(territory_description)
    region.territories.append(territory)

    db.session.commit()
    return jsonify(
        territory_description=territory_description

    )
