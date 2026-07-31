import Navbar from "@/components/layout/Navbar";
import Sidebar from "@/components/layout/Sidebar";

export default function AboutPage() {
  return (
    <>
      <Navbar />
      <div className="flex">
        <Sidebar />
        <main className="flex-1 p-10">
          <h1 className="text-4xl font-bold">About</h1>
          <p className="text-gray-500 mt-2">OptiMind AI v1.0.0</p>
        </main>
      </div>
    </>
  );
}
