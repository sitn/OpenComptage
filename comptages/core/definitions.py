IMPORT_STATUS_QUARANTINE = 1
IMPORT_STATUS_DEFINITIVE = 0


# Definitions of the layers
LAYER_DEFINITIONS = {
    "installation": {
        "table": "installation",
        "display_name": "installation",
        "geometry": "geometry",
        "sql": "",
        "id": "id",
        "epsg": "EPSG:2056",
        "legend": True,
    },
    "sensor": {
        "table": "sensor",
        "display_name": "capteur",
        "geometry": "geometry",
        "sql": "",
        "id": "id",
        "epsg": "EPSG:2056",
        "legend": True,
    },
    "section": {
        "table": "section",
        "display_name": "troncon",
        "geometry": "geometry",
        "sql": "",
        "id": "id",
        "epsg": "EPSG:2056",
        "legend": True,
    },
    "municipality": {
        "table": "municipality",
        "display_name": "commune",
        "geometry": "geometry",
        "sql": "",
        "id": "id",
        "epsg": "EPSG:2056",
        "legend": True,
    },
    "sector": {
        "table": "sector",
        "display_name": "secteur",
        "geometry": "geometry",
        "sql": "",
        "id": "id",
        "epsg": "EPSG:2056",
        "legend": True,
    },
    "brand": {
        "table": "brand",
        "display_name": "marque",
        "geometry": None,
        "sql": "",
        "id": "id",
        "epsg": "EPSG:2056",
        "legend": False,
    },
    "model": {
        "table": "model",
        "display_name": "model",
        "geometry": None,
        "sql": "",
        "id": "id",
        "epsg": "EPSG:2056",
        "legend": False,
    },
    "device": {
        "table": "device",
        "display_name": "automate",
        "geometry": None,
        "sql": "",
        "id": "id",
        "epsg": "EPSG:2056",
        "legend": False,
    },
    "class": {
        "table": "class",
        "display_name": "classification",
        "geometry": None,
        "sql": "",
        "id": "id",
        "epsg": "EPSG:2056",
        "legend": False,
    },
    "category": {
        "table": "category",
        "display_name": "categorie",
        "geometry": None,
        "sql": "",
        "id": "id",
        "epsg": "EPSG:2056",
        "legend": False,
    },
    #     'count_detail': {
    #         'table':        'count_detail',
    #         'display_name': 'comptage_detail',
    #         'geometry':     None,
    #         'sql':          '',
    #         'id':           'id',
    #         'epsg':         'EPSG:2056',
    #         'legend':       False
    #     },
    #     'count_aggregate': {
    #         'table':        'count_aggregate',
    #         'display_name': 'comptage_aggrege',
    #         'geometry':     None,
    #         'sql':          '',
    #         'id':           'id',
    #         'epsg':         'EPSG:2056',
    #         'legend':       False
    #     },
    "damage_log": {
        "table": "damage_log",
        "display_name": "journal_panne",
        "geometry": None,
        "sql": "",
        "id": "id",
        "epsg": "EPSG:2056",
        "legend": False,
    },
    "special_period": {
        "table": "special_period",
        "display_name": "periode_speciale",
        "geometry": None,
        "sql": "",
        "id": "id",
        "epsg": "EPSG:2056",
        "legend": False,
    },
    "count": {
        "table": "count",
        "display_name": "comptage",
        "geometry": None,
        "sql": "",
        "id": "id",
        "epsg": "EPSG:2056",
        "legend": True,
    },
    "sensor_type": {
        "table": "sensor_type",
        "display_name": "type_capteur",
        "geometry": None,
        "sql": "",
        "id": "id",
        "epsg": "EPSG:2056",
        "legend": False,
    },
    "lane": {
        "table": "lane",
        "display_name": "voie",
        "geometry": None,
        "sql": "",
        "id": "id",
        "epsg": "EPSG:2056",
        "legend": False,
    },
}
