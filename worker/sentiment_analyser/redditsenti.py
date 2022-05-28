import cohere
from cohere.classify import Example

co = cohere.Client('wyQMKZSy0o3OGx3B3LT8qXDXhQiTDCWPTWQvZLzf')

# its the titles for the posts 

# we need more examples for positive and neutral
classifications = co.classify(
  model='medium',
  taskDescription='Classify these as positive, negative',
  outputIndicator='Classify this stock',
  inputs=["Why doesn't TSLA get included as part of mega caps, at 10x value of NFLX and almost twice the value of FB?", "The Nasdaq fell 2.5% today, while TSLA fell 8%."],
  examples=[
    Example("More Room For Growth In Pioneer Energy Stock?", "positive"),
    Example("After Dismal Performance Last Month, L'Oreal Stock Looks Set To Rebound", "positive"),
    Example("The stock market is close to finding its bottom as corporate share buybacks surge to record highs, JPMorgan says", "positive"),
    Example("How Do You Stay Confident in a Market Crash?", "negative"),
    Example("Here's 1 of the Biggest Problems With Airbnb Stock", "negative"),
    Example("GameStop Unveils Crypto and NFT Wallet, Shares up 3%", "positive"),
    Example("Should You Buy Stocks With An Impending Bear Market And Possible Recession?", "negative"),
    Example("Costco Q3 Earnings Preview: Don't Fall With It Any Longer (NASDAQ:COST)", "negative"),
    Example("Bear Market Has Only Just Begun", "negative"),
    Example("Photronics stock gains on guiding FQ3 above consensus after FQ2 beat (NASDAQ:PLAB)", "positive"),
    Example("Texas Instruments Stock: Playing The Long Game; Buy Now (NASDAQ:TXN)", "positive"),
    Example("U.S.-NEW YORK-STOCK MARKET-RISE", "positive"),
    Example("Chart Check: Record high in sight! This stock from agrochemical space is a good buy on dips bet", "positive"),
    Example("MSCI Inc. stock rises Wednesday, still underperforms market", "negative"),
    Example("DraftKings Inc. stock rises Wednesday, outperforms market", "positive"),
    Example("Willis Towers Watson PLC stock falls Tuesday, still outperforms market", "positive"),
    Example("ONEOK Inc. stock rises Tuesday, outperforms market", "positive"),
    Example("Marathon Oil Corp. stock falls Tuesday, still outperforms market", "positive"),
    Example("Intuitive Surgical Inc. stock falls Tuesday, underperforms market", "negative"),
    Example("Kohl's Corp. stock falls Monday, underperforms market", "negative"),
    Example("Intuit Inc. stock rises Monday, still underperforms market", "negative"),
    Example("Dow Inc. stock falls Monday, underperforms market", "negative"),
    Example("Walgreens Boots Alliance Inc. stock rises Thursday, still underperforms market", "negative"),
    Example("Waste Management Inc. stock rises Thursday, still underperforms market", "negative"),
    Example("Teleflex Inc. stock rises Thursday, still underperforms market", "negative"),
    Example("Public Storage stock rises Thursday, still underperforms market", "negative"),
    Example("Kohl's Corp. stock rises Thursday, outperforms market", "positive"),
    Example("Johnson Controls International PLC stock rises Thursday, outperforms market", "positive"),
    Example("Regency Centers Corp. stock rises Friday, outperforms market", "positive"),
    Example("Snap-On Inc. stock rises Friday, still underperforms market", "negative"),
    Example("Cooper Cos. stock rises Friday, still underperforms market", "negative"),
    Example("Unum Group stock rises Wednesday, still underperforms market", "negative"),
    Example("United Rentals Inc. stock rises Wednesday, outperforms market", "positive"),
    Example("Target Corp. stock outperforms market on strong trading day", "positive"),
    Example("Snap Inc. stock rises Wednesday, outperforms market", "positive"),
    Example("Paramount Global Cl B stock outperforms market on strong trading day", "positive"),
    Example("Live Nation Entertainment Inc. stock rises Wednesday, outperforms market", "positive"),
    Example("International Flavors & Fragrances Inc. stock rises Wednesday, still underperforms market", "negative"),
    Example('The Nasdaq fell 2.5% today, while TSLA fell 8%', 'negative')
])



print('The confidence levels of the labels are: {}'.format(
       classifications.classifications))