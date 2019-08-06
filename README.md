# Understanding Fantasy Basketball with Game Theory
## Setting Up The Rules Of The Game:
Although it's not as popular as Fantasy Football, Fantasy Basketball is an engaging game for fans to play during the NBA season. Fantasy sports use a real sport as a data source (for basketball this means how many points, assists, steals, turnovers etc. are accumulated). The following is a white paper of sorts. It is the first attempt I'm aware of that uses Blotto games as a model for Fantasy Basketball as well as the first attempt I'm aware of finding a dominant Blotto strategy by facing random strategies. https://www.semanticscholar.org/paper/%E2%80%9C-Solving-%E2%80%9D-the-Blotto-Game-%3A-A-Computational-Wittman/241ba18a3819a3341ef091eb99b10dc510f28ef0 this paper compares a selection of pre-defined strategies.

At the start of the season, each person in a fantasy league picks a team (called drafting). Picking good players at the start is incredibly important for doing well during the season because the players available mid-season are not very good. Each week during the season, our team goes up against another team in our league in a head-to-head matchup. The winner of this head-to-head matchup is whichever team wins the most number of statistical categories. In a 9 category league, you need to win at least 5 categories to win that week. Those categories are Points, Rebounds, Blocks, Assists, Steals, Turnovers (lower is better), 3-point shots made (3PM), Free Throw % (higher is better), and Field Goal % (higher is better). The more games you win, the higher seeded you are for the playoffs (and the easier your fantasy championship run is).
 
## Understanding Relative Player Value

Good NBA players help you win by contributing to each of the statistical categories (in various amounts). We need to develop a way to evaluate how good each player is for their position, and for all players before the season starts so that we can plan our draft.

The first step is either creating player statistical projections with machine learning or using other projections (for the upcoming season). For example basketball-reference's projection system: https://www.basketball-reference.com/friv/projections.cgi

The next step is turning the raw statistics into something comparable across categories. We can do this by figuring out the standard deviation of each category. A general but good metric for how much a player contributes to your team over the course of a season is to sum the standard deviations of all categories. Free Throw % and Field Goal % are more tricky because players who shoot a lot of free throws or who shoot a lot of field goals have a much larger impact on our weekly team %, so you need to scale those categories appropriately.

There's one more element crutical for winnning the game: picking the right distribution.

A common strategy in fantasy basketball is called “punting” and it means to intentionally draft players who are bad at one or two categories in order to strenghen the rest of your categories. The idea is that because you only need to win five out of the nine categories to win a match, you should concentrate your player values. It is essentially letting your opponent try to win every category and concentrating on your strongest categories.

But how can we evaluate if this is even a good strategy?

## Using Game Theory to Model the Situation:
We can use Game Theory to model this situation. A model in this context is just simplified version of reality that lets us. 

If we think about player value being Colonel Blotto game, we can simulate a bunch of games against other strategies and try to find the best distribution for our model. 

The setup of a Blotto game is simple: two colonels are fighting a war with equal sized armies. But each of those armies has to be split across different areas called “battlefields”. For example each colonel has 100 troops distributed across 5 battlefields. If a colonel has more troops on a battlefield than the other colonel, that colonel wins that battlefield with their size majority, and if they win more battlefields than the other colonel they win the war. For example, if colonel 1 had 10 troops deployed across battlefields 1-5 as [1, 2, 4, 2, 1] against colonel 2’s troop distribution of [2, 0, 0, 3, 5]: 1<2, 2>0, 4>0, 2<3, 1<5, so colonel 2 wins 3 battlefields and colonel 1’s only wins 2 battlefields, so colonel 2 wins the war. In a more visually understandable way:
  ```
  [1] < [2]
  [2] > [0]
  [4] > [0]
  [2] < [3]
  [1] < [5]
  
  Total:
  2 > 3
  ```
This theoretical game has no dominant strategy, because if a colonel adjusts their troops before battle, there will always be a strategy that the opposing colonel can change to that will beat them. Almost every strategy has a situation where except for a strategy that puts 0 troops into more than half the number of battlefields e.g. [10, 0, 0, 0, 0] or [0, 0, 0, 5, 5] because those will always lose. Assuming no prior information about the opposing colonel’s choices, there isn’t a dominant strategy.

## Solving using Monte Carlo Simulation:
We can use 

Summary: I used Blotto games and a Monte Carlo algorithm to optimize fantasy basketball strategy. You can find an interactive version of my code here: 
https://colab.research.google.com/drive/1LsDSJjSjAm6-GpNWeZaUOzb9emaiseXA


## Big Takeaway
All else being equal, having your players' categorical strengths spread across all your categories is better than having them concentrated in only some categories.

## Further Work
Future work could use reinforcment learning to create a drafting bot and optimize based on who other players in the pool (and projections). In addition, a more detailed model could take the NBA schedule into account and optimize futher based on that.
