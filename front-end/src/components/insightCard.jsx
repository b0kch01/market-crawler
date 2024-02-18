import React from "react";
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

const InsightCard = ({ title, desc }) => {
  return (
    <div>
      <Card className="relative w-[450px] h-[220px] p-5 pb-2 overflow-hidden hover:rotate-1 hover:shadow-lg hover:scale-[1.02] transition-all cursor-default ease-out duration-500">
        <div className="overflow-auto h-full z-10">
          <p className="text-base font-bold break-words mb-2">{title}</p>
          <p className="text-sm">{desc}</p>
        </div>
        <img className="absolute w-full h-full top-0 left-0 blur-lg opacity-10" src="https://img.freepik.com/free-vector/gradient-blur-pink-blue-abstract-background_53876-117324.jpg" />
      </Card>
    </div>
  );
};

export default InsightCard;
