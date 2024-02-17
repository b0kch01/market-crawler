import { query } from "./_generated/server"
import { v } from "convex/values"

export const getAll = query({
  args: {},
  handler: async (ctx) => {
    return await ctx.db.query("food_halls").collect()
  }
})