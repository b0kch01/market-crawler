'use client'

import { useQuery } from 'convex/react';
import { api } from '@/../convex/_generated/api';

export default function Home() {

  const halls = useQuery(api.findings.getAll);

  return (
    <main className="flex flex-col justify-center items-center min-h-screen w-full">
      {
        halls == undefined ? <span>Loading...</span> :
          halls.map((obj) => {
            return (
              <span key={obj._id} className="flex gap-4 border">
                {
                  Object.keys(obj).map((key) => {
                    return (
                      <span key={key} className="flex flex-col">
                        <span>{key}</span>
                        <span>{`${obj[key]}`}</span>
                      </span>
                    )
                  })
                }
              </span>
            )
          })
      }
    </main>
  );
}
