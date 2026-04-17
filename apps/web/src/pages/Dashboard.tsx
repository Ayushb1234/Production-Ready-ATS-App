import { useNavigate } from "react-router-dom";

export default function Dashboard() {
  const navigate = useNavigate();

  const token = localStorage.getItem("token");

  const logout = () => {
    localStorage.removeItem("token");
    navigate("/login");
  };

  return (
    <div style={{
      minHeight: "100vh",
      padding: "40px",
      fontFamily: "Arial"
    }}>
      
      <h1>Welcome to Dashboard 🚀</h1>
      <p>You are successfully logged in.</p>

      <div style={{
        marginTop: "20px",
        padding: "20px",
        border: "1px solid #ddd",
        borderRadius: "10px",
        maxWidth: "400px"
      }}>
        <h3>Account Info</h3>
        <p><strong>Plan:</strong> Free</p>
        <p><strong>Scans Left:</strong> 2</p>
        <p><strong>Token:</strong> {token ? "Active" : "Missing"}</p>
      </div>

      <div style={{ marginTop: "30px" }}>
        <button
          onClick={() => navigate("/scan")}
          style={{
            padding: "10px 20px",
            marginRight: "10px",
            cursor: "pointer"
          }}
        >
          Upload Resume
        </button>

        <button
          onClick={logout}
          style={{
            padding: "10px 20px",
            cursor: "pointer"
          }}
        >
          Logout
        </button>
      </div>
    </div>
  );
}