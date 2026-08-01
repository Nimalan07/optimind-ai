"use client";

import { useEffect, useState } from "react";
import Navbar from "@/components/layout/Navbar";
import Sidebar from "@/components/layout/Sidebar";

import {
  Card,
  CardContent,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";

import { Badge } from "@/components/ui/badge";

const initialHistory = [
  {
    id: 1,
    model: "Llama 3.2 3B",
    optimization: "INT4 + GGUF",
    latency: "1.6 s",
    memory: "2.5 GB",
    status: "Completed",
  },
  {
    id: 2,
    model: "Gemma 2B",
    optimization: "ONNX",
    latency: "2.2 s",
    memory: "3.1 GB",
    status: "Completed",
  },
  {
    id: 3,
    model: "Qwen 2.5",
    optimization: "INT8",
    latency: "2.0 s",
    memory: "2.8 GB",
    status: "Running",
  },
];

export default function HistoryPage() {
  const [historyList, setHistoryList] = useState<any[]>([]);

  useEffect(() => {
    const saved = localStorage.getItem("optimindHistory");
    if (saved) {
      setHistoryList(JSON.parse(saved));
    } else {
      localStorage.setItem("optimindHistory", JSON.stringify(initialHistory));
      setHistoryList(initialHistory);
    }
  }, []);

  return (
    <>
      <Navbar />

      <div className="flex">
        <Sidebar />

        <main className="flex-1 p-10">
          <h1 className="text-4xl font-bold">Benchmark History</h1>
          <p className="text-gray-500 mt-2">
            View previous optimization runs.
          </p>

          <Card className="mt-8">
            <CardHeader>
              <CardTitle>Previous Benchmarks</CardTitle>
            </CardHeader>

            <CardContent>
              <Table>
                <TableHeader>
                  <TableRow>
                    <TableHead>Model</TableHead>
                    <TableHead>Optimization</TableHead>
                    <TableHead>Latency</TableHead>
                    <TableHead>Memory</TableHead>
                    <TableHead>Status</TableHead>
                  </TableRow>
                </TableHeader>

                <TableBody>
                  {historyList.map((item) => (
                    <TableRow key={item.id}>
                      <TableCell className="font-medium">{item.model}</TableCell>
                      <TableCell>{item.optimization}</TableCell>
                      <TableCell>{item.latency}</TableCell>
                      <TableCell>{item.memory}</TableCell>
                      <TableCell>
                        <Badge
                          variant={
                            item.status === "Completed"
                              ? "default"
                              : "secondary"
                          }
                        >
                          {item.status}
                        </Badge>
                      </TableCell>
                    </TableRow>
                  ))}
                </TableBody>
              </Table>
            </CardContent>
          </Card>
        </main>
      </div>
    </>
  );
}