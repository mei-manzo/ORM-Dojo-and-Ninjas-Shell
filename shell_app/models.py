from django.db import models

class Dojos(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc = models.TextField(default = 'old dojo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "Name: {}".format(self.name)
    #this code will return a readable string rather than {object}
    #can reformat for assignment. may need to exit() shell and re-import to see changes

class Ninjas(models.Model):
    dojo = models.ForeignKey(Dojos, related_name="ninjas", on_delete = models.CASCADE, default='0')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "Name: {} {}".format(self.first_name, self.last_name)

    # def __repr__(self):
    #     return "Dojo: {}".format(self.dojo)