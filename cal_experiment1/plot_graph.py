import matplotlib.pyplot as plt
from chord_method import chord, f as f_chord, g
from newton_method import newton, f as f_newton, df
from dichotomy_method import dichotomy, f as f_dichotomy

# 使用弦截法找到根
root_chord, x_values_chord, error_values_chord = chord(f_chord, g, 0.1, 0.9, tol=1e-4, max_iter=100)

# 使用牛顿法找到根
root_newton, x_values_newton, error_values_newton = newton(f_newton, df, 1, tol=1e-4, max_iter=100)

# 使用二分法找到根
root_dichotomy, x_values_dichotomy, error_values_dichotomy = dichotomy(f_dichotomy, 0, 1, tol=1e-4, max_iter=100)

# 创建图形对象并设置图形大小
plt.figure(figsize=(18, 6))

# 绘制弦截法的迭代过程
plt.subplot(1, 3, 1)
plt.plot(x_values_chord, marker='o', color='b', label='Chord Method')
plt.xlabel('Iteration')
plt.ylabel('x_new')
plt.title('Iteration vs. x_new (Chord Method)')
plt.xticks(range(0, len(x_values_chord), 1))  # 设置迭代次数的刻度间隔为1
plt.legend()  # 添加图例

plt.subplot(1, 3, 2)
plt.plot(error_values_chord, marker='o', color='r', label='Chord Method')
plt.xlabel('Iteration')
plt.ylabel('Error')
plt.title('Iteration vs. Error (Chord Method)')
plt.xticks(range(0, len(error_values_chord), 1))  # 设置迭代次数的刻度间隔为1
plt.legend()  # 添加图例

# 绘制牛顿法的迭代过程
plt.subplot(1, 3, 1)
plt.plot(x_values_newton, marker='x', color='g', label='Newton Method')
plt.xlabel('Iteration')
plt.ylabel('x_new')
plt.title('Iteration vs. x_new (Both Methods)')
plt.xticks(range(0, len(x_values_newton), 1))  # 设置迭代次数的刻度间隔为1
plt.legend()  # 添加图例

plt.subplot(1, 3, 2)
plt.plot(error_values_newton, marker='x', color='m', label='Newton Method')
plt.xlabel('Iteration')
plt.ylabel('Error')
plt.title('Iteration vs. Error (Both Methods)')
plt.xticks(range(0, len(error_values_newton), 1))  # 设置迭代次数的刻度间隔为1
plt.legend()  # 添加图例

# 绘制二分法的迭代过程
plt.subplot(1, 3, 3)
plt.plot(x_values_dichotomy, marker='s', color='y', label='Dichotomy Method')
plt.xlabel('Iteration')
plt.ylabel('x_new')
plt.title('Iteration vs. x_new (Dichotomy Method)')
plt.xticks(range(0, len(x_values_dichotomy), 1))  # 设置迭代次数的刻度间隔为1
plt.legend()  # 添加图例

plt.tight_layout()  # 调整子图之间的间距
plt.show()  # 显示图形

print("Root found (Chord Method):", root_chord)
print("Root found (Newton Method):", root_newton)
print("Root found (Dichotomy Method):", root_dichotomy)
