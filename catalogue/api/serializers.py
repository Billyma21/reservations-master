from rest_framework import serializers
from catalogue.models import *
from catalogue.models.representationUser import RepresentationUser
from catalogue.models.representation import Representation
from catalogue.models.artistTypeShow import ArtistTypeShow
from catalogue.models.roleUser import RoleUser


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'firstname', 'lastname']


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['id', 'type']


class ArtistTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistType
        fields = ['id', 'artist_id', 'type_id']


class ArtistTypeShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistTypeShow
        fields = ['id', 'artiste_type_id', 'show_id']


class ShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Show
        fields = ['id', 'slug', 'title', 'poster_url', 'location_id', 'bookable', 'price']


class RepresentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Representation
        fields = ['id', 'show_id', 'when', 'location_id']


class RepresentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Representation
        fields = ['id', 'show_id', 'when', 'location_id']

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'slug', 'designation', 'address', 'locality_id', 'website', 'phone']

class LocalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Locality
        fields = ['id', 'postal_code', 'locality']

class RepresentationUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepresentationUser
        fields = ['id', 'representation_id', 'user_id', 'places']

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'login', 'password', 'firstname', 'lastname', 'email', 'langue']

class RoleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleUser
        fields = ['id', 'role_id', 'user_id']

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'role']