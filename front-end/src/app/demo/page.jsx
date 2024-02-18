"use client";
import InsightCard from "@/components/insightCard";
import Navbar from "@/components/navbar";
import SearchBar from "@/components/searchbar";
import { DataTableDemo } from "@/components/views/datatable-demo";

export default function DemoPage() {
  return (
    <div className="bg-[#F4F4F4] flex flex-col p-25px pb-40">
      <Navbar />
      <div className="px-[10vw]">
        <SearchBar onClick={() => { }} />
        <div className="flex flex-row align-middle items-center gap-2 items-center mb-5">
          <img src="black.svg" className="w-7 h-7" alt="Insight Icon" />
          <p className="font-bold text-xl">Insights</p>
        </div>
        <div className="flex flex-row gap-2 overflow-x-auto">
          <InsightCard title={"Market Segmentation and Target Demographics"} desc={"The food halls located in downtown Palo Alto are frequented more by millennials and Gen Z, who prefer quick, diverse, and Instagram-worthy food options. This contrasts with food halls in the suburbs, which see a higher footfall from families and baby boomers, indicating a preference for traditional cuisines and a more relaxed dining experience."} />
          <InsightCard title={"Cuisine Popularity vs. Demographic Preferences"} desc={"Analysis reveals a high demand for plant-based and gluten-free options among the younger demographics, particularly in areas with a higher concentration of tech companies. This trend is less pronounced in areas with an older demographic, where there is a consistent preference for classic American and Italian cuisines."} />
          <InsightCard title={"Pricing Strategies Based on Local Income Levels"} desc={"Food halls in neighborhoods with higher average incomes tend to offer more gourmet dining options, with prices to match, and have a higher rate of repeat customers for these premium options. Conversely, areas with lower average incomes have a greater demand for affordable dining options, leading to competitive pricing strategies among food halls to attract price-sensitive customers."} />
          <InsightCard title={"Impact of Location on Foot Traffic"} desc={"Food halls located near public transportation hubs or in close proximity to major employers in Palo Alto experience higher weekday foot traffic, suggesting a significant lunchtime crowd. In contrast, those situated near parks or recreational areas see a spike in weekend traffic, indicating they are preferred for leisurely meals and family outings."} />
        </div>

        <p className="font-bold text-xl mt-5">Data</p>
        <DataTableDemo />
      </div>
    </div>
  );
}
