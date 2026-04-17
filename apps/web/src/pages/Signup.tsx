import { useState } from "react";
import { api } from "../services/api";
import { Link } from "react-router-dom";

export default function Signup() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const submit = async () => {
    await api.post("/auth/signup", {
      email,
      password,
      full_name: "Ayush"
    });

    alert("Signup success");
  };

  return (
    <div>
      <input onChange={(e)=>setEmail(e.target.value)} placeholder="Email" />
      <input type="password" onChange={(e)=>setPassword(e.target.value)} placeholder="Password" />
      <button onClick={submit}>Signup</button>
      Already have an account? <Link to="/login">Login</Link>
    </div>
  );
}