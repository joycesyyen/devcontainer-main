import glob
import os
import pandas as pd

path = "/workspaces/devcontainer-main/res_gossiping"
file_type = "*.txt"
path_full = os.path.join(path, file_type)

columns = [
    "推",
    "噓",
    "分數",
    "作者",
    "標題",
    "時間"
]

# Define function
def get_text_file_path() -> list[str]:
    return glob.glob("workspaces/devcontainer-main/res_gossiping/*.txt")

def e_text_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
    
def t_text_to_df_row_list(article_string: str) ->list[str]:
    reply_info_string = article_string.split("---split---")[1]
    return reply_info_string.split("\n")[1:-1]

def t_combine_list_to df(reply_info_list: list[list]) -> pd.DataFrame:
    return.pd.DataFrame(
        data=reply_info_lists,
        columns=COLUMNS
    )

def l_df_to_csv(df:df: pd.DataFrame) -> None:
    df.to_csv("ptt2.csv", index=0)

if __name__ == "__main__":
    # Get paths of all text files
    pass

    # Loop for file paths
        # Extract text file

        # Text to list-element in DataFrame

        # Concat lists to DataFrame

    # Load DataFrame to CSV
