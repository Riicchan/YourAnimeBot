from discord.ext import commands

from helpers import anime_helper, general_helper
import config

class AnimeModule(commands.Cog):

    @commands.command(name="quote", description="Returns a random anime quote")
    @commands.cooldown(rate=5, per=30*60, type=commands.BucketType.user)
    async def anime_quote(self, ctx:commands.Context):
        reply = await anime_helper.get_random_anime_quote_embed()

        await ctx.send(embed=reply)

    @commands.command(name="suggest", aliases=["recommend"], description="Recommends an anime similar to the provided anime")
    @general_helper.short_cooldown()
    async def suggest_anime(self, ctx:commands.Context, *anime):
        
        anime = " ".join(anime)

        async def reply_callback():
            media_id = anime_list[paginator.current_page].media_id

            anime_scroller = await anime_helper.get_similar_anime(media_id)

            if anime_scroller is not None:
                return anime_scroller
            else:
                return await general_helper.get_information_embed(
                        title="Whoops",
                        description="No recommendations were found for this anime",
                        color=config.ERROR_COLOR
                    )

<<<<<<< HEAD
<<<<<<< HEAD
        response = await general_helper.get_media_selection_paginator(anime, reply_callback)
=======
        response = await general_helper.get_anime_selection_paginator(anime, reply_callback)
>>>>>>> bbd2353 (MODIFY : Better Selection Screen)
=======
        response = await general_helper.get_media_selection_paginator(anime, reply_callback)
>>>>>>> bb4ee89 (ADD : Add mangas to lists)

        paginator = response.paginator
        anime_list = response.media

        if response.length() > 0:
            await paginator.send(ctx)
        else:
            await ctx.reply(embed=await response.get_error_embed())


def setup(bot):
    bot.add_cog(AnimeModule())