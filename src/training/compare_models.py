import pandas as pd


def compare_models(results):

    comparison = pd.DataFrame(results)

    print("\n========== MODEL COMPARISON ==========")
    print(comparison)

    best_model = comparison.loc[
        comparison["Accuracy"].idxmax()
    ]

    print("\n========== BEST MODEL ==========")
    print(best_model)

    return comparison