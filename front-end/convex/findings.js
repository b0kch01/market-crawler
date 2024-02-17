import { query } from "./_generated/server"
import { v } from "convex/values"

export const get = query({
  handler: async (ctx) => {
    return await ctx.db.query("food_halls").collect()
  }
})