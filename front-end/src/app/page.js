'use client'

import { useQuery } from 'convex/react';
import { api } from '@/../convex/_generated/api';

export default function Home() {

  const halls = useQuery(api.findings.get);

  return (
    <main class="flex flex-col justify-center items-center min-h-screen w-full">
      {
        halls == undefined ? <span>Loading...</span> :
          halls.map(({ _id, name }) => {
            return (
              <span id={_id} class="text-4xl font-bold border">{name}</span>
            )
          })
      }
    </main>
  );
}
