import { query } from "./_generated/server"

export const getAll = query({
  handler: async (ctx) => {
    return await ctx.db
      .query("food_halls")
      .order("desc")
      .collect()
  }
})