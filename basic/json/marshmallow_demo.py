from datetime import date
from pprint import pprint

from marshmallow import Schema, fields, ValidationError

class ArtistSchema(Schema):
    """Artist Schema"""
    name = fields.Str()

class AlbumSchema(Schema):
    """Album Schema"""
    title = fields.Str()
    release_date = fields.Date()
    artist = fields.Nested(ArtistSchema())

bowie = dict(name="David Bowie")
album = dict(artist=bowie, title="Hunky Dory", release_date=date(1971, 12, 17))

# dump: 正常序列化（对象类型 -> dict）
schema = AlbumSchema()
result = schema.dump(album)
pprint(result, indent=2)
# { 'artist': {'name': 'David Bowie'},
#   'release_date': '1971-12-17',
#   'title': 'Hunky Dory'}

# dump: 序列化 多个对象
artist1 = dict(name="Mick")
artist2 = dict(name="Keith")
artists = [artist1, artist2]
schema = ArtistSchema(many=True)
result = schema.dump(artists)  # OR UserSchema().dump(users, many=True)
pprint(result)
## [{'name': 'Mick'}, {'name': 'Keith'}]

# load: 校验（json -> 对象类型）
album_wrong_type = {"artist": "bowie", "title": "smiecj", "release_date": "2022-03-14"}
try:
    # wrong_result = schema.dump(album_wrong_type)
    wrong_result = AlbumSchema().load(album_wrong_type)
    pprint(wrong_result, indent=2)
except ValidationError as err:
    pprint(err.messages)
    pprint(err.valid_data)
    ## {'artist': {'_schema': ['Invalid input type.']}}
    ## {'release_date': datetime.date(2022, 3, 14), 'title': 'smiecj'}

# load: 校验数组（多个对象）
# load: 添加校验规则

from marshmallow import validate

class UserSchema(Schema):
    name = fields.Str(validate=validate.Length(min=1))
    permission = fields.Str(validate=validate.OneOf(["read", "write", "admin"]))
    age = fields.Int(validate=validate.Range(min=18, max=40))

