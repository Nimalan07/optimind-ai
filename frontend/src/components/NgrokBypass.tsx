"use client";

import { useEffect } from "react";

export default function NgrokBypass() {
  useEffect(() => {
    if (typeof window !== "undefined") {
      const originalFetch = window.fetch;
      window.fetch = function (input, init) {
        const fetchInit = init || {};
        let headers = fetchInit.headers || {};

        if (headers instanceof Headers) {
          headers.set("ngrok-skip-browser-warning", "true");
        } else if (Array.isArray(headers)) {
          headers.push(["ngrok-skip-browser-warning", "true"]);
        } else {
          headers = {
            ...headers,
            "ngrok-skip-browser-warning": "true",
          };
        }

        fetchInit.headers = headers;
        return originalFetch(input, fetchInit);
      };
    }
  }, []);

  return null;
}
