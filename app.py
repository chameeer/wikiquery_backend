from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('query')


class Result(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self):
        arg = parser.parse_args()
        query = arg['query']
        return {
            'res1':
                {'href':
                    "https://zh.wikipedia.org/wiki/%E4%B8%AD%E6%96%87%E7%BB%B4%E5%9F%BA%E7%99%BE%E7%A7%91",
                'title': query + '结果1',
                'description': '本文档与关键词话题重合率 85.032033435%'
                },

            'res2':
                {'href':
                     "https://zh.wikipedia.org/wiki/%E4%B8%AD%E6%96%87%E7%BB%B4%E5%9F%BA%E7%99%BE%E7%A7%91",
                 'title': query + '结果2',
                 'description': '本文档与关键词话题重合率 85.032033435%'
                 },

            'res3':
                {'href':
                     "https://zh.wikipedia.org/wiki/%E4%B8%AD%E6%96%87%E7%BB%B4%E5%9F%BA%E7%99%BE%E7%A7%91",
                 'title': query + '结果3',
                 'description': '本文档与关键词话题重合率 85.032033435%'
                 }

        }



api.add_resource(Result, '/result')

if __name__ == "__main__":
    app.run()
