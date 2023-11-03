from flask import Flask, jsonify, request, make_response
import flask_cors

# create app
app = Flask(__name__, static_folder='static')
cors = flask_cors.CORS(app, resources={r"/api/*": {"origins": "*"}})
MY_JSON = {
        "scraped_at": "2023-10-10 21:22:59.943714 +00:00",
        "post_text": "Possibly recent (but date unverified) video...",
        "posted_at": "2023-01-05T19:32:15-01:00",
        "tweet_url": "https://social-media-website.com/Dmojavensis/post/1611083174192480257",
        "media_urls":
        [
            "https://video.social-media-website.com/1611081502133227520/pu/vid/720x1288/VCFtz2M8Ehfg4N8C.mp4"
        ],
        "view_count": "1.5k",
        "original_post":
        {
            "post_text": "@golub The video is filmed from Magnolia Park mall...",
            "posted_at": "2023-01-05T19:17:03-01:00",
            "tweet_url": "https://social-media-website.com/Dmojavensis/post/1611079349230526464",
            "media_urls":
            [
                "https://image.social-media-website.com/media/FluzVfLaUAABwe1.jpg",
                "https://image.social-media-website.com/media/Flu0Hf9aUAA3PxW.jpg"
            ],
            "view_count": "1k",
            "profile_metadata":
            {
                "description": "Fictional character - explores the world...",
                "external_id": "Dmojavensis",
                "display_name": "D. mojavensis 🇺🇲 🇺🇦",
                "external_url": "https://social-media-website.com/Dmojavensis",
                "friends_count": "409",
                "statuses_count": "13.8k",
                "followers_count": "956"
            },
            "total_repost_count": "1",
        },
        "favorite_count": "3",
        "profile_metadata":
        {
            "description": "Fictional character - explores the world...",
            "external_id": "Dmojavensis",
            "display_name": "D. mojavensis 🇺🇲 🇺🇦",
            "external_url": "https://social-media-website.com/Dmojavensis",
            "friends_count": "409",
            "statuses_count": "13.8k",
            "followers_count": "956"
        },
        "total_repost_count": "3",
    }

@app.route('/social/', methods=['POST', 'OPTIONS'])
@flask_cors.cross_origin()
def square():
    if request.method == "OPTIONS":  # CORS preflight
        return build_cors_prelight_response()

    response = {}
    response['results'] = MY_JSON

    return jsonify(response)


@app.route('/square/', methods=['POST', 'OPTIONS'])
@flask_cors.cross_origin()
def square():
    if request.method == "OPTIONS":  # CORS preflight
        return build_cors_prelight_response()

    # get data
    data = request.get_json()[0]
    num_list = data.values()

    response = {}
    response['results'] = []

    for n in num_list:
        square = n ** 2
        response['results'].append(square)

    return jsonify(response)

# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>My API Server</h1>"


def build_cors_prelight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    return response


if __name__ == '__main__':
    app.run(debug=True)
