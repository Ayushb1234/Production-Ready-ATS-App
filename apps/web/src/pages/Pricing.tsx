export default function Pricing() {
  return (
    <div className="p-10 text-white bg-gray-950 min-h-screen">
      <h1 className="text-4xl font-bold mb-10">
        Pricing 🚀
      </h1>

      <div className="grid md:grid-cols-2 gap-6">

        <div className="bg-gray-900 p-8 rounded-2xl">
          <h2 className="text-2xl">Free</h2>
          <p>2 Scans</p>
        </div>

        <div className="bg-green-500 text-black p-8 rounded-2xl">
          <h2 className="text-2xl font-bold">Pro ₹199</h2>
          <p>Unlimited Scans</p>
          <p>AI Resume Rewrite</p>
        </div>

      </div>
    </div>
  );
}