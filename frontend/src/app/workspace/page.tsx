import Sidebar from "@/components/layout/Sidebar";
import Navbar from "@/components/layout/Navbar";

export default function Workspace() {

    return (

        <>

            <Navbar />

            <div className="flex">

                <Sidebar />

                <main className="flex-1 p-10">

                    <h1 className="text-4xl font-bold">

                        Dashboard

                    </h1>

                    <div className="grid grid-cols-4 gap-6 mt-10">

                        <div className="border rounded-xl p-6">

                            <h2>Total Models</h2>

                            <p className="text-3xl font-bold mt-2">

                                0

                            </p>

                        </div>

                        <div className="border rounded-xl p-6">

                            <h2>Benchmarks</h2>

                            <p className="text-3xl font-bold mt-2">

                                0

                            </p>

                        </div>

                        <div className="border rounded-xl p-6">

                            <h2>Optimizations</h2>

                            <p className="text-3xl font-bold mt-2">

                                0

                            </p>

                        </div>

                        <div className="border rounded-xl p-6">

                            <h2>Reports</h2>

                            <p className="text-3xl font-bold mt-2">

                                0

                            </p>

                        </div>

                    </div>

                </main>

            </div>

        </>

    )

}