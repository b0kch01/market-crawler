import { useEffect } from "react";
import { BusFront, TrainFront, Bike, Plane, Building, Store, LandPlot } from "lucide-react"

/**
 * v0 by Vercel.
 * @see https://v0.dev/t/E2JYQSvSgAe
 * Documentation: https://v0.dev/docs#integrating-generated-code-into-your-nextjs-app
 */
export default function NeighborhoodsInfo({ data }) {

	if (!data) {
		return <div>Loading...</div>;
	}

	console.log(data)

	return (
		<div className="bg-white rounded-lg pb-[20vh]">
			<div className="bg-hero-pattern overflow-hidden bg-gradient-to-d w-full">
				<div className="relative">
					{
						!data.images ? <div className="bg-stone-300 w-full h-44"></div> :
							<img
								alt="Photo 1"
								className="w-full h-[150px] object-cover"
								src={"https://source.unsplash.com/random/?resturaunt"}
								style={{
									aspectRatio: "60/60",
									objectFit: "cover",
								}}
							/>
					}

					<div className="absolute top-0 w-full h-full bg-gradient-to-t to-50% from-white to-transparent z-[2]"></div>
				</div>
			</div>

			<div className="p-4">
				<div className="flex items-center mb-4 gap-4">
					<p className="object-cover w-12 h-12 rounded border text-3xl flex items-center justify-center opacity-85">
						{data.name.charAt(0).toUpperCase()}
					</p>
					<div className="flex flex-col">
						<h1 className="text-lg font-bold">{data.name}</h1>
						<span className="text-xs text-gray-500">{data.year_established} - Present</span>
					</div>
				</div>

				{
					!data.city || !data.state ? null :
						<div className="mb-4">
							<div className="flex flex-row gap-2 mb-2">
								<div class="flex-1 max-w-sm border rounded-md  overflow-hidden">
									<img className="map w-full h-32 object-cover" src={`https://maps.googleapis.com/maps/api/staticmap?center=${data.name},${data.state}zoom=16&size=400x400&key=AIzaSyCHUJhIvbMeTZS4h-YrgJp5QmhPw1JhZ2I`} />
									<div class="pt-2 pl-2">
										<h2 className="ml-0 text-[0.7rem] font-bold">{data.city}, {data.state}</h2>
										<p className="ml-0 pt-1 pb-2.5 text-[0.65rem] opacity-55">
											Live Map
										</p>
									</div>
								</div>

								<div class="flex-1 max-w-sm border rounded-md  overflow-hidden">
									<img className="map w-full h-32 object-cover" src={`https://maps.googleapis.com/maps/api/staticmap?center=${data.name},${data.state}zoom=1&maptype=satellite&&size=400x400&key=AIzaSyCHUJhIvbMeTZS4h-YrgJp5QmhPw1JhZ2I`} />
									<div class="pt-2 pl-2">
										<h2 className="ml-0 text-[0.7rem] font-bold">{data.population_density}</h2>
										<p className="ml-0 pt-1 pb-2.5 text-[0.65rem] opacity-55">
											Population Density
										</p>
									</div>
								</div>
							</div>
						</div>
				}


				<div className="mb-4">
					<h2 className="text-base font-semibold mb-2">Photo Gallery</h2>
					<div className="grid grid-cols-3 gap-2">
						{!data.images ? null : <>
							<img
								alt="Photo 1"
								className="col-span-2 row-span-2 w-full h-full object-cover rounded-md"
								height="60"
								src={data.images[6].url}
								style={{
									aspectRatio: "60/60",
									objectFit: "cover",
								}}
								width="60"
							/>
							<img
								alt="Photo 2"
								className="w-full h-full object-cover rounded-md"
								height="60"
								src={data.images[8].url}
								style={{
									aspectRatio: "60/60",
									objectFit: "cover",
								}}
								width="60"
							/>
							<img
								alt="Photo 3"
								className="w-full h-full object-cover rounded-md"
								height="60"
								src={data.images[9].url}
								style={{
									aspectRatio: "60/60",
									objectFit: "cover",
								}}
								width="60"
							/>
						</>}

					</div>
				</div>

				<div className="flex flex-col">

					{data.public_transport && <>
						<h2 className="text-base font-semibold mb-2">Public Transport Options</h2>
						<div className="flex flex-row gap-2 mb-4	">
							<div class="flex-1 max-w-sm border rounded-md overflow-hidden">
								<div className="flex justify-between m-2">
									<BusFront className="" />
									{
										data.public_transport.includes("bus") ? <span className="bg-green-200 text-green-700 text-xs rounded-full px-2 py-1 h-fit">Available</span> :
											<span className="bg-red-200 text-red-700 text-xs rounded-full px-2 py-1 h-fit">Unavailable</span>
									}
								</div>
								<span className="m-2 font-medium">Bus</span>
								<div className="text-xs mx-2 mb-2 text-muted-foreground">MUNI, SamTrans</div>
							</div>
							<div class="flex-1 max-w-sm border rounded-md overflow-hidden">
								<div className="flex justify-between m-2">
									<TrainFront className="" />
									{
										data.public_transport.includes("train") ? <span className="bg-green-200 text-green-700 text-xs rounded-full px-2 py-1 h-fit">Available</span> :
											<span className="bg-red-200 text-red-700 text-xs rounded-full px-2 py-1 h-fit">Unavailable</span>
									}
								</div>
								<span className="m-2 font-medium">Train</span>
								<div className="text-xs mx-2 mb-2 text-muted-foreground">WeTrain, Freik</div>
							</div>
							<div class="flex-1 max-w-sm border rounded-md overflow-hidden">
								<div className="flex justify-between m-2">
									<Bike className="" />
									{
										data.public_transport.includes("bike") ? <span className="bg-green-200 text-green-700 text-xs rounded-full px-2 py-1 h-fit">Available</span> :
											<span className="bg-red-200 text-red-700 text-xs rounded-full px-2 py-1 h-fit">Unavailable</span>
									}
								</div>
								<span className="m-2 font-medium">Bike</span>
								<div className="text-xs mx-2 mb-2 text-muted-foreground">Lime, Citi</div>
							</div>
							<div class="flex-1 max-w-sm border rounded-md overflow-hidden">
								<div className="flex justify-between m-2">
									<Plane className="" />
									<span className="bg-red-200 text-red-700 text-xs rounded-full px-2 py-1 h-fit">Unavailable</span>
								</div>
								<span className="m-2 font-medium">Plane</span>
								<div className="text-xs mx-2 mb-2 text-muted-foreground">WeTrain, Freik</div>
							</div>
						</div>

					</>}
				</div>

				<div className="flex gap-2">

					{
						!data.age_distribution ? null : (
							<div className="mb-4 flex-1">
								<h2 className="text-sm font-medium mb-2">Age Distribution</h2>
								<div className="border border-gray-200 pl-0 py-2 ml-0 rounded-md">
									<ul className="ml-0 pl-4 text-xs list-none">
										{
											Object.keys(data.age_distribution).map((age, index) => {
												return (
													<li key={index} className="py-2">
														<h2 className="ml-0 text-[0.7rem] font-bold">{age}</h2>
														<span className="text-[0.65rem] opacity-55" >
															{data.age_distribution[age] == "N/A" ? "Unknown %" : data.age_distribution[age] + "%"}
														</span>
													</li>
												)
											})
										}
									</ul>
								</div>
							</div>
						)
					}

					{
						!data.annual_visitor_count ? null :
							<div className="mb-4 flex-1">
								<h2 className="text-sm font-medium mb-2">Annual Visitors</h2>
								<div className="border border-gray-200 pl-0 py-2 ml-0 rounded-md">
									<span className="text-xs ml-0 pl-4">
										{`${data.annual_visitor_count}`}
									</span>
								</div>
							</div>
					}

					{
						!data.median_income ? null :
							<div className="mb-4 flex-1">
								<h2 className="text-sm font-medium mb-2">Median Income</h2>
								<div className="border border-gray-200 pl-0 py-2 ml-0 rounded-md">
									<span className="text-xs ml-0 pl-4">
										{`${data.median_income}`}
									</span>
								</div>
							</div>
					}

					{
						!data.lease_rates ? null :
							<div className="mb-4 flex-1">
								<h2 className="text-sm font-mediummedium mb-2">Lease Rates</h2>
								<div className="border border-gray-200 pl-0 py-2 ml-0 rounded-md">
									<span className="text-xs ml-0 pl-4">
										{`${data.lease_rates}`}
									</span>
								</div>
							</div>
					}
				</div>

				{/* Nearby development (office, retail, or residential), array of strings */}
				{/* Matching icons */}

				{
					!data.composition ? null :
						<div className="relative my-5">
							<div className="mb-4 flex justify-center gap-10">
								{
									!data.composition ? null : data.composition.map((item, index) => {
										return (
											<div key={index} className="flex flex-col justify-center gap-2 items-center h-[150px]">
												<div className="w-[70px] h-[70px] border bg-stone-50 rounded-full flex justify-center items-center z-10">
													{
														item == "office" ? <Building /> :
															item == "retail" ? <Store /> :
																item == "residential" ? <LandPlot /> : null
													}
												</div>
												<p className="text-sm text-center py-2">
													{item.charAt(0).toUpperCase() + item.slice(1) + " ✓"}
												</p>
											</div>
										)
									})
								}
								<hr className="absolute rounded-full top-[35%] opacity-25 w-full h-[1px] bg-stone-500 outline-none border-none" />
							</div>
						</div>
				}
				{/* 
				<div className="mb-4">
					<h2 className="text-base font-semibold mb-2">Stakeholders Involved</h2>
					<div className="flex flex-row gap-1 mb-2">
						<div class="flex-1 border rounded overflow-hidden">

							<img
								alt="Joshua Choi"
								className="w-full h-32 rounded-md border-2 border-white"
								height="100"
								src="https://source.unsplash.com/random"
								style={{
									aspectRatio: "100/100",
									objectFit: "cover",
								}}
								heigwidth="100"
							/>
							<div class="pt-2 pl-2">
								<h2 className="ml-0 text-[0.7rem] font-bold">Joshua Choi</h2>
								<p className="ml-0 pt-1 pb-2.5 text-[0.65rem] opacity-55">
									Agent
								</p>
							</div>

						</div>
						<div class="flex-1 max-w-sm border rounded overflow-hidden">

							<img
								alt="Austin Lee"
								className="w-full h-32 rounded-md border-2 border-white"
								height="100"
								src="https://source.unsplash.com/random"
								style={{
									aspectRatio: "100/100",
									objectFit: "cover",
								}}
								heigwidth="100"
							/>
							<div class="pt-2 pl-2">
								<h2 className="ml-0 text-[0.7rem] font-bold">Austin Lee</h2>
								<p className="ml-0 pt-1 pb-2.5 text-[0.65rem] opacity-55">
									Architect
								</p>
							</div>
						</div>
						<div class="flex-1 max-w-sm border rounded overflow-hidden">
							<img
								alt="Nathan Choi"
								className="w-full h-32 rounded-md border-2 border-white"
								height="100"
								src="https://source.unsplash.com/random"
								style={{
									aspectRatio: "100/100",
									objectFit: "cover",
								}}
								heigwidth="100"
							/>
							<div class="pt-2 pl-2">
								<h2 className="ml-0 text-[0.7rem] font-bold">Nathan Choi</h2>
								<p className="ml-0 pt-1 pb-2.5 text-[0.65rem] opacity-55">
									Developer
								</p>
							</div>
						</div>
						<div class="flex-1 max-w-sm border rounded overflow-hidden">
							<img
								alt="Albert Chen"
								className="w-full h-32 rounded-md border-2 border-white"
								height="100"
								src="https://source.unsplash.com/random"
								style={{
									aspectRatio: "100/100",
									objectFit: "cover",
								}}
								heigwidth="100"
							/>
							<div class="pt-2 pl-2">
								<h2 className="ml-0 text-[0.7rem] font-bold">Albert Chen</h2>
								<p className="ml-0 pt-1 pb-2.5 text-[0.65rem] opacity-55">
									Developer
								</p>
							</div>
						</div>
					</div>
				</div> */}
				{
					!data.sources ? null :
						<div className="mb-4">
							<h2 className="text-base font-semibold mb-2">Sources</h2>
							<div className="border border-gray-200 pl-0 py-2 ml-0 rounded-md">
								<ul className="ml-0 pl-4 text-xs list-none">
									{
										!data.sources ? null : data.sources.map(({ source, label }, index) => {
											return (
												<li key={index} className="py-2">
													<h2 className="ml-0 text-[0.7rem] font-bold">{label}</h2>
													<a className="underline" href={source}>
														<p className="text-[0.65rem] opacity-55" >
															{source}
														</p>
													</a>
												</li>
											)
										})

									}
								</ul>
							</div>
						</div>
				}
			</div>
		</div >
	)
}

