import pytest

from categories.models import CategoryModel


@pytest.mark.django_db
class TestCategoryModel:
    @pytest.fixture(autouse=True)
    def initial(self, client):
        CategoryModel.objects.create(name="Salary", category_type="I")
        CategoryModel.objects.create(name="Grocery", category_type="E")
        CategoryModel.objects.create(name="Washing", category_type="E")

    def test_models_are_created(self):
        assert CategoryModel.objects.count() == 3

    def test_category_type(self):
        category_model = CategoryModel.objects.filter(name="Salary").first()
        assert category_model.name == "Salary"
        assert category_model.category_type == "I"

    def test_get_category_type_fullname(self):
        category_model = CategoryModel.objects.filter(name="Salary").first()
        category_type_name = category_model.category_type

        assert category_type_name == "I"
        assert category_model.get_category_type_fullname(category_type_name) == "Income"

    def test_get_category_type_fullname_raises_error(self):
        category_model = CategoryModel.objects.filter(name="Salary").first()

        with pytest.raises(ValueError):
            category_model.get_category_type_fullname("Z")
