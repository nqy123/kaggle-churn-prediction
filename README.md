# Kaggle 客户流失预测项目

这是一个 Kaggle 客户流失预测项目，目标是根据用户特征预测二分类目标 `Churn`。

当前项目已经完成 baseline、特征工程、三模型融合、Optuna 调参、多 seed 训练和若干融合实验。经过线上提交验证后，最终保留当前表现最好的版本：

`outputs/submission_xgb_optuna50_multiseed.csv`

## 当前最佳结果

| 项目 | 内容 |
|---|---|
| 最佳模型 | XGBoost Optuna50 MultiSeed |
| 特征版本 | FE |
| 目标列 | `Churn` |
| ID 列 | `id` |
| OOF AUC | `0.917168` |
| 最佳提交文件 | `outputs/submission_xgb_optuna50_multiseed.csv` |
| 说明 | 使用 XGBoost Optuna 50 trials 的最佳参数，并进行 7 seeds 平均 |

## 最终保留文件

```text
kaggle_churn_project/
├── data/
│   ├── train.csv
│   ├── test.csv
│   └── sample_submission.csv
├── notebooks/
│   └── baseline.ipynb
├── outputs/
│   ├── oof_xgb_optuna50_multiseed.csv
│   ├── pred_xgb_optuna50_multiseed.csv
│   ├── submission_xgb_optuna50_multiseed.csv
│   ├── experiment_log.csv
│   └── best_result_summary.csv
├── src/
│   ├── feature.py
│   ├── train.py
│   └── utils.py
├── README.md
└── requirements.txt
```

## 输出文件说明

| 文件 | 说明 |
|---|---|
| `outputs/oof_xgb_optuna50_multiseed.csv` | 最佳模型在训练集上的 OOF 预测 |
| `outputs/pred_xgb_optuna50_multiseed.csv` | 最佳模型在测试集上的预测 |
| `outputs/submission_xgb_optuna50_multiseed.csv` | 当前最佳 Kaggle 提交文件 |
| `outputs/experiment_log.csv` | 当前保留实验的简要日志 |
| `outputs/best_result_summary.csv` | 当前最佳版本的结果检查摘要 |

## Submission 检查

当前最佳提交文件已检查：

| 检查项 | 结果 |
|---|---|
| 行数等于 `sample_submission.csv` | 通过 |
| 列名和顺序一致 | 通过 |
| 预测值在 `[0, 1]` | 通过 |
| 缺失值 | 0 |
| 无穷值 | 0 |
| 预测最小值 | `0.0000748893` |
| 预测最大值 | `0.9899883845` |
| 预测均值 | `0.2181675594` |
| 预测标准差 | `0.2761685134` |

## 复现实验

主要实验代码保留在：

`notebooks/baseline.ipynb`

该 notebook 中包含：

1. 数据读取与基础检查
2. CatBoost baseline
3. FE 特征工程版 CatBoost
4. 三模型融合
5. XGBoost Optuna
6. XGBoost Optuna MultiSeed
7. OOF 融合权重搜索
8. 后续极限压榨实验记录

## 当前结论

线上验证后，继续做 fine pseudo blend 没有带来提升，因此项目当前回到稳定最佳版本：

`outputs/submission_xgb_optuna50_multiseed.csv`

后续如果继续冲分，建议优先从新特征工程或更强的 XGBoost 参数空间入手，而不是继续微调现有融合权重。
