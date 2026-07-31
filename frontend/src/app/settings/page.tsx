"use client";

import Navbar from "@/components/layout/Navbar";
import Sidebar from "@/components/layout/Sidebar";

import {
  Card,
  CardContent,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

import { Switch } from "@/components/ui/switch";
import { Button } from "@/components/ui/button";
import { Label } from "@/components/ui/label";

export default function SettingsPage() {
  return (
    <>
      <Navbar />

      <div className="flex">

        <Sidebar />

        <main className="flex-1 p-10">

          <h1 className="text-4xl font-bold">
            Settings
          </h1>

          <p className="text-gray-500 mt-2">
            Configure optimization preferences.
          </p>

          <Card className="mt-8">

            <CardHeader>

              <CardTitle>
                General Settings
              </CardTitle>

            </CardHeader>

            <CardContent className="space-y-6">

              <div className="flex items-center justify-between">

                <Label>Enable Auto Optimization</Label>

                <Switch />

              </div>

              <div className="flex items-center justify-between">

                <Label>Enable Benchmark Logging</Label>

                <Switch defaultChecked />

              </div>

              <div className="flex items-center justify-between">

                <Label>Save Benchmark History</Label>

                <Switch defaultChecked />

              </div>

              <Button className="mt-4">
                Save Settings
              </Button>

            </CardContent>

          </Card>

        </main>

      </div>
    </>
  );
}