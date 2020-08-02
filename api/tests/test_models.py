from django.test import TestCase
from api.models import  Course, Contact, Branch, Category


class CourseModelTest(TestCase):
    """Tests Course model"""
    @classmethod
    def setUp(cls):
        category = Category.objects.create(
            name = 'akdssd',
            imgpath = 'sdfsdf'
        )
        course = Course.objects.create(
            name = 'sdfsdfds',
            description = 'sdfsf',
            logo = 'sdfsdfs',
            category = category
        )
    def test_category_name_label(self):
        category_2 = Category.objects.get(id=1)
        field_label = category_2._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_category_imgpath_label(self):
        category_2 = Category.objects.get(id=1)
        field_label = category_2._meta.get_field('imgpath').verbose_name
        self.assertEquals(field_label, 'imgpath')  
    
    def test_course_name_label(self):
        course_1 = Course.objects.get(id=1)
        field_label = course_1._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')
      
    def test_course_description_label(self):
        course_1 = Course.objects.get(id=1)
        field_label = course_1._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

    def test_logo_description_label(self):
        course_1 = Course.objects.get(id=1)
        field_label = course_1._meta.get_field('logo').verbose_name
        self.assertEquals(field_label, 'logo')


class BranchModelTest(TestCase):
    """Tests Branch model"""
    @classmethod
    def setUp(cls):
        category = Category.objects.create(
            name = 'akdssd',
            imgpath = 'sdfsdf'
        )
        course = Course.objects.create(
            name = 'sdfsdfds',
            description = 'sdfsf',
            logo = 'sdfsdfs',
            category = category
        )
        Branch.objects.create(
            latitude ='sdfsfsfsf',
            longitude ='dsfsfsfss',
            address ='sdfsdfsfs',
            branches = course
        )
    def test_branch_latitude_label(self):
        branch_1 = Branch.objects.get(id=1)
        field_label = branch_1._meta.get_field('latitude').verbose_name
        self.assertEquals(field_label, 'latitude')
    
    def test_branch_longitude_label(self):
        branch_1 = Branch.objects.get(id=1)
        field_label = branch_1._meta.get_field('longitude').verbose_name
        self.assertEquals(field_label, 'longitude')

    def test_branch_address_label(self):
        branch_1 = Branch.objects.get(id=1)
        field_label = branch_1._meta.get_field('address').verbose_name
        self.assertEquals(field_label, 'address')


class ContactModelTest(TestCase):
    """Test Contact Model"""
    def setUp(cls):
        category = Category.objects.create(
            name = 'akdssd',
            imgpath = 'sdfsdf'
        )
        course = Course.objects.create(
            name = 'sdfsdfds',
            description = 'sdfsf',
            logo = 'sdfsdfs',
            category = category
        )
        Contact.objects.create(
            type = 'Facebook',
            contacts = course,
            value = 'dsfsdfs'
        )

    def test_type_contacts_label(self):
        contact = Contact.objects.get(id=1)
        field_label = contact._meta.get_field('type').verbose_name
        self.assertEquals(field_label, 'type')

    def test_value_contacts_label(self):
        contact = Contact.objects.get(id=1)
        field_label = contact._meta.get_field('value').verbose_name
        self.assertEquals(field_label, 'value')




