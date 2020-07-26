import pandas as pd

students = pd.read_excel('/Users/Apple/Desktop/pandas/join.xlsx',
                         sheet_name='stu', dtype={'stu_id': str})
scores = pd.read_excel('/Users/Apple/Desktop/pandas/join.xlsx',
                       sheet_name='score', dtype={'stu_id': str})

datas = students.merge(scores, how='inner', on='stu_id')


# 校验其中某一列

# 定义一个校验函数
def score_validation(row):
    try:
        assert 0 <= row.score <= 100
    except:
        print(f"#{row.stu_id} student {row['name']} has invalid score {row.score}")


datas.apply(score_validation, axis=1)
