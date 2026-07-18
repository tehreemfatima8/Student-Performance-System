function PredictionCard({ prediction }) {

    return (

        <div className="prediction-card">

            <h2>Prediction Result</h2>

            <div className="prediction-item">

                <strong>Predicted Score</strong>

                <p>{prediction.predicted_score}</p>

            </div>

            <div className="prediction-item">

                <strong>Prediction</strong>

                <p>{prediction.prediction}</p>

            </div>

            <div className="prediction-item">

                <strong>Confidence</strong>

                <p>{prediction.confidence}%</p>

            </div>

        </div>

    );

}

export default PredictionCard;