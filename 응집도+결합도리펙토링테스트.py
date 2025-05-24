# 두 코드의 응집도/결합도 요소를 수치화하고 비교하는 분석기
# 기준: 클래스 수, 인터페이스 존재 여부, 의존 방향, 책임 수(간이 측정)
import ast
from collections import defaultdict
import pandas as pd
import matplotlib.pyplot as plt

# 분석 함수
def analyze_code(code: str, name: str):
    tree = ast.parse(code)
    method_field_usage = defaultdict(set)

    result = {
        "source": name,
        "class_count": 0,
        "method_total": 0,
        "interface_used": False,
        "explicit_dependency": 0,
        "cohesion_score": 0.0,
        "coupling_score": 0.0,
    }

    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            result["class_count"] += 1
            for item in node.body:
                if isinstance(item, ast.FunctionDef):
                    result["method_total"] += 1
                    for sub in ast.walk(item):
                        if isinstance(sub, ast.Attribute) and isinstance(sub.value, ast.Name) and sub.value.id == "self":
                            method_field_usage[item.name].add(sub.attr)
        if isinstance(node, ast.ClassDef) and node.name == "ProductStoreInterface":
            result["interface_used"] = True
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            if node.func.id in ["ProductRepository", "WebApp"]:
                result["explicit_dependency"] += 1

    # 응집도 계산
    shared = 0
    keys = list(method_field_usage.keys())
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            if method_field_usage[keys[i]] & method_field_usage[keys[j]]:
                shared += 1
    total_pairs = len(keys) * (len(keys) - 1) / 2
    result["cohesion_score"] = round((shared / total_pairs * 10), 2) if total_pairs else 10

    # 결합도 점수 (낮을수록 좋으므로 점수는 높게 부여)
    raw_coupling = result["explicit_dependency"] - (1 if result["interface_used"] else 0)
    result["coupling_score"] = max(0, 10 - raw_coupling * 2)

    return result

# 코드 문자열 예시
improved_code = """
class Product:
    def __init__(self, id, name): self.id = id; self.name = name
    def show(self): print(self.id, self.name)

class Repo:
    def __init__(self): self.items = []
    def add(self, p): self.items.append(p)
    def find(self, keyword): return [x for x in self.items if keyword in x.name]

class ProductStoreInterface: ...
class App:
    def __init__(self, store): self.store = store
    def search(self): return self.store.find("test")
"""

original_code = """
class Product:
    def __init__(self, id, name): self.id = id; self.name = name
    def show(self): print(self.id, self.name)

class Repo:
    def __init__(self): self.items = []
    def add(self, p): self.items.append(p)
    def find(self, keyword): return [x for x in self.items if keyword in x.name]

class App:
    def __init__(self): self.store = Repo()
    def search(self): return self.store.find("test")
"""

# 분석 실행
result_improved = analyze_code(improved_code, "개선 구조")
result_original = analyze_code(original_code, "기존 구조")

# 데이터프레임으로 정리
df = pd.DataFrame([result_improved, result_original])
print(df[["source", "cohesion_score", "coupling_score"]])

# 시각화
labels = ["Cohesion Score", "Coupling Score"]
modular_values = [result_improved["cohesion_score"], result_improved["coupling_score"]]
original_values = [result_original["cohesion_score"], result_original["coupling_score"]]

x = range(len(labels))
width = 0.35

fig, ax = plt.subplots(figsize=(8, 5))
ax.bar([i - width/2 for i in x], modular_values, width=width, label="Improved Structure", color="mediumseagreen")
ax.bar([i + width/2 for i in x], original_values, width=width, label="Original Structure", color="salmon")

ax.set_ylabel("Score (0–10)")
ax.set_title("Comparison of Cohesion and Coupling Scores")
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylim(0, 12)
ax.legend()
ax.grid(True, axis="y", linestyle="--", alpha=0.7)

plt.tight_layout()
plt.show()
