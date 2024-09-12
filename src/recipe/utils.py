from .models import Recipe  # Connect parameters from Recipe model
from io import BytesIO
import base64
import matplotlib.pyplot as plt

# Define a function that takes the ID
def get_recipe_from_id(recipe_id):
    # Example implementation
    try:
        recipe = Recipe.objects.get(id=recipe_id)
        return recipe.name
    except Recipe.DoesNotExist:
        return "Unknown Recipe"

def get_graph():
    # Create a BytesIO buffer for the image
    buffer = BytesIO()

    # Create a plot with a BytesIO object as a file-like object. Set format to png
    plt.savefig(buffer, format='png')

    # Set cursor to the beginning of the stream
    buffer.seek(0)

    # Retrieve the content of the file
    image_png = buffer.getvalue()

    # Encode the bytes-like object
    graph = base64.b64encode(image_png)

    # Decode to get the string as output
    graph = graph.decode('utf-8')

    # Free up the memory of buffer
    buffer.close()

    # Return the image/graph
    return graph

# chart_type: user input of type of chart,
# data: pandas dataframe
def get_chart(chart_type, data, **kwargs):
    # Switch plot backend to AGG (Anti-Grain Geometry) - to write to file
    # AGG is preferred solution to write PNG files
    plt.switch_backend('AGG')

    # Specify figure size
    fig = plt.figure(figsize=(6, 3))

    # Select chart_type based on user input from the form
    if chart_type == '#1':
        # Plot bar chart between recipe names on x-axis and cooking_time on y-axis
        plt.bar(data['name'], data['cooking_time'])
        plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels

    elif chart_type == '#2':
        # Generate pie chart based on the cooking_time.
        # The recipe names are sent from the view as labels
        labels = kwargs.get('labels')
        plt.pie(data['cooking_time'], labels=labels)

    elif chart_type == '#3':
        # Plot line chart based on recipe names on x-axis and cooking_time on y-axis
        plt.plot(data['name'], data['cooking_time'])
        plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels
    else:
        print('unknown chart type')

    # Specify layout details
    plt.tight_layout()

    # Render the graph to file
    chart = get_graph()
    return chart