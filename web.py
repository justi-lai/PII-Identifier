from bottle import Bottle, route, run, template, static_file, post, request
import webbrowser
from remover import RemovePII
import sys


def StartWebserver():
    webbrowser.open(
        "http://localhost:1986/",
    )
    app = Bottle()
    run(host="localhost", port=1986)
    exit(0)


@route("/")
def landing():
    return static_file("index.html", "static")


@route("/static/<filename:path>")
def static(filename):
    return static_file(filename, root="static")


@post("/PII")
def processPII():
    data = request.json

    fullText = data["text"]
    re_name = data["FilterName"]
    re_address = data["FilterAddress"]
    re_dob = data["FilterDOB"]
    re_ssn = data["FilterSSN"]
    re_phone = data["FilterPhone"]
    re_email = data["FilterEmail"]
    re_provider = data["FilterProvider"]
    re_social_worker = data["FilterSocialWorker"]
    re_hospital_name = data["FilterHospitalName"]
    re_medicaid = data["FilterMedicaid"]
    re_allergies = data["FilterAllergies"]
    re_lab_results = data["FilterLabResults"]

    processedText = RemovePII(
        fullText,
        re_name,
        re_address,
        re_dob,
        re_ssn,
        re_phone,
        re_email,
        re_provider,
        re_social_worker,
        re_medicaid,
        re_lab_results,
        re_allergies,
        re_hospital_name,
    )

    response = {"text": processedText}
    return response


@post("/kill")
def kill():
    print("Terminated via page closed")
    sys.stderr.close()
