// import { useNavigate } from "react-router-dom";

// export default function Dashboard() {
//   const navigate = useNavigate();

//   const token = localStorage.getItem("token");

//   const logout = () => {
//     localStorage.removeItem("token");
//     navigate("/login");
//   };

//   return (
//     <div style={{
//       minHeight: "100vh",
//       padding: "40px",
//       fontFamily: "Arial"
//     }}>
      
//       <h1>Welcome to Dashboard 🚀</h1>
//       <p>You are successfully logged in.</p>

//       <div style={{
//         marginTop: "20px",
//         padding: "20px",
//         border: "1px solid #ddd",
//         borderRadius: "10px",
//         maxWidth: "400px"
//       }}>
//         <h3>Account Info</h3>
//         <p><strong>Plan:</strong> Free</p>
//         <p><strong>Scans Left:</strong> 2</p>
//         <p><strong>Token:</strong> {token ? "Active" : "Missing"}</p>
//       </div>

//       <div style={{ marginTop: "30px" }}>
//         <button
//           onClick={() => navigate("/scan")}
//           style={{
//             padding: "10px 20px",
//             marginRight: "10px",
//             cursor: "pointer"
//           }}
//         >
//           Upload Resume
//         </button>

//         <button
//           onClick={logout}
//           style={{
//             padding: "10px 20px",
//             cursor: "pointer"
//           }}
//         >
//           Logout
//         </button>
//       </div>
//     </div>
//   );
// }

import { useState } from "react";
import { api } from "../services/api";

export default function Dashboard() {
  const [file, setFile] = useState<File | null>(null);
  const [jd, setJd] = useState("");
  const [result, setResult] = useState<any>(null);

  const scanResume = async () => {
    const formData = new FormData();

    if (file) formData.append("file", file);
    formData.append("jd_text", jd);

    const res = await api.post("/scan-ai/", formData, {
      headers: {
        "Content-Type": "multipart/form-data"
      }
    });

    setResult(res.data);
  };

  return (
    <div style={{ padding: "40px" }}>
      <h1>ATS Resume Scanner 🚀</h1>

      <input
        type="file"
        onChange={(e) => setFile(e.target.files?.[0] || null)}
      />

      <br /><br />

      <textarea
        rows={10}
        cols={60}
        placeholder="Paste Job Description"
        onChange={(e) => setJd(e.target.value)}
      />
      

      <br /><br />

      <button onClick={scanResume}>
        Scan Resume
      </button>

     {result && (
  <div style={{ marginTop: "30px" }}>
    <h2>ATS Score: {result.score}%</h2>

    <h3>Breakdown</h3>
    <p>Required Skills: {result.breakdown?.required}%</p>
    <p>Preferred Skills: {result.breakdown?.preferred}%</p>
    <p>Experience: {result.breakdown?.experience}%</p>
    <p>Education: {result.breakdown?.education}%</p>

    <h3>Missing Skills</h3>
    <p>

      {result.missing_skills?.length
        ? result.missing_skills.join(", ")
        : "None"}
    </p>
  </div>
)}
    </div>
  );
}