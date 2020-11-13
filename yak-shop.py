from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
import Yak
from ReadHerd import Herd

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
api = Api(app)

Ordertime = 0  #  Needed for story 3, to remember the day of the previous order
OldStock = {"milk": 0, "skins": 0}  # To remember the stock status after the last order
parser = reqparse.RequestParser()

class Herdstatus(Resource):
    def get(self, T):
        T = int(T)
        [milk, wol, age, age_shave] = Yak.Stockstatus(Herd, T)
        N = len(age)
        data = {"herd": []}
        for i in range(N):
            data["herd"].append(
                {"name": Herd[i].name, "age": round(age[i], 2), "age-last-shaved": round(age_shave[i], 2)})
        return (jsonify(data))


class Order(Resource):  # story 3 combined with story 2, the status at story 2 changes when there are orders.

    def get (self):  # get stock status
        global Ordertime
        T0 = Ordertime
        parser.add_argument("day of status")
        args = parser.parse_args()
        T = int(args["day of status"])
        milk2, wol2, _, _ = Yak.Stockstatus(Herd, T)
        milk1, wol1, _, _ = Yak.Stockstatus(Herd, T0)
        milk = milk2 - milk1  # netto production with respect to the last order
        wol = wol2 - wol1
        NewStock = {"milk": round(OldStock["milk"] + float(milk),2), "skins": OldStock["skins"] + int(wol)}
        return(jsonify(NewStock))

    def post (self):  # post order
        parser.add_argument("customer")
        parser.add_argument("milk")
        parser.add_argument("skins")
        parser.add_argument("day of order")
        args = parser.parse_args()
        T = int(args["day of order"])
        global Ordertime
        T0 = Ordertime
        milk2, wol2 ,_ ,_ = Yak.Stockstatus(Herd, T)
        milk1, wol1 ,_,_ = Yak.Stockstatus(Herd,T0)
        milk = milk2 - milk1  #netto production with respect to the last order
        wol = wol2 - wol1
        Ordertime = T
        NewStock = {"milk": OldStock["milk"] + float(milk), "skins": OldStock["skins"] + int(wol)}
        args["milk"] = float(args["milk"]); args["skins"] = int(args["skins"])
        if NewStock["milk"] >= args["milk"] and NewStock["skins"] >= args["skins"]:
            OldStock["milk"] = NewStock["milk"] - args["milk"]
            OldStock["skins"] = NewStock["skins"] - args["skins"]
            return 201
        if NewStock["milk"] >= args["milk"] or NewStock["skins"] >= args["skins"]:
            if NewStock["milk"] >= args["milk"]:
                OldStock["milk"] = NewStock["milk"] - args["milk"]
                OldStock["skins"] = NewStock["skins"]
                return({"milk:": args["milk"]}), 206
            else:
                OldStock["milk"] = NewStock["milk"]
                OldStock["skins"] = NewStock["skins"] - args["skins"]
                return ({"skins:": args["skins"]}), 206
        else:
            OldStock["milk"] = NewStock["milk"]
            OldStock["skins"] = NewStock["skins"]
            return 404




api.add_resource(Herdstatus, '/yak-shop/herd/<T>')
api.add_resource(Order, '/yak-shop/order')
if __name__ == "__main__":
    app.run(debug=True)
