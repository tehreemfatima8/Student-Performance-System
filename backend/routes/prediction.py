from flask import Blueprint, request, jsonify

from ml.recommendation import generate_recommendations

from ml.predict import predict_student

prediction_bp = Blueprint(
    "prediction",
    __name__
)



@prediction_bp.route(
    "/predict",
    methods=["POST"]
)
def prediction():

    try:

        student_data = request.json


        # Step 1:
        # AI Model Prediction

        prediction_result = predict_student(student_data)



        # Step 2:
        # Generate Recommendations

        recommendations = generate_recommendations(
            student_data,
            prediction_result
        )



        # Step 3:
        # Final Response


        return jsonify({

            "prediction":prediction_result,

            "recommendations":recommendations

        })


    except Exception as e:

        return jsonify({

            "error":str(e)

        }),500