import { useState } from "react";
import API from "../services/api";
import PredictionCard from "./PredictionCard";
import RecommendationCard from "./RecommendationCard";
import RiskBadge from "./RiskBadge";

function StudentForm() {

    const [formData, setFormData] = useState({

        age: "",

        gender: "Male",

        study_hours_per_day: "",

        social_media_hours: "",

        netflix_hours: "",

        part_time_job: "No",

        attendance_percentage: "",

        sleep_hours: "",

        diet_quality: "Good",

        exercise_frequency: "",

        parental_education_level: "Bachelor",

        internet_quality: "Good",

        mental_health_rating: "",

        extracurricular_participation: "No"

    });

    const [result, setResult] = useState(null);
    const [loading, setLoading] = useState(false);

    const handleChange = (e) => {

        setFormData({

            ...formData,

            [e.target.name]: e.target.value

        });

    };

    const resetForm = () => {

    setFormData({

        age: "",

        gender: "Male",

        study_hours_per_day: "",

        social_media_hours: "",

        netflix_hours: "",

        part_time_job: "No",

        attendance_percentage: "",

        sleep_hours: "",

        diet_quality: "Good",

        exercise_frequency: "",

        parental_education_level: "Bachelor",

        internet_quality: "Good",

        mental_health_rating: "",

        extracurricular_participation: "No"

    });

    setResult(null);

};

    const handleSubmit = async (e) => {

        e.preventDefault();

        // Required Fields

if (

    !formData.age ||

    formData.study_hours_per_day === "" ||

    !formData.attendance_percentage ||

    !formData.sleep_hours ||

    !formData.exercise_frequency ||

    !formData.mental_health_rating

){

    alert("Please fill all required fields.");

    return;

}


// Attendance

if(formData.attendance_percentage < 0 || formData.attendance_percentage > 100){

    alert("Attendance must be between 0 and 100.");

    return;

}


// Study Hours

if(formData.study_hours_per_day < 0 || formData.study_hours_per_day > 12){

    alert("Study hours should be between 0 and 12.");

    return;

}


// Sleep

if(formData.sleep_hours < 0 || formData.sleep_hours > 24){

    alert("Sleep hours should be between 0 and 24.");

    return;

}


// Mental Health

if(formData.mental_health_rating < 1 || formData.mental_health_rating > 10){

    alert("Mental Health Rating should be between 1 and 10.");

    return;

}

        const data = {

            ...formData,

            age: Number(formData.age),

            study_hours_per_day: Number(formData.study_hours_per_day),

            social_media_hours: Number(formData.social_media_hours),

            netflix_hours: Number(formData.netflix_hours),

            attendance_percentage: Number(formData.attendance_percentage),

            sleep_hours: Number(formData.sleep_hours),

            exercise_frequency: Number(formData.exercise_frequency),

            mental_health_rating: Number(formData.mental_health_rating)

        };

        console.log("Sending:", data);

        try {

    setLoading(true);

    const response = await API.post("/predict", data);

            console.log(response.data);

            setResult(response.data);

            setLoading(false);

        }

        catch (error) {

            setLoading(false);
            if (error.response) {

                console.log(error.response.data);

                alert(error.response.data.error);

            }

            else {

                console.log(error.message);

                alert("Cannot connect to Flask backend.");

            }

        }

    };

    return (

        <>

            <form onSubmit={handleSubmit}>

                <h3>Student Information</h3>

                <div className="form-grid">

                    {/* Age */}

                    <div>

                        <label>Age</label>

                        <input
                            type="number"
                            name="age"
                            value={formData.age}
                            onChange={handleChange}
                        />

                    </div>

                    {/* Gender */}

                    <div>

                        <label>Gender</label>

                        <select
                            name="gender"
                            value={formData.gender}
                            onChange={handleChange}
                        >

                            <option>Male</option>

                            <option>Female</option>

                        </select>

                    </div>

                    {/* Study Hours */}

                    <div>

                        <label>Study Hours / Day</label>

                        <input
                            type="number"
                            name="study_hours_per_day"
                            value={formData.study_hours_per_day}
                            onChange={handleChange}
                        />

                    </div>

                    {/* Attendance */}

                    <div>

                        <label>Attendance %</label>

                        <input
                            type="number"
                            name="attendance_percentage"
                            value={formData.attendance_percentage}
                            onChange={handleChange}
                        />

                    </div>

                    {/* Social Media */}

                    <div>

                        <label>Social Media Hours</label>

                        <input
                            type="number"
                            name="social_media_hours"
                            value={formData.social_media_hours}
                            onChange={handleChange}
                        />

                    </div>

                    {/* Netflix */}

                    <div>

                        <label>Netflix Hours</label>

                        <input
                            type="number"
                            name="netflix_hours"
                            value={formData.netflix_hours}
                            onChange={handleChange}
                        />

                    </div>

                    {/* Sleep */}

                    <div>

                        <label>Sleep Hours</label>

                        <input
                            type="number"
                            name="sleep_hours"
                            value={formData.sleep_hours}
                            onChange={handleChange}
                        />

                    </div>

                    {/* Exercise */}

                    <div>

                        <label>Exercise Frequency</label>

                        <input
                            type="number"
                            name="exercise_frequency"
                            value={formData.exercise_frequency}
                            onChange={handleChange}
                        />

                    </div>

                    {/* Diet */}

                    <div>

                        <label>Diet Quality</label>

                        <select
                            name="diet_quality"
                            value={formData.diet_quality}
                            onChange={handleChange}
                        >

                            <option>Good</option>

                            <option>Average</option>

                            <option>Poor</option>

                        </select>

                    </div>

                    {/* Internet */}

                    <div>

                        <label>Internet Quality</label>

                        <select
                            name="internet_quality"
                            value={formData.internet_quality}
                            onChange={handleChange}
                        >

                            <option>Good</option>

                            <option>Average</option>

                            <option>Poor</option>

                        </select>

                    </div>

                    {/* Parent Education */}

                    <div>

                        <label>Parent Education</label>

                        <select
                            name="parental_education_level"
                            value={formData.parental_education_level}
                            onChange={handleChange}
                        >

                            <option>High School</option>

                            <option>Bachelor</option>

                            <option>Master</option>

                            <option>PhD</option>

                        </select>

                    </div>

                    {/* Part Time Job */}

                    <div>

                        <label>Part Time Job</label>

                        <select
                            name="part_time_job"
                            value={formData.part_time_job}
                            onChange={handleChange}
                        >

                            <option>Yes</option>

                            <option>No</option>

                        </select>

                    </div>

                    {/* Mental Health */}

                    <div>

                        <label>Mental Health Rating</label>

                        <input
                            type="number"
                            name="mental_health_rating"
                            value={formData.mental_health_rating}
                            onChange={handleChange}
                        />

                    </div>

                    {/* Extracurricular */}

                    <div>

                        <label>Extracurricular</label>

                        <select
                            name="extracurricular_participation"
                            value={formData.extracurricular_participation}
                            onChange={handleChange}
                        >

                            <option>Yes</option>

                            <option>No</option>

                        </select>

                    </div>

                </div>

                <div className="button-group">

    <button

        type="submit"

        disabled={loading}

    >

        {

            loading

            ?

            "Analyzing Student Performance..."

            :

            "Predict Performance"

        }

    </button>

    <button

        type="button"

        className="reset-btn"

        onClick={resetForm}

    >

        Reset Form

    </button>

</div>

            </form>

            {result && (

    <>

        <PredictionCard
            prediction={result.prediction}
        />

        <RiskBadge
            risk={result.recommendations.risk_level}
        />

        <RecommendationCard
            title="Academic Habits"
            items={result.recommendations["Academic Habits"]}
        />

        <RecommendationCard
            title="Health & Lifestyle"
            items={result.recommendations["Health & Lifestyle"]}
        />

        <RecommendationCard
            title="Technology Usage"
            items={result.recommendations["Technology Usage"]}
        />

        <RecommendationCard
            title="Overall Advice"
            items={result.recommendations["Overall Advice"]}
        />

    </>

)}
        </>

    );

}

export default StudentForm;