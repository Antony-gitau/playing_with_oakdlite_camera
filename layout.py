from dash import html

def simple_layout():
    return html.Div([
            html.Iframe(src="/video_feed", width="1200", height="800", id="video-stream"),
            ], style={'width': '100%', 'display': 'flex', 'justify-content': 'center', 'align-items': 'center'}
            )

    # can add more components here to make the web app more interactive and interesting
