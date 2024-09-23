from .models import Recipe  # Connect parameters from Recipe model
from io import BytesIO
import base64
import matplotlib.pyplot as plt


def get_recipe_from_id(recipe_id):
    """
    Retrieve the recipe name based on the recipe ID.
    """
    try:
        recipe = Recipe.objects.get(id=recipe_id)
        return recipe.name
    except Recipe.DoesNotExist:
        return "Unknown Recipe"


def get_graph():
    """
    Create a graph image and return it as a base64 encoded string.
    """
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png).decode("utf-8")
    buffer.close()
    return graph


def get_chart(chart_type, data, **kwargs):
    """
    Generate a chart based on the chart type and data provided.
    """
    plt.switch_backend("AGG")
    fig = plt.figure(figsize=(6, 3))

    if chart_type == "#1":
        plt.bar(data["name"], data["cooking_time"])
        plt.xticks(rotation=45, ha="right")
        plt.ylabel("Cooking Time (minutes)")
        plt.title("Cooking Time by Recipe")

    elif chart_type == "#2":
        labels = kwargs.get("labels")
        plt.pie(data["cooking_time"], labels=labels)
        plt.title("Cooking Time Distribution by Recipe")

    elif chart_type == "#3":
        plt.plot(data["name"], data["cooking_time"])
        plt.xticks(rotation=45, ha="right")
        plt.ylabel("Cooking Time (minutes)")
        plt.title("Cooking Time by Recipe")

    else:
        print("Unknown chart type")

    plt.tight_layout()
    return get_graph()
