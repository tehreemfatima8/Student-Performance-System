function RiskBadge({ risk }) {

    let color = "#22c55e";

    if (risk === "Medium") {

        color = "#f59e0b";

    }

    else if (risk === "High") {

        color = "#ef4444";

    }

    else if (risk === "Very Low") {

        color = "#3b82f6";

    }

    return (

        <div
            className="risk-badge"
            style={{
                background: color
            }}
        >

            Risk Level : {risk}

        </div>

    );

}

export default RiskBadge;