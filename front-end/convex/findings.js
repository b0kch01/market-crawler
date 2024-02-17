import { query } from "./_generated/server"
import { v } from "convex/values"

export const get = query({
  args: { _id: v.id("food_halls"), name: v.string() },
  handler: async (ctx) => {
    console.log(ctx.db)
    return await ctx.db.query("food_halls").collect()
  }
})