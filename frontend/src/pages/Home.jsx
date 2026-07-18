import Header from "../components/Header";
import Footer from "../components/Footer";
import StudentForm from "../components/StudentForm";
import "../styles/Home.css";

function Home() {
  return (
    <div className="home-container">

      <Header />

      <main className="main-content">

        <h2>Student Performance Prediction</h2>

        <p>
          Enter the student's academic and lifestyle information
          to predict exam performance.
        </p>

        <StudentForm />

      </main>

      <Footer />

    </div>
  );
}

export default Home;