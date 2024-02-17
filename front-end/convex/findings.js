import { query } from "./_generated/server"

export const get = query({
  args: {},
  handler: async (ctx) => {
    console.log(ctx.db)
    return await ctx.db.query("food_halls").collect()
  }
})