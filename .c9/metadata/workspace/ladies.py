{"filter":false,"title":"ladies.py","tooltip":"/ladies.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":11,"column":10},"end":{"row":11,"column":11},"action":"insert","lines":["m"],"id":258}],[{"start":{"row":11,"column":10},"end":{"row":11,"column":11},"action":"remove","lines":["m"],"id":259},{"start":{"row":11,"column":10},"end":{"row":11,"column":15},"action":"insert","lines":["map()"]}],[{"start":{"row":11,"column":13},"end":{"row":11,"column":15},"action":"remove","lines":["()"],"id":260}],[{"start":{"row":11,"column":12},"end":{"row":11,"column":13},"action":"remove","lines":["p"],"id":261}],[{"start":{"row":11,"column":11},"end":{"row":11,"column":12},"action":"remove","lines":["a"],"id":262}],[{"start":{"row":11,"column":11},"end":{"row":11,"column":12},"action":"insert","lines":["e"],"id":263}],[{"start":{"row":11,"column":12},"end":{"row":11,"column":13},"action":"insert","lines":["d"],"id":264}],[{"start":{"row":11,"column":13},"end":{"row":11,"column":14},"action":"insert","lines":["i"],"id":265}],[{"start":{"row":11,"column":14},"end":{"row":11,"column":15},"action":"insert","lines":["a"],"id":266}],[{"start":{"row":11,"column":15},"end":{"row":11,"column":16},"action":"insert","lines":["."],"id":267}],[{"start":{"row":11,"column":16},"end":{"row":11,"column":17},"action":"insert","lines":["c"],"id":268}],[{"start":{"row":11,"column":17},"end":{"row":11,"column":18},"action":"insert","lines":["a"],"id":269}],[{"start":{"row":11,"column":18},"end":{"row":11,"column":19},"action":"insert","lines":["p"],"id":270}],[{"start":{"row":11,"column":19},"end":{"row":11,"column":20},"action":"insert","lines":["t"],"id":271}],[{"start":{"row":11,"column":20},"end":{"row":11,"column":21},"action":"insert","lines":["i"],"id":272},{"start":{"row":11,"column":21},"end":{"row":11,"column":22},"action":"insert","lines":["o"]}],[{"start":{"row":11,"column":22},"end":{"row":11,"column":23},"action":"insert","lines":["n"],"id":273}],[{"start":{"row":10,"column":0},"end":{"row":10,"column":1},"action":"insert","lines":["№"],"id":274}],[{"start":{"row":10,"column":0},"end":{"row":10,"column":1},"action":"remove","lines":["№"],"id":275}],[{"start":{"row":10,"column":0},"end":{"row":10,"column":1},"action":"insert","lines":["#"],"id":276}],[{"start":{"row":11,"column":1},"end":{"row":11,"column":2},"action":"insert","lines":["#"],"id":277}],[{"start":{"row":11,"column":24},"end":{"row":12,"column":0},"action":"insert","lines":["",""],"id":278},{"start":{"row":12,"column":0},"end":{"row":12,"column":1},"action":"insert","lines":[" "]}],[{"start":{"row":12,"column":1},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":279},{"start":{"row":13,"column":0},"end":{"row":13,"column":1},"action":"insert","lines":[" "]}],[{"start":{"row":13,"column":1},"end":{"row":23,"column":0},"action":"insert","lines":["app = Flask(__name__)","","@app.route(\"/\")","def hello():","    recent_media = get_instagram_recent_media()","    context = {","            \"media\": recent_media","    }","    return render_template(\"template.html\", **context)","",""],"id":280}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":1},"action":"remove","lines":[" "],"id":281}],[{"start":{"row":23,"column":0},"end":{"row":25,"column":0},"action":"insert","lines":["if __name__ == \"__main__\":","   app.run(port=8080, host=\"0.0.0.0\", debug=True)",""],"id":282}],[{"start":{"row":22,"column":0},"end":{"row":23,"column":0},"action":"insert","lines":["",""],"id":283}],[{"start":{"row":0,"column":41},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":284}],[{"start":{"row":1,"column":0},"end":{"row":1,"column":40},"action":"insert","lines":["from flask import Flask, render_template"],"id":285}],[{"start":{"row":22,"column":35},"end":{"row":22,"column":36},"action":"remove","lines":["e"],"id":286}],[{"start":{"row":22,"column":34},"end":{"row":22,"column":35},"action":"remove","lines":["t"],"id":287}],[{"start":{"row":22,"column":33},"end":{"row":22,"column":34},"action":"remove","lines":["a"],"id":288}],[{"start":{"row":22,"column":32},"end":{"row":22,"column":33},"action":"remove","lines":["l"],"id":289}],[{"start":{"row":22,"column":31},"end":{"row":22,"column":32},"action":"remove","lines":["p"],"id":290}],[{"start":{"row":22,"column":30},"end":{"row":22,"column":31},"action":"remove","lines":["m"],"id":291}],[{"start":{"row":22,"column":29},"end":{"row":22,"column":30},"action":"remove","lines":["e"],"id":292}],[{"start":{"row":22,"column":28},"end":{"row":22,"column":29},"action":"remove","lines":["t"],"id":293}],[{"start":{"row":22,"column":28},"end":{"row":22,"column":29},"action":"insert","lines":["u"],"id":294}],[{"start":{"row":22,"column":29},"end":{"row":22,"column":30},"action":"insert","lines":["m"],"id":295}],[{"start":{"row":22,"column":30},"end":{"row":22,"column":31},"action":"insert","lines":["a"],"id":296}],[{"start":{"row":22,"column":31},"end":{"row":22,"column":32},"action":"insert","lines":["g"],"id":297}],[{"start":{"row":22,"column":32},"end":{"row":22,"column":33},"action":"insert","lines":["e"],"id":298}],[{"start":{"row":22,"column":32},"end":{"row":22,"column":33},"action":"remove","lines":["e"],"id":299}],[{"start":{"row":22,"column":31},"end":{"row":22,"column":32},"action":"remove","lines":["g"],"id":300}],[{"start":{"row":22,"column":30},"end":{"row":22,"column":31},"action":"remove","lines":["a"],"id":301}],[{"start":{"row":22,"column":29},"end":{"row":22,"column":30},"action":"remove","lines":["m"],"id":302}],[{"start":{"row":22,"column":28},"end":{"row":22,"column":29},"action":"remove","lines":["u"],"id":303}],[{"start":{"row":22,"column":28},"end":{"row":22,"column":29},"action":"insert","lines":["i"],"id":304}],[{"start":{"row":22,"column":29},"end":{"row":22,"column":30},"action":"insert","lines":["m"],"id":305}],[{"start":{"row":22,"column":30},"end":{"row":22,"column":31},"action":"insert","lines":["a"],"id":306}],[{"start":{"row":22,"column":31},"end":{"row":22,"column":32},"action":"insert","lines":["g"],"id":307}],[{"start":{"row":22,"column":32},"end":{"row":22,"column":33},"action":"insert","lines":["e"],"id":308}],[{"start":{"row":24,"column":0},"end":{"row":25,"column":0},"action":"insert","lines":["",""],"id":309}],[{"start":{"row":24,"column":0},"end":{"row":30,"column":0},"action":"insert","lines":["from clarifai.client import ClarifaiApi","def image_tags_recognition(url):","    clarifai_api = ClarifaiApi(app_id=CLARIFY_ID, app_secret=CLARIFY_SECRET)","    response = clarifai_api.tag_image_urls(url)","    if response['status_code'] == 'OK':","        return response['results'][0]['result']['tag']['classes']",""],"id":310}],[{"start":{"row":24,"column":0},"end":{"row":24,"column":39},"action":"remove","lines":["from clarifai.client import ClarifaiApi"],"id":311}],[{"start":{"row":1,"column":40},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":312}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":39},"action":"insert","lines":["from clarifai.client import ClarifaiApi"],"id":313}],[{"start":{"row":31,"column":0},"end":{"row":32,"column":0},"action":"insert","lines":["",""],"id":314}],[{"start":{"row":32,"column":0},"end":{"row":35,"column":0},"action":"insert","lines":["app.jinja_env.globals.update(","    tags_recognition=image_tags_recognition",")",""],"id":315}],[{"start":{"row":34,"column":1},"end":{"row":35,"column":0},"action":"remove","lines":["",""],"id":316}],[{"start":{"row":24,"column":0},"end":{"row":25,"column":0},"action":"insert","lines":["",""],"id":317}],[{"start":{"row":25,"column":0},"end":{"row":26,"column":0},"action":"insert","lines":["",""],"id":318}],[{"start":{"row":25,"column":0},"end":{"row":27,"column":0},"action":"insert","lines":["CLARIFY_ID = \"9NgaOKCxeeI--3Ao90__LmuV8yJIQto670v8JNQA\"",">>> CLARIFY_SECRET = \"47f9xAyi35-ZrJeU3NiwrqW0iles-9BZEGMDckWh\"",""],"id":319}],[{"start":{"row":26,"column":3},"end":{"row":26,"column":4},"action":"remove","lines":[" "],"id":320}],[{"start":{"row":26,"column":2},"end":{"row":26,"column":3},"action":"remove","lines":[">"],"id":321}],[{"start":{"row":26,"column":1},"end":{"row":26,"column":2},"action":"remove","lines":[">"],"id":322}],[{"start":{"row":26,"column":0},"end":{"row":26,"column":1},"action":"remove","lines":[">"],"id":323}],[{"start":{"row":27,"column":0},"end":{"row":28,"column":0},"action":"remove","lines":["",""],"id":327}],[{"start":{"row":26,"column":59},"end":{"row":27,"column":0},"action":"remove","lines":["",""],"id":328}],[{"start":{"row":25,"column":14},"end":{"row":25,"column":54},"action":"remove","lines":["9NgaOKCxeeI--3Ao90__LmuV8yJIQto670v8JNQA"],"id":329},{"start":{"row":25,"column":14},"end":{"row":25,"column":54},"action":"insert","lines":["hF5aLr77Qdx7Pz6Y_7oAme5ntQO15_esUT4DL4bo"]}],[{"start":{"row":26,"column":18},"end":{"row":26,"column":58},"action":"remove","lines":["47f9xAyi35-ZrJeU3NiwrqW0iles-9BZEGMDckWh"],"id":330},{"start":{"row":26,"column":18},"end":{"row":26,"column":58},"action":"insert","lines":["pWO29ycwWDPv-QWwG-gJRYStVeluBN2LNmsGnYbV"]}],[{"start":{"row":1,"column":40},"end":{"row":1,"column":41},"action":"insert","lines":["б"],"id":331}],[{"start":{"row":1,"column":41},"end":{"row":1,"column":42},"action":"insert","lines":[" "],"id":332}],[{"start":{"row":1,"column":42},"end":{"row":1,"column":43},"action":"insert","lines":["к"],"id":333}],[{"start":{"row":1,"column":43},"end":{"row":1,"column":44},"action":"insert","lines":["у"],"id":334}],[{"start":{"row":1,"column":44},"end":{"row":1,"column":45},"action":"insert","lines":["й"],"id":335}],[{"start":{"row":1,"column":45},"end":{"row":1,"column":46},"action":"insert","lines":["г"],"id":336}],[{"start":{"row":1,"column":46},"end":{"row":1,"column":47},"action":"insert","lines":["у"],"id":337}],[{"start":{"row":1,"column":47},"end":{"row":1,"column":48},"action":"insert","lines":["ы"],"id":338}],[{"start":{"row":1,"column":48},"end":{"row":1,"column":49},"action":"insert","lines":["е"],"id":339}],[{"start":{"row":1,"column":48},"end":{"row":1,"column":49},"action":"remove","lines":["е"],"id":340}],[{"start":{"row":1,"column":47},"end":{"row":1,"column":48},"action":"remove","lines":["ы"],"id":341}],[{"start":{"row":1,"column":46},"end":{"row":1,"column":47},"action":"remove","lines":["у"],"id":342}],[{"start":{"row":1,"column":45},"end":{"row":1,"column":46},"action":"remove","lines":["г"],"id":343}],[{"start":{"row":1,"column":44},"end":{"row":1,"column":45},"action":"remove","lines":["й"],"id":344}],[{"start":{"row":1,"column":43},"end":{"row":1,"column":44},"action":"remove","lines":["у"],"id":345}],[{"start":{"row":1,"column":42},"end":{"row":1,"column":43},"action":"remove","lines":["к"],"id":346}],[{"start":{"row":1,"column":41},"end":{"row":1,"column":42},"action":"remove","lines":[" "],"id":347}],[{"start":{"row":1,"column":40},"end":{"row":1,"column":41},"action":"remove","lines":["б"],"id":348}],[{"start":{"row":1,"column":40},"end":{"row":1,"column":41},"action":"insert","lines":[","],"id":349}],[{"start":{"row":1,"column":41},"end":{"row":1,"column":42},"action":"insert","lines":[" "],"id":350}],[{"start":{"row":1,"column":42},"end":{"row":1,"column":43},"action":"insert","lines":["r"],"id":351}],[{"start":{"row":1,"column":43},"end":{"row":1,"column":44},"action":"insert","lines":["e"],"id":352}],[{"start":{"row":1,"column":44},"end":{"row":1,"column":45},"action":"insert","lines":["q"],"id":353}],[{"start":{"row":1,"column":45},"end":{"row":1,"column":46},"action":"insert","lines":["u"],"id":354}],[{"start":{"row":1,"column":46},"end":{"row":1,"column":47},"action":"insert","lines":["e"],"id":355}],[{"start":{"row":1,"column":47},"end":{"row":1,"column":48},"action":"insert","lines":["s"],"id":356}],[{"start":{"row":1,"column":48},"end":{"row":1,"column":49},"action":"insert","lines":["t"],"id":357}],[{"start":{"row":24,"column":0},"end":{"row":25,"column":0},"action":"insert","lines":["",""],"id":358}],[{"start":{"row":25,"column":0},"end":{"row":26,"column":0},"action":"insert","lines":["",""],"id":359}],[{"start":{"row":25,"column":0},"end":{"row":31,"column":0},"action":"insert","lines":["@app.route(\"/tags/\")","def tags():","    url = request.args.get('url')","    tags = image_tags_recognition(url)","    return \", \".join(tags)","",""],"id":360}],[{"start":{"row":30,"column":0},"end":{"row":31,"column":0},"action":"remove","lines":["",""],"id":361}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":30,"column":0},"end":{"row":30,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1461683938000,"hash":"a86489e9db20c4116db08f0b4602c7bff0707fab"}