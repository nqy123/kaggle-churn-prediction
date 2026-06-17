"""模型训练与预测入口。"""

from pathlib import Path

import pandas as pd

from feature import build_features
from utils import DATA_DIR, ensure_output_dir


def main() -> None:
    """加载数据、训练模型并生成提交文件。"""
    train_path = DATA_DIR / "train.csv"
    test_path = DATA_DIR / "test.csv"

    if not train_path.exists() or not test_path.exists():
        raise FileNotFoundError(
            "请先将 train.csv 和 test.csv 放入 data/ 目录。"
        )

    train_df = pd.read_csv(train_path)
    test_df = pd.read_csv(test_path)

    # TODO: 根据竞赛数据确定目标列名称
    # target_col = "Churn"
    # X_train = build_features(train_df.drop(columns=[target_col]))
    # y_train = train_df[target_col]
    # X_test = build_features(test_df)

    output_dir = ensure_output_dir()
    print(f"数据加载完成。训练集: {train_df.shape}, 测试集: {test_df.shape}")
    print(f"输出目录: {output_dir}")
    print("请在完成特征工程和模型训练后，将预测结果保存至 outputs/")


if __name__ == "__main__":
    main()
