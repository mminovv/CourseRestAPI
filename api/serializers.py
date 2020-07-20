from rest_framework import serializers
from .models import Course, Contact, Branch, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'imgpath')


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id','type', 'value')


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ('id','latitude', 'longitude', 'address')

class CourseSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True)
    branches = BranchSerializer(many=True)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'category', 'logo', 'contacts', 'branches']

    def create(self, validated_data):
        branches_data = validated_data.pop('branches')
        contacts_data = validated_data.pop('contacts')
        course = Course.objects.create(**validated_data)

        for branch in branches_data:
            branch, created = Branch.objects.get_or_create(address=branch['address'])
            course.branches.add(branch)

        for contact in contacts_data:
            contact, created = Contact.objects.get_or_create(value=contact['value'])
            course.contacts.add(contact)
        return course