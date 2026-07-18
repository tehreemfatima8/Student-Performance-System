function RecommendationCard({ title, items }) {

    return (

        <div className="recommendation-card">

            <h3>{title}</h3>

            {

                items.length === 0 ?

                <p>No recommendations.</p>

                :

                <ul>

                    {

                        items.map((item, index) => (

                            <li key={index}>

                                {item}

                            </li>

                        ))

                    }

                </ul>

            }

        </div>

    );

}

export default RecommendationCard;