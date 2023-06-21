import pandas as pd  # Using pandas for their dataframe
import numpy as np  # Used once
from altair import Chart, Color, Scale  # Chart: display chart on application
# Color: prepares the gradient we give later,
from pandas.core.frame import DataFrame

def chart(df: DataFrame, x: str, y: str, target: str) -> Chart:
    # taking the 3 arguments the user determines
    Number_type_data = pd.DataFrame({
        x: df[x],  # What ever the USER causes x to be from the list of 5 choices (updates)
        y: df[y],  # What ever the USER causes y to be from the list of 5 choices (updates)
        target: np.random.choice(["Level", "Health", "Energy", "Sanity", "Rarity"], len(df))
        # target has 5 numerical monster qualities
    })
    chart_title = f"{x} by {y} for {target}"  # The user decides what's x and y
    chart = Chart(Number_type_data).mark_point(opacity=0.12).encode(  # You can see how the
        # monsters qualities are dispersed with opacity showing how intense the monsters
        # may be grouped underneath
        x=x,  # user's choice
        y=y,  # also user decides this in application
        color=Color(x, scale=Scale(scheme='rainbow'))  # Rainbow gradient is for chart appeal
    )
    chart_title_text = f'{chart_title}'
    chart_with_title = chart.properties(title=chart_title_text)
    chart_with_title.properties(title=chart_title)

    return chart_with_title

#  What were the deliverables for your ticket?
#  What requirements did you have to keep in mind? Think tech stack, constraints, etc.
#  How did you go about shipping your ticket?
#  Why did you take the approach you took?
