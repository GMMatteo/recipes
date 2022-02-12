from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash

db = 'recipes'

class Recipe:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.time = data['time']
        self.instruction = data['instruction']
        self.date_made = data['date_made']
        self.user_id = data['user_id']
        self.cook = data['cook']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_recipe(cls,data):
        query = "INSERT INTO recipes (name, description, time, instruction, date_made, user_id) VALUES (%(name)s, %(description)s, %(time)s, %(instruction)s, %(date_made)s, %(user_id)s);"
        recipe = connectToMySQL(db).query_db(query,data)
        return recipe

    @classmethod
    def edit_recipe(cls,data):
        query = "UPDATE recipes SET name=%(name)s, description=%(description)s, time=%(time)s, instruction=%(instruction)s, date_made=%(date_made)s, user_id=%(user_id)s WHERE ID = %(id)s;"
        recipe = connectToMySQL(db).query_db(query,data)
        return recipe

    @classmethod
    def get_recipes(cls,data):
        query = "SELECT CONCAT(users.first_name,' ', users.last_name) AS cook, recipes.* FROM recipes JOIN users ON users.id = recipes.user_id;"
        recipes = connectToMySQL(db).query_db(query,data)
        recipe =[]
        for r in recipes:
            recipe.append(cls(r))
        return recipe

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT CONCAT(users.first_name,' ', users.last_name) AS cook, recipes.* FROM recipes LEFT JOIN users ON users.id = recipes.user_id WHERE recipes.id = %(id)s;"
        results = connectToMySQL(db).query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @staticmethod
    def valid_recipe(recipe):
        is_valid=True
        if len(recipe['name']) < 3:
            flash("Name is too short")
            is_valid = False
        if len(recipe['description']) < 3:
            flash("Description is too short")
            is_valid = False
        if len(recipe['instruction']) < 3:
            flash("Instructions are too short")
            is_valid = False
        if len(recipe['date_made']) < 3:
            flash("Date is either invalid or missing")
            is_valid = False
        return is_valid

    @classmethod
    def delete_recipe(cls,data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(db).query_db(query,data)