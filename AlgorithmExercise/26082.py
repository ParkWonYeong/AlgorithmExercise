## WARBOY
# WARBOY 가격 대비 성능이 경쟁사 제품의 3배. (가격 대비 성능 = 성능 / 가격)
# 경쟁사 제품의 가격 A, 경쟁사 제품의 성능 B, WARBOY의 가격 C.
# WARBOY의 성능은?

import sys
si = sys.stdin.readline

A,B,C = map(int, si().split())
print((B//A)*3*C) 