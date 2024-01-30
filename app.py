import dash
from flask import Response 

# to access the generate function from the streaming_oak_d_lite file
from streaming_oak_d_lite import generate 

# And the simple_layout function from the layout file
from layout import simple_layout

# Create the Dash app
app = dash.Dash(__name__)
app.layout = simple_layout()

# Create the video feed route
@app.server.route("/video_feed") #
def video_feed():
    return Response(generate(), mimetype = "multipart/x-mixed-replace; boundary=frame")

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)