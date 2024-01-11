from flask import Flask, render_template, request, jsonify
import PyATEMMax

app = Flask(__name__)
switcher = PyATEMMax.ATEMMax()
addr = "192.168.11.102"

@app.route('/')
def index():
    macros = ["発表PC", "発表Cam", "質問Cam", "PP", "発表時", "質問時", "発表者Only", "蓋絵", "Macro I", "Macro J",]
            #   "Macro K", "Macro L", "Macro M", "Macro N", "Macro O", "Macro P", "Macro Q", "Macro R", "Macro S", "Macro T"]

    stills = ["Still 1", "Still 2", "Still 3", "Still 4", "Still 5", "Still 6", "Still 7", "Still 8", "Still 9", "Still 10",
              "Still 11", "Still 12", "Still 13", "Still 14", "Still 15", "Still 16", "Still 17", "Still 18", "Still 19", "蓋絵"]

    return render_template('index.html', macros=macros, stills=stills)

@app.route('/run_macro', methods=['POST'])
def run_macro():
    macro_id = request.form.get('macro_id')
    switcher.setMacroAction(int(macro_id), "runMacro")
    return jsonify({'status': 'success'})

@app.route('/switch_still', methods=['POST'])
def switch_still():
    still_id = request.form.get('still_id')
    switcher.setMediaPlayerSourceStillIndex(0, int(still_id))
    return jsonify({'status': 'success'})

@app.route('/status', methods=['GET'])
def get_status():
    server_status = "Connected"
    if switcher.connected:
        atem_status = "Connected"
    else:
        atem_status = "Disconnected"
    return jsonify({'server_status': server_status, 'atem_status': atem_status})

if __name__ == '__main__':
    switcher.connect(addr)
    switcher.waitForConnection(infinite=False)
    app.run(debug=False, host='0.0.0.0', port=8080)
