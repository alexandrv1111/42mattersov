"""This module describes schema of downloads.json and playstore.json"""

schema_downloads = {
    "type": "object",
    "properties": {
        "estimates": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "td": {
                        "type": "string",
                        "format": "date"
                    },
                    "countries": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "country": {
                                    "type": "string"
                                },
                                "value": {
                                    "type": ["integer", "null"],
                                    "minimum": 0
                                }
                            },
                            "required": ["country", "value"]
                        }
                    }
                },
                "required": ["td", "countries"]
            }
        },
        "estimates_agg": {
            "type": "object",
            "patternProperties": {
                "^[A-Za-z]+$": {
                    "type": "integer"
                }
            }
        },
        "estimates_total": {
            "type": "string",
            "pattern": "^[0-9,]+$"
        },
        "regions": {
            "type": "object",
            "properties": {
                "EU": {
                    "type": "string"
                },
                "AS": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string"
                        },
                        "regions": {
                            "type": "object",
                            "properties": {
                                "ASEA": {
                                    "type": "string"
                                },
                                "ASCA": {
                                    "type": "string"
                                },
                                "ASSA": {
                                    "type": "string"
                                },
                                "ASSEA": {
                                    "type": "string"
                                },
                                "ASWA": {
                                    "type": "string"
                                }
                            }
                        }
                    }
                },
                "NA": {
                    "type": "string"
                },
                "OC": {
                    "type": "string"
                },
                "SA": {
                    "type": "string"
                },
                "AF": {
                    "type": "string"
                }
            }
        },
        "countries": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "cc": {
                        "type": "string",
                        "pattern": "^[A-Z]{2}$"
                    },
                    "name": {
                        "type": "string"
                    },
                    "region": {
                        "type": "object",
                        "properties": {
                            "code": {
                                "type": "string"
                            },
                            "name": {
                                "type": "string"
                            }
                        },
                        "required": ["code", "name"]
                    }
                },
                "required": ["cc", "name", "region"]
            }
        }
    },
    "required": ["estimates", "estimates_agg", "estimates_total", "regions", "countries"]
}


schema_playstore = {
    "$schema": "http://json-schema.org/draft-07/schema#",

    "type": "object",
    "properties": {
        "rating": {
            "type": "number", "minimum": 0, "maximum": 5
        },
        "package_name": {
            "type": "string"
        },
        "stores": {
            "type": "object",
            "properties": {
                "itunes": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "market_status": {
                                "type": "string",
                                "enum": ["PUBLISHED", "UNPUBLISHED"]
                            },
                            "trackId": {
                                "type": "integer"
                            }
                        },
                        # "required": ["market_status", "trackId"]
                    }
                }
            },
            # "required": ["itunes"]
        },
        "badges": {
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "developer": {
            "type": "string"
        },
        "price_currency": {
            "type": "string"
        },
        "iap_max": {
            "type": "number"
        },
        "icon_72": {
            "type": "string",
            "format": "uri"
        },
        "title": {
            "type": "string"
        },
        "privacy_policy": {
            "type": "string",
            "format": "uri"
        },
        "removed_timestamp": {
            "type": "integer"
        },
        "category": {
            "type": "string"
        },
        "version_code": {
            "type": "integer"
        },
        "version": {
            "type": "string"
        },
        "size": {
            "type": "integer"
        },
        "email": {
            "type": "string",
            "format": "email"
        },
        "physical_address": {
            "type": "string"
        },
        "cat_int": {
            "type": "integer"
        },
        "created": {
            "type": "string",
            "format": "date-time"
        },
        "market_update": {
            "type": "string",
            "format": "date-time"
        },
        "market_url": {
            "type": "string",
            "format": "uri"
        },
        "cat_key": {
            "type": "string",
            "enum": [
                'OVERALL',
                'APPLICATION',
                'GAME',
                'ART_AND_DESIGN',
                'AUTO_AND_VEHICLES',
                'BEAUTY',
                'BOOKS_AND_REFERENCE',
                'BUSINESS',
                'COMICS',
                'COMMUNICATION',
                'DATING',
                'EDUCATION',
                'ENTERTAINMENT',
                'EVENTS',
                'FINANCE',
                'FOOD_AND_DRINK',
                'HEALTH_AND_FITNESS',
                'HOUSE_AND_HOME',
                'LIFESTYLE',
                'MAPS_AND_NAVIGATION',
                'MEDICAL',
                'MUSIC_AND_AUDIO',
                'NEWS_AND_MAGAZINES',
                'PARENTING',
                'PERSONALIZATION',
                'PHOTOGRAPHY',
                'PRODUCTIVITY',
                'SHOPPING',
                'SOCIAL',
                'SPORTS',
                'TOOLS',
                'TRAVEL_AND_LOCAL',
                'VIDEO_PLAYERS',
                'WEATHER',
                'LIBRARIES_AND_DEMO',
                'GAME_ARCADE',
                'GAME_PUZZLE',
                'GAME_CARD',
                'GAME_CASUAL',
                'GAME_RACING',
                'GAME_SPORTS',
                'GAME_ACTION',
                'GAME_ADVENTURE',
                'GAME_BOARD',
                'GAME_CASINO',
                'GAME_EDUCATIONAL',
                'GAME_MUSIC',
                'GAME_ROLE_PLAYING',
                'GAME_SIMULATION',
                'GAME_STRATEGY',
                'GAME_TRIVIA',
                'GAME_WORD',
                'ANDROID_WEAR',
                'FAMILY',
                'FAMILY_ACTION',
                'FAMILY_BRAINGAMES',
                'FAMILY_CREATE',
                'FAMILY_EDUCATION',
                'FAMILY_MUSICVIDEO',
                'FAMILY_PRETEND'

            ]
        },
        "downloads": {
            "type": "string"
        },
        "from_developer": {
            "type": "array",
            "items": {"type": "string"}
        },
        "iap": {
            "type": "boolean"
        },
        "website": {
            "type": "string",
            "format": "uri"
        },
        "promo_video": {
            "type": "string",
            "format": "uri"
        },
        "screenshots_count": {
            "type": "integer"
        },
        "market_status": {
            "type": "string",
            "enum": ["PUBLISHED", "UNPUBLISHED"]
        },
        "price_numeric": {
            "type": "number"
        },
        "short_desc": {
            "type": "string"
        },
        "downloads_max": {
            "type": "integer"
        },
        "contains_ads": {
            "type": "boolean"
        },
        "description": {
            "type": "string"
        },
        "price": {
            "type": "string"
        },
        "age_approved_by_teachers": {
            "type": "string",
            "pattern": "Ages [0-9]{1,2}\\+|Ages [0-9]{1,2}-[0-9]{1,2}"
        },
        "downloads_min": {
            "type": "integer"
        },
        "promo_video_image": {
            "type": "string",
            "format": "uri"
        },
        "icon": {
            "type": "string",
            "format": "uri"
        },
        "lang": {
            "type": "string"
        },
        "ratings_5": {
            "type": "integer"
        },
        "iap_min": {
            "type": "number"
        },
        "content_rating": {
            "type": "string"
        },
        "ratings_4": {
            "type": "integer"
        },
        "cat_type": {
            "type": "integer",
            "enum": [0, 1]
        },
        "ratings_2": {
            "type": "integer"
        },
        "ratings_3": {
            "type": "integer"
        },
        "ratings_1": {
            "type": "integer"
        },
        "cat_keys": {
            "type": "array",
            "items": {
                "type": "string",
                "enum": [
                    'OVERALL',
                    'APPLICATION',
                    'GAME',
                    'ART_AND_DESIGN',
                    'AUTO_AND_VEHICLES',
                    'BEAUTY',
                    'BOOKS_AND_REFERENCE',
                    'BUSINESS',
                    'COMICS',
                    'COMMUNICATION',
                    'DATING',
                    'EDUCATION',
                    'ENTERTAINMENT',
                    'EVENTS',
                    'FINANCE',
                    'FOOD_AND_DRINK',
                    'HEALTH_AND_FITNESS',
                    'HOUSE_AND_HOME',
                    'LIFESTYLE',
                    'MAPS_AND_NAVIGATION',
                    'MEDICAL',
                    'MUSIC_AND_AUDIO',
                    'NEWS_AND_MAGAZINES',
                    'PARENTING',
                    'PERSONALIZATION',
                    'PHOTOGRAPHY',
                    'PRODUCTIVITY',
                    'SHOPPING',
                    'SOCIAL',
                    'SPORTS',
                    'TOOLS',
                    'TRAVEL_AND_LOCAL',
                    'VIDEO_PLAYERS',
                    'WEATHER',
                    'LIBRARIES_AND_DEMO',
                    'GAME_ARCADE',
                    'GAME_PUZZLE',
                    'GAME_CARD',
                    'GAME_CASUAL',
                    'GAME_RACING',
                    'GAME_SPORTS',
                    'GAME_ACTION',
                    'GAME_ADVENTURE',
                    'GAME_BOARD',
                    'GAME_CASINO',
                    'GAME_EDUCATIONAL',
                    'GAME_MUSIC',
                    'GAME_ROLE_PLAYING',
                    'GAME_SIMULATION',
                    'GAME_STRATEGY',
                    'GAME_TRIVIA',
                    'GAME_WORD',
                    'ANDROID_WEAR',
                    'FAMILY',
                    'FAMILY_ACTION',
                    'FAMILY_BRAINGAMES',
                    'FAMILY_CREATE',
                    'FAMILY_EDUCATION',
                    'FAMILY_MUSICVIDEO',
                    'FAMILY_PRETEND'

                ]
            }
        },
        "screenshots": {
            "type": "array",
            "items": {
                "type": "string",
                "format": "uri"
            }
        },
        "interactive_elements": {
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "sdks": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "website": {
                        "type": "string",
                        "format": "uri"
                    },
                    "platforms": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    },
                    "title": {
                        "type": "string"
                    },
                    "id": {
                        "type": "string"
                    },
                    "tags": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    }
                },
                # "required": ["website", "platforms", "title", "id", "tags"]
            }
        },
        "permissions": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "source": {
                        "type": "string"
                    },
                    "id": {
                        "type": "string"
                    },
                    "protection_level": {
                        "type": "string"
                    }
                },
                # "required": ["source", "id"]
            }
        },
        "app_availability": {
            "type": "object",
            "properties": {
                "pn": {
                    "type": "string"
                },
                "available_in": {
                    "type": "object",
                    "patternProperties": {
                        "^(AE|AM|AR|AT|AU|BE|BG|BR|BY|CA|CH|CL|CN|CO|CY|CZ|DE|DK|EE|EG|ES|FI|FR|GB|GE|GR|HK|HR|HU|ID"
                        "|IL|IN|IR|IT|JP|KR|LB|LT|LV|MX|MY|NG|NL|NO|NZ|PE|PH|PL|PT|RO|RS|RU|SA|SE|SG|SK|TH|TR|TW|UA"
                        "|US|VN|ZA)$": {
                            "type": "integer"}
                    },
                    "additionalProperties": False
                },
                "not_available_in": {
                    "type": "object",
                    "patternProperties": {
                        "^(AE|AM|AR|AT|AU|BE|BG|BR|BY|CA|CH|CL|CN|CO|CY|CZ|DE|DK|EE|EG|ES|FI|FR|GB|GE|GR|HK|HR|HU|ID"
                        "|IL|IN|IR|IT|JP|KR|LB|LT|LV|MX|MY|NG|NL|NO|NZ|PE|PH|PL|PT|RO|RS|RU|SA|SE|SG|SK|TH|TR|TW|UA"
                        "|US|VN|ZA)$": {
                            "type": "integer"}
                    },
                    "additionalProperties": False
                }
            },
            # "required": ["pn", "available_in", "not_available_in"]
        },
        "i18n": {
            "type": "object",
            "patternProperties": {
                "^(en|en-gb|ar|bg|ca|cs|da|de|el|es|et|fi|fr|hi|hr|hu|id|it|ja|ko|lt|lv|ms|nl|no|pl|pt|ro|ru|sk|sr|sv"
                "|th|tr|uk|vi|zh|zh-cn|zh-tw)$": {
                    "type": "object",
                    "properties": {
                        "description": {
                            "type": "string",
                        },
                        "screenshots": {
                            "type": "array",
                            "items": {
                                "type": "string",
                                "format": "uri"
                            }
                        },
                        "what_is_new": {
                            "type": "string"
                        },
                        "title": {
                            "type": "string",
                            "minLength": 1
                        }
                    },
                    # "required": ["description", "screenshots", "what_is_new", "title"]
                }
            },
            "additionalProperties": False

        },
        "content_descriptors": {
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "what_is_new": {
            "type": "string"
        },
        "number_ratings": {
            "type": "integer"
        },
        "similar": {
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "i18n_lang": {
            "type": "array",
            "items": {
                "type": "string"
            }
        }
    },
    "required": [
        "package_name",
        # "cat_key",
        # "cat_keys",
        # "age_approved_by_teachers",
        # "screenshots",
        # "interactive_elements",
        # "sdks",
        # "permissions",
        # "app_availability",
        # "i18n",
        # "content_descriptors",
        # "what_is_new",
        # "number_ratings",
        # "similar",
        # "i18n_lang",
        # "rating",
        # "stores",
        # "badges",
        # "developer",
        # "price_currency",
        # "iap_max",
        # "icon_72",
        # "title",
        # "privacy_policy",
        # "removed_timestamp",
        # "category",
        # "version_code",
        # "version",
        # "size",
        # "email",
        # "physical_address",
        # "cat_int",
        # "created",
        # "market_update",
        # "market_url",
        # "downloads",
        # "from_developer",
        # "iap",
        # "website",
        # "promo_video",
        # "screenshots_count",
        # "market_status",
        # "price_numeric",
        # "short_desc",
        # "downloads_max",
        # "contains_ads",
        # "description",
        # "price",
        # "downloads_min",
        # "promo_video_image",
        # "icon",
        # "lang",
        # "ratings_5",
        # "iap_min",
        # "content_rating",
        # "ratings_4",
        # "cat_type",
        # "ratings_2",
        # "ratings_3",
        # "ratings_1"
    ]

}
