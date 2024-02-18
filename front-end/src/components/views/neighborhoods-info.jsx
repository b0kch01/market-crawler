/**
 * v0 by Vercel.
 * @see https://v0.dev/t/E2JYQSvSgAe
 * Documentation: https://v0.dev/docs#integrating-generated-code-into-your-nextjs-app
 */
export default function NeighborhoodsInfo() {
	return (
		<div className="bg-white p-4 rounded-lg max-w-sm mx-auto pb-[20vh]">
			<div className="flex justify-between items-center mb-4">
				<h1 className="text-lg font-bold">State Street Market</h1>
				<span className="text-xs text-gray-500">2004 - Present</span>
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
				<div className="flex justify-between items-center mb-2">
					<img
						alt="Map"
						className="w-full h-32 rounded-md object-cover"
						height="100"
						src="https://source.unsplash.com/random"
						style={{
							aspectRatio: "100/100",
							objectFit: "cover",
						}}
						width="100"
					/>
					<img
						alt="Map"
						className="w-full h-32 rounded-md object-cover"
						height="100"
						src="https://source.unsplash.com/random"
						style={{
							aspectRatio: "100/100",
							objectFit: "cover",
						}}
						width="100"
					/>
					<div className="ml-4">
						<p className="text-xs">99 State St, Los Altos</p>
						<p className="text-xs">1,342 sqft</p>
					</div>
				</div>
			</div>
			<div className="mb-4">
				<h2 className="text-base font-semibold mb-2">Stakeholders Involved</h2>
				<div className="flex -space-x-2">
					<img
						alt="Joshua Choi"
						className="w-10 h-10 rounded-md border-2 border-white"
						height="40"
						src="https://source.unsplash.com/random"
						style={{
							aspectRatio: "40/40",
							objectFit: "cover",
						}}
						width="40"
					/>
					<img
						alt="Austin Lee"
						className="w-10 h-10 rounded-md border-2 border-white"
						height="40"
						src="https://source.unsplash.com/random"
						style={{
							aspectRatio: "40/40",
							objectFit: "cover",
						}}
						width="40"
					/>
					<img
						alt="Nathan Choi"
						className="w-10 h-10 rounded-md border-2 border-white"
						height="40"
						src="https://source.unsplash.com/random"
						style={{
							aspectRatio: "40/40",
							objectFit: "cover",
						}}
						width="40"
					/>
					<img
						alt="Albert Chen"
						className="w-10 h-10 rounded-md border-2 border-white"
						height="40"
						src="https://source.unsplash.com/random"
						style={{
							aspectRatio: "40/40",
							objectFit: "cover",
						}}
						width="40"
					/>
				</div>
			</div>
			<div className="mb-4">
				<h2 className="text-base font-semibold mb-2">Sources</h2>
				<div className="border border-gray-200 p-4 rounded-md">
					<ul className="text-xs list-none pl-5">
						<li>
							State Street Market in Los Altos, CA
							<a className="block text-blue-600 dark:text-blue-400" href="#">
								Source URL
							</a>
						</li>
						<li>
							State Street Market in Los Altos, CA
							<a className="block text-blue-600 dark:text-blue-400" href="#">
								Source URL
							</a>
						</li>
						<li>
							State Street Market in Los Altos, CA
							<a className="block text-blue-600 dark:text-blue-400" href="#">
								Source URL
							</a>
						</li>
					</ul>
				</div>
			</div>
		</div>
	)
}

