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
      <Card className="w-[450px] h-[200px] max-h-[200px] p-5 pb-2 overflow-hidden">
        <div className="overflow-auto h-full">
          <p className="text-base font-bold break-words">{title}</p>
          <p className="text-sm">{desc}</p>
        </div>
      </Card>
    </div>
  );
};

export default InsightCard;
