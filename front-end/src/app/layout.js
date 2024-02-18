import { Inter } from "next/font/google";
import "./globals.css";
import { DataContextProvider } from "../contexts/data-context";

const inter = Inter({ subsets: ["latin"] });

export const metadata = {
  title: "Market Crawler",
  description: "2024 TreeHacks project",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <DataContextProvider>
          {children}
        </DataContextProvider>
      </body>
    </html>
  );
}
