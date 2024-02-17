from uagents import Agent, Context, Bureau

agent_multiply = Agent(name="multiply", seed="_multiply_recovery")
agent_base = Agent(name="base", seed="_base_recovery")


@agent_base.on_event("startup")
async def startup(ctx: Context):
    ctx.logger.info("Agent base started")


@agent_multiply.on_event("startup")
async def startup(ctx: Context):
    ctx.logger.info("Agent multiply started")


if __name__ == "__main__":
    bureau = Bureau()
    bureau.add(agent_base)
    bureau.add(agent_multiply)
    bureau.run()
