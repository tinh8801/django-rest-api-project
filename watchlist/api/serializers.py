from rest_framework import serializers
from watchlist.models import WatchList, StreamPlatform, Review

class ReviewSerializer(serializers.ModelSerializer):
    review_user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Review
        #fields='__all__'
        exclude =('watchlist',)

class WatchListSerializer(serializers.ModelSerializer):
    #review=ReviewSerializer(many=True, read_only=True)
    #len_name=serializers.SerializerMethodField()#tao custom field (field khong co san trong model)
    platform=serializers.CharField(source='platform.name')
    class Meta:
        model=WatchList
        fields='__all__'
        
        
class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist=WatchListSerializer(many=True, read_only=True)
    #watchlist=serializers.StringRelatedField(many=True, read_only=True)
    #watchlist=serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    #watchlist=serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='movie-details')
    class Meta:
        model=StreamPlatform
        fields='__all__'

        #fields=['id', 'name', 'description']
        #exclude=['active']
    
    '''def get_len_name(self, obj):
        return len(obj.description)
    
    def validate(self, data): #object level validation
        if data['title']==data['storyline']:
            raise serializers.ValidationError({'error': 'name and description must be different'})
        else:
            return data
        
    def validate_name(self, value):#field level validation ten ham bat dau voi validate_tenfield can validate
        if len(value)<2:
            raise serializers.ValidationError({'error': 'name must be at least 2 characters'})
        else:
            return value

def check_length(value):
    if len(value)<2:
        raise serializers.ValidationError({'description': 'description must be at least 2 characters'})
    
class MovieSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    description=serializers.CharField(validators=[check_length])#validators
    active=serializers.BooleanField()
    
    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
    
    def update(self, instance, validated_data):#instance chua du lieu cu, validated_data chuwa du lieu moi
        instance.name=validated_data.get('name', instance.name)
        instance.description=validated_data.get('description', instance.description)
        instance.active=validated_data.get('active', instance.active)
        instance.save()
        return instance
    
    def validate(self, data): #object level validation
        if data['name']==data['description']:
            raise serializers.ValidationError({'name': 'name and description must be different'})
        else:
            return data
        
    def validate_name(self, value):#field level validation ten ham bat dau voi validate_tenfield can validate
        if len(value)<2:
            raise serializers.ValidationError({'name': 'name must be at least 2 characters'})
        else:
            return value'''