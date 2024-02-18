/**
 * v0 by Vercel.
 * @see https://v0.dev/t/E2JYQSvSgAe
 * Documentation: https://v0.dev/docs#integrating-generated-code-into-your-nextjs-app
 */
export default function NeighborhoodsInfo({ data }) {
	return (
		<div className="bg-white rounded-lg max-w-sm mx-auto pb-[20vh]">
			<div className="bg-hero-pattern overflow-hidden bg-gradient-to-d md:bg-gradient-to-d w-full">
				<div className="relative">
					<img
						alt="Photo 1"
						className="w-full h-[150px] object-cover"
						height="60"
						src="https://source.unsplash.com/random"
						style={{
							aspectRatio: "60/60",
							objectFit: "cover",
						}}
						width="60"
					/>

					<div className="absolute top-0 w-full h-full bg-gradient-to-t to-50% from-white to-transparent z-[2]"></div>
				</div>
			</div>
			<div className="p-4">
				<div className="flex items-center mb-4 gap-4">
					<img src="https://source.unsplash.com/random" className="object-cover w-12 h-12 rounded border" />
					<div className="flex flex-col">
						<h1 className="text-lg font-bold">{data.name}</h1>
						<span className="text-xs text-gray-500">{data.year_established} - Present</span>
					</div>
				</div>
				<div className="mb-4">
					<h2 className="text-base font-semibold mb-2">Photos</h2>
					<div className="grid grid-cols-3 gap-2">
						<img
							alt="Photo 1"
							className="col-span-2 row-span-2 w-full h-full object-cover rounded-md"
							height="60"
							src="https://source.unsplash.com/random"
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
							src="https://source.unsplash.com/random"
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
							src="https://source.unsplash.com/random"
							style={{
								aspectRatio: "60/60",
								objectFit: "cover",
							}}
							width="60"
						/>
					</div>
				</div>
				<p className="text-xs mb-4">
					Food halls in neighborhoods with higher average incomes tend to offer more gourmet food options. Gourmet food
					halls tend to have higher revenue than their more generalist counterparts. Conversely, with each new gourmet
					opening, revenues at prior establishments decline. Creating less competitive pricing strategies among food halls
					to attract price-sensitive customers.
				</p>
				<div className="mb-4">
					<h2 className="text-base font-semibold mb-2">Map</h2>
					<div className="flex flex-row gap-2 mb-2">
						<div class="flex-1 max-w-sm border rounded-md  overflow-hidden">
							<img
								alt="Map"
								className="map w-full h-32 object-cover"
								height="100"
								src="https://source.unsplash.com/random"
								style={{
									aspectRatio: "100/100",
									objectFit: "cover",
								}}
								width="100"
							/>
							<div class="pt-2 pl-2">
								<h2 className="ml-0 text-[0.7rem] font-bold">99 State St, Los Altos</h2>
								<p className="ml-0 pt-1 pb-2.5 text-[0.65rem] opacity-55">
									CA 94022
								</p>
							</div>
						</div>

						<div class="flex-1 max-w-sm border rounded-md  overflow-hidden">
							<img
								alt="3D Model"
								className="3d-model w-full h-32 object-cover"
								height="100"
								src="https://source.unsplash.com/random"
								style={{
									aspectRatio: "100/100",
									objectFit: "cover",
								}}
								width="100"
							/>
							<div class="pt-2 pl-2">
								<h2 className="ml-0 text-[0.7rem] font-bold">1,242 sqft</h2>
								<p className="ml-0 pt-1 pb-2.5 text-[0.65rem] opacity-55">
									Status: Built
								</p>
							</div>
						</div>
					</div>
				</div>

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
					<p className="text-xs mb-4">
						Food halls in neighborhoods with higher average incomes tend to offer more gourmet food options. Gourmet food
						halls tend to have higher revenue than their more generalist counterparts. Conversely, with each new gourmet
						opening, revenues at prior establishments decline. Creating less competitive pricing strategies among food halls
						to attract price-sensitive customers.
					</p>
				</div>
				<div className="mb-4">
					<h2 className="text-base font-semibold mb-2">Sources</h2>
					<div className="border border-gray-200 pl-0 py-4 ml-0 rounded-md">
						<ul className="ml-0 pl-4 text-xs list-none">
							<li className="py-2">
								<h2 className="ml-0 text-[0.7rem] font-bold">
									State Street Market in Los Altos, CA
								</h2>
								<a className="underline" href="#">
									<p className="text-[0.65rem] opacity-55" >
										https://maps.app.goo.gl/MDrMPxef62Mfw5Kr5
									</p>
								</a>
							</li>
							<li className="py-2">
								<h2 className="ml-0 text-[0.7rem] font-bold">
									State Street Market in Los Altos, CA
								</h2>
								<a className="underline" href="#">
									<p className="text-[0.65rem] opacity-55" >
										https://maps.app.goo.gl/MDrMPxef62Mfw5Kr5
									</p>
								</a>
							</li>
							<li className="py-2">
								<h2 className="ml-0 text-[0.7rem] font-bold">
									State Street Market in Los Altos, CA
								</h2>
								<a className="underline" href="#">
									<p className="text-[0.65rem] opacity-55" >
										https://maps.app.goo.gl/MDrMPxef62Mfw5Kr5
									</p>
								</a>
							</li>
						</ul>
					</div>
				</div>
			</div>
		</div >
	)
}

