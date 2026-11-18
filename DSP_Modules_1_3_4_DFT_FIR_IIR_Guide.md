# DSP Exam-Only Preparation Guide: Modules 1, 3 & 4

---

## Part 1: Discrete Fourier Transform (DFT) & Fast Fourier Transform (FFT)

```
                            Discrete Fourier Transform (DFT)
                                          │
        ┌─────────────────────────────────┼─────────────────────────────────┐
        ▼                                 ▼                                 ▼
 Radix-2 FFT (DIT / DIF)       Block Filtering Methods           Circular Shift & Properties
  • Bit-reversal input/output   • Overlap-Add: sum overlaps       • Time-shift: phase factor W_N^(km)
  • N/2 log2(N) complex mults   • Overlap-Save: discard M-1       • Circular convolution via DFT
```

---

### Topic 1.1: Fast Fourier Transforms (FFT) — Radix-2 DIT & DIF Algorithms

#### Core Formulas & Butterfly Equations
* **Twiddle Factor**: $W_N^k = e^{-j \frac{2\pi k}{N}} = \cos\left(\frac{2\pi k}{N}\right) - j \sin\left(\frac{2\pi k}{N}\right)$
* **Computational Complexity**:
  * Direct DFT: $N^2$ complex multiplications, $N(N-1)$ complex additions.
  * Radix-2 FFT: $\frac{N}{2}\log_2 N$ complex multiplications, $N\log_2 N$ complex additions.
  * For $N=8$: FFT requires $\frac{8}{2}(3) = 12$ complex multiplications vs. $8^2 = 64$ for direct DFT (an 81.25% reduction).
* **Decimation-in-Time (DIT)**: Bit-reversed input, normal order output.
  * Butterfly: $X_m(p) = X_{m-1}(p) + W_N^r X_{m-1}(q)$, $\quad X_m(q) = X_{m-1}(p) - W_N^r X_{m-1}(q)$
* **Decimation-in-Frequency (DIF)**: Normal order input, bit-reversed output.
  * Butterfly: $X_m(p) = X_{m-1}(p) + X_{m-1}(q)$, $\quad X_m(q) = [X_{m-1}(p) - X_{m-1}(q)] W_N^r$

---

#### Question 1.1.1 (Dec 2025 — Final Exam)
> **Question:** Find the 8-point DFT of $x(n) = \{1, 2, 3, 4, 5, 0, 0, 0\}$ by Radix-2 DIT-FFT or DIF-FFT algorithm.  
> **Exam:** Final Examination (2025–2026), Dec 2025 | **Marks:** 8 Marks  
> **Official Solution Link:** [ANS-Sem-V-EXTC-Digital Signal Processing.pdf](./ANS-Sem-V-EXTC-Digital%20Signal%20Processing.pdf#page=1)

**Step-by-Step Mathematical Solution (Radix-2 DIT-FFT):**

1. **Bit Reversal of Input Sequence ($N=8$):**
   * $n = 0 \ (000_2) \to 000_2 = 0 \implies x(0) = 1$
   * $n = 1 \ (001_2) \to 100_2 = 4 \implies x(4) = 5$
   * $n = 2 \ (010_2) \to 010_2 = 2 \implies x(2) = 3$
   * $n = 3 \ (011_2) \to 110_2 = 6 \implies x(6) = 0$
   * $n = 4 \ (100_2) \to 001_2 = 1 \implies x(1) = 2$
   * $n = 5 \ (101_2) \to 101_2 = 5 \implies x(5) = 0$
   * $n = 6 \ (110_2) \to 011_2 = 3 \implies x(3) = 4$
   * $n = 7 \ (111_2) \to 111_2 = 7 \implies x(7) = 0$

2. **Stage 1 Computations ($W_8^0 = 1$):**
   * $v_0 = x(0) + W_8^0 x(4) = 1 + 5 = 6$
   * $v_1 = x(0) - W_8^0 x(4) = 1 - 5 = -4$
   * $v_2 = x(2) + W_8^0 x(6) = 3 + 0 = 3$
   * $v_3 = x(2) - W_8^0 x(6) = 3 - 0 = 3$
   * $v_4 = x(1) + W_8^0 x(5) = 2 + 0 = 2$
   * $v_5 = x(1) - W_8^0 x(5) = 2 - 0 = 2$
   * $v_6 = x(3) + W_8^0 x(7) = 4 + 0 = 4$
   * $v_7 = x(3) - W_8^0 x(7) = 4 - 0 = 4$

3. **Stage 2 Computations ($W_8^0 = 1, W_8^2 = -j$):**
   * $u_0 = v_0 + W_8^0 v_2 = 6 + 3 = 9$
   * $u_1 = v_1 + W_8^2 v_3 = -4 + (-j)(3) = -4 - 3j$
   * $u_2 = v_0 - W_8^0 v_2 = 6 - 3 = 3$
   * $u_3 = v_1 - W_8^2 v_3 = -4 - (-j)(3) = -4 + 3j$
   * $u_4 = v_4 + W_8^0 v_6 = 2 + 4 = 6$
   * $u_5 = v_5 + W_8^2 v_7 = 2 + (-j)(4) = 2 - 4j$
   * $u_6 = v_4 - W_8^0 v_6 = 2 - 4 = -2$
   * $u_7 = v_5 - W_8^2 v_7 = 2 - (-j)(4) = 2 + 4j$

4. **Stage 3 Computations ($W_8^0 = 1, W_8^1 = \frac{1-j}{\sqrt{2}} \approx 0.7071 - 0.7071j, W_8^2 = -j, W_8^3 = \frac{-1-j}{\sqrt{2}} \approx -0.7071 - 0.7071j$):**
   * $X(0) = u_0 + W_8^0 u_4 = 9 + 6 = 15$
   * $X(1) = u_1 + W_8^1 u_5 = (-4 - 3j) + (0.7071 - 0.7071j)(2 - 4j)$
     $$(0.7071 - 0.7071j)(2 - 4j) = 0.7071 [2 - 4j - 2j - 4] = 0.7071(-2 - 6j) = -1.4142 - 4.2426j$$
     $$X(1) = (-4 - 3j) + (-1.4142 - 4.2426j) = -5.4142 - 7.2426j$$
   * $X(2) = u_2 + W_8^2 u_6 = 3 + (-j)(-2) = 3 + 2j$
   * $X(3) = u_3 + W_8^3 u_7 = (-4 + 3j) + (-0.7071 - 0.7071j)(2 + 4j)$
     $$(-0.7071 - 0.7071j)(2 + 4j) = -0.7071 [2 + 4j + 2j - 4] = -0.7071(-2 + 6j) = 1.4142 - 4.2426j$$
     $$X(3) = (-4 + 3j) + (1.4142 - 4.2426j) = -2.5858 - 1.2426j$$
   * $X(4) = u_0 - W_8^0 u_4 = 9 - 6 = 3$
   * $X(5) = u_1 - W_8^1 u_5 = (-4 - 3j) - (-1.4142 - 4.2426j) = -2.5858 + 1.2426j = X^*(3)$
   * $X(6) = u_2 - W_8^2 u_6 = 3 - 2j = X^*(2)$
   * $X(7) = u_3 - W_8^3 u_7 = (-4 + 3j) - (1.4142 - 4.2426j) = -5.4142 + 7.2426j = X^*(1)$

**Final Answer:**
$$X(k) = \{15, \ -5.414 - 7.243j, \ 3 + 2j, \ -2.586 - 1.243j, \ 3, \ -2.586 + 1.243j, \ 3 - 2j, \ -5.414 + 7.243j\}$$

---

#### Question 1.1.2 (March 2026 — Re-Exam)
> **Question:** Find the 8-point DFT of $x(n) = \{1, 0, 2, 0, 3, 0, 4, 0\}$ by Radix-2 DIF-FFT algorithm.  
> **Exam:** Re-Examination (2025–2026), March 2026 | **Marks:** 8 Marks  
> **Official Solution Link:** [ANS_Re-Exam_Digital Signal Processing_2025-2026.pdf](./Sem-V%20QP%20Misc/sem%205%20last%20year%20reexam/Digital%20Signal%20Processing/ANS_Re-Exam_Digital%20Signal%20Processing%28DJS23ECPC501%29_Semester%20V_2025-2026.pdf#page=1)

**Step-by-Step Mathematical Solution (Radix-2 DIF-FFT):**

1. **Input in Normal Order ($N=8$):**
   $$x(n) = [x(0), x(1), x(2), x(3), x(4), x(5), x(6), x(7)] = [1, 0, 2, 0, 3, 0, 4, 0]$$

2. **Stage 1 (Pairing elements spaced by $N/2 = 4$):**
   * Upper half: $a_n = x(n) + x(n+4)$
     * $a_0 = x(0) + x(4) = 1 + 3 = 4$
     * $a_1 = x(1) + x(5) = 0 + 0 = 0$
     * $a_2 = x(2) + x(6) = 2 + 4 = 6$
     * $a_3 = x(3) + x(7) = 0 + 0 = 0$
   * Lower half: $b_n = [x(n) - x(n+4)] W_8^n$
     * $b_0 = [x(0) - x(4)] W_8^0 = (1 - 3)(1) = -2$
     * $b_1 = [x(1) - x(5)] W_8^1 = (0 - 0) W_8^1 = 0$
     * $b_2 = [x(2) - x(6)] W_8^2 = (2 - 4)(-j) = 2j$
     * $b_3 = [x(3) - x(7)] W_8^3 = (0 - 0) W_8^3 = 0$

3. **Stage 2 (Pairing elements spaced by $N/4 = 2$):**
   * Top branch (from $a_n$):
     * $c_0 = a_0 + a_2 = 4 + 6 = 10$
     * $c_1 = a_1 + a_3 = 0 + 0 = 0$
     * $c_2 = [a_0 - a_2] W_8^0 = (4 - 6)(1) = -2$
     * $c_3 = [a_1 - a_3] W_8^2 = (0 - 0)(-j) = 0$
   * Bottom branch (from $b_n$):
     * $d_0 = b_0 + b_2 = -2 + 2j$
     * $d_1 = b_1 + b_3 = 0 + 0 = 0$
     * $d_2 = [b_0 - b_2] W_8^0 = (-2 - 2j)(1) = -2 - 2j$
     * $d_3 = [b_1 - b_3] W_8^2 = (0 - 0)(-j) = 0$

4. **Stage 3 (Pairing adjacent elements spaced by 1):**
   * From $c_n$:
     * $X(0) = c_0 + c_1 = 10 + 0 = 10$
     * $X(4) = c_0 - c_1 = 10 - 0 = 10$
     * $X(2) = c_2 + c_3 = -2 + 0 = -2$
     * $X(6) = c_2 - c_3 = -2 - 0 = -2$
   * From $d_n$:
     * $X(1) = d_0 + d_1 = -2 + 2j$
     * $X(5) = d_0 - d_1 = -2 + 2j$
     * $X(3) = d_2 + d_3 = -2 - 2j$
     * $X(7) = d_2 - d_3 = -2 - 2j$

5. **Bit-Reversal Permutation to Natural Frequency Order:**
   * $X(0) = 10$
   * $X(1) = -2 + 2j$
   * $X(2) = -2$
   * $X(3) = -2 - 2j$
   * $X(4) = 10$
   * $X(5) = -2 + 2j$
   * $X(6) = -2$
   * $X(7) = -2 - 2j$

**Final Answer:**
$$X(k) = \{10, \ -2 + 2j, \ -2, \ -2 - 2j, \ 10, \ -2 + 2j, \ -2, \ -2 - 2j\}$$

---

#### Question 1.1.3 (TT1 — Term Test I)
> **Question:** Compute the 4-point DFT of the complex sequence $x(n) = \{1+3j, -2-5j, 2+3j, 5-4j\}$ using the Radix-2 DIT-FFT algorithm.  
> **Exam:** Term Test I (31/08/2026) | **Marks:** 5 Marks

**Step-by-Step Mathematical Solution:**

1. **Bit Reversal ($N=4$):**
   * $x(0) = 1 + 3j$
   * $x(2) = 2 + 3j$
   * $x(1) = -2 - 5j$
   * $x(3) = 5 - 4j$

2. **Stage 1 ($W_4^0 = 1$):**
   * $v_0 = x(0) + x(2) = (1 + 3j) + (2 + 3j) = 3 + 6j$
   * $v_1 = x(0) - x(2) = (1 + 3j) - (2 + 3j) = -1 + 0j = -1$
   * $v_2 = x(1) + x(3) = (-2 - 5j) + (5 - 4j) = 3 - 9j$
   * $v_3 = x(1) - x(3) = (-2 - 5j) - (5 - 4j) = -7 - j$

3. **Stage 2 ($W_4^0 = 1, W_4^1 = -j$):**
   * $X(0) = v_0 + W_4^0 v_2 = (3 + 6j) + (3 - 9j) = 6 - 3j$
   * $X(1) = v_1 + W_4^1 v_3 = -1 + (-j)(-7 - j) = -1 + (7j - 1) = -2 + 7j$
   * $X(2) = v_0 - W_4^0 v_2 = (3 + 6j) - (3 - 9j) = 0 + 15j = 15j$
   * $X(3) = v_1 - W_4^1 v_3 = -1 - (-1 + 7j) = 0 - 7j = -7j$

**Final Answer:**
$$X(k) = \{6 - 3j, \ -2 + 7j, \ 15j, \ -7j\}$$

---

### Topic 1.2: Filtering of Long Data Sequences — Overlap-Save & Overlap-Add

| Parameter | Overlap-Save Method | Overlap-Add Method |
| :--- | :--- | :--- |
| **Input Block Length** | $N = L + M - 1$ | $L$ samples (zero-padded with $M-1$ zeros to length $N$) |
| **Overlap Between Inputs** | Previous $M-1$ samples prepended | No overlap in input blocks |
| **Convolution Type** | $N$-point Circular Convolution | $N$-point Circular Convolution (equals linear convolution) |
| **Recombination Rule** | **Discard** first $M-1$ corrupted samples of each block | **Add (accumulate)** overlapping $M-1$ trailing samples |

---

#### Question 1.2.1 (March 2026 — Re-Exam)
> **Question:** A digital filter has the impulse response $h(n) = \{2, 2, 1\}$. Determine the output of the filter if the input sequence is $x(n) = \{3, 0, -2, 0, 2, 1\}$ using the **Overlap-Add method**.  
> **Exam:** Re-Examination (2025–2026), March 2026 | **Marks:** 5 Marks  
> **Official Solution Link:** [ANS_Re-Exam_Digital Signal Processing_2025-2026.pdf](./Sem-V%20QP%20Misc/sem%205%20last%20year%20reexam/Digital%20Signal%20Processing/ANS_Re-Exam_Digital%20Signal%20Processing%28DJS23ECPC501%29_Semester%20V_2025-2026.pdf#page=6)

**Step-by-Step Mathematical Solution:**

1. **Determine Parameters:**
   * Filter length $M = 3$ ($h(n) = \{2, 2, 1\}$).
   * Total input length $N_x = 6$. Choose block length $L = 3$.
   * Total section length $N = L + M - 1 = 3 + 3 - 1 = 5$.
   * Total output length $L_{\text{out}} = N_x + M - 1 = 6 + 3 - 1 = 8$.

2. **Partition Input into Blocks of Length $L=3$ & Zero-Pad to Length $N=5$:**
   * Block 1: $x_1(n) = \{3, 0, -2, 0, 0\}$
   * Block 2: $x_2(n) = \{0, 2, 1, 0, 0\}$

3. **Compute Linear Convolution of Each Block with $h(n) = \{2, 2, 1\}$:**
   * **For Block 1 ($y_1(n) = x_1(n) * h(n)$):**
     * $y_1(0) = 3 \times 2 = 6$
     * $y_1(1) = 3(2) + 0(2) = 6$
     * $y_1(2) = 3(1) + 0(2) + (-2)(2) = 3 - 4 = -1$
     * $y_1(3) = 0(1) + (-2)(2) + 0(2) = -4$
     * $y_1(4) = (-2)(1) + 0(2) + 0(1) = -2$
     $$\implies y_1(n) = \{6, 6, -1, -4, -2\}$$

   * **For Block 2 ($y_2(n) = x_2(n) * h(n)$):**
     * $y_2(0) = 0 \times 2 = 0$
     * $y_2(1) = 0(2) + 2(2) = 4$
     * $y_2(2) = 0(1) + 2(2) + 1(2) = 6$
     * $y_2(3) = 2(1) + 1(2) = 4$
     * $y_2(4) = 1(1) = 1$
     $$\implies y_2(n) = \{0, 4, 6, 4, 1\}$$

4. **Overlap-Add Recombination (Shift by $L=3$):**

```
n:        0    1    2     3     4    5    6    7
------------------------------------------------
y1(n):    6    6   -1    -4    -2
y2(n):                    0     4    6    4    1
------------------------------------------------
y(n):     6    6   -1    -4     2    6    4    1
```

* $y(0) = 6$
* $y(1) = 6$
* $y(2) = -1$
* $y(3) = -4 + 0 = -4$
* $y(4) = -2 + 4 = 2$
* $y(5) = 6$
* $y(6) = 4$
* $y(7) = 1$

**Final Answer:**
$$y(n) = \{6, \ 6, \ -1, \ -4, \ 2, \ 6, \ 4, \ 1\}$$

---

#### Question 1.2.2 (Dec 2024 — Final Exam)
> **Question:** Perform the **Overlap-Save method** to find the output of a filter whose impulse response $h(n) = \{1, 2\}$ and input signal $x(n) = \{1, 2, -1, 2, 3, -2, -3, -1, 1, 1, 2, -1\}$ using block length $N = 4$.  
> **Exam:** Final Examination (2024–2025), Dec 2024 | **Marks:** 7 Marks  
> **Official Solution Link:** [ANS_Final-Exam_Digital Signal Processing_2024-2025.pdf](./Sem-V%20QP%20Misc/ANS_Final-Exam_Digital%20Signal%20Processing%28DJS22EC504%29_Semester%20V_2024-2025.pdf#page=5)

**Step-by-Step Mathematical Solution:**

1. **Parameters:**
   * $h(n) = \{1, 2\} \implies M = 2$.
   * Total section size $N = 4 \implies L = N - M + 1 = 4 - 2 + 1 = 3$ new samples per block.
   * Number of samples discarded per block $= M - 1 = 1$.
   * Zero-pad $h(n)$ to length $N = 4$: $h_4(n) = \{1, 2, 0, 0\}$.

2. **Form Overlap-Save Input Blocks (Prepend previous $M-1 = 1$ sample):**
   * Block 1: $x_{1m}(n) = [0, \ 1, 2, -1]$ (prepend 0)
   * Block 2: $x_{2m}(n) = [-1, \ 2, 3, -2]$
   * Block 3: $x_{3m}(n) = [-2, \ -3, -1, 1]$
   * Block 4: $x_{4m}(n) = [1, \ 1, 2, -1]$

3. **Perform 4-point Circular Convolution $y_{km}(n) = x_{km}(n) \mathbin{\circledast}_4 h_4(n)$:**
   * **Block 1:** $x_{1m} = [0, 1, 2, -1]$
     $$\begin{bmatrix} y_{1m}(0) \\ y_{1m}(1) \\ y_{1m}(2) \\ y_{1m}(3) \end{bmatrix} = \begin{bmatrix} 1 & 0 & 0 & 2 \\ 2 & 1 & 0 & 0 \\ 0 & 2 & 1 & 0 \\ 0 & 0 & 2 & 1 \end{bmatrix} \begin{bmatrix} 0 \\ 1 \\ 2 \\ -1 \end{bmatrix} = \begin{bmatrix} -2 \\ 1 \\ 4 \\ 3 \end{bmatrix}$$
     * Discard index 0 $\implies$ Keep: $\{1, 4, 3\}$.

   * **Block 2:** $x_{2m} = [-1, 2, 3, -2]$
     $$\begin{bmatrix} y_{2m}(0) \\ y_{2m}(1) \\ y_{2m}(2) \\ y_{2m}(3) \end{bmatrix} = \begin{bmatrix} 1 & 0 & 0 & 2 \\ 2 & 1 & 0 & 0 \\ 0 & 2 & 1 & 0 \\ 0 & 0 & 2 & 1 \end{bmatrix} \begin{bmatrix} -1 \\ 2 \\ 3 \\ -2 \end{bmatrix} = \begin{bmatrix} -5 \\ 0 \\ 7 \\ 4 \end{bmatrix}$$
     * Discard index 0 $\implies$ Keep: $\{0, 7, 4\}$.

   * **Block 3:** $x_{3m} = [-2, -3, -1, 1]$
     $$\begin{bmatrix} y_{3m}(0) \\ y_{3m}(1) \\ y_{3m}(2) \\ y_{3m}(3) \end{bmatrix} = \begin{bmatrix} 1 & 0 & 0 & 2 \\ 2 & 1 & 0 & 0 \\ 0 & 2 & 1 & 0 \\ 0 & 0 & 2 & 1 \end{bmatrix} \begin{bmatrix} -2 \\ -3 \\ -1 \\ 1 \end{bmatrix} = \begin{bmatrix} 0 \\ -7 \\ -7 \\ -1 \end{bmatrix}$$
     * Discard index 0 $\implies$ Keep: $\{-7, -7, -1\}$.

   * **Block 4:** $x_{4m} = [1, 1, 2, -1]$
     $$\begin{bmatrix} y_{4m}(0) \\ y_{4m}(1) \\ y_{4m}(2) \\ y_{4m}(3) \end{bmatrix} = \begin{bmatrix} 1 & 0 & 0 & 2 \\ 2 & 1 & 0 & 0 \\ 0 & 2 & 1 & 0 \\ 0 & 0 & 2 & 1 \end{bmatrix} \begin{bmatrix} 1 \\ 1 \\ 2 \\ -1 \end{bmatrix} = \begin{bmatrix} -1 \\ 3 \\ 4 \\ 3 \end{bmatrix}$$
     * Discard index 0 $\implies$ Keep: $\{3, 4, 3\}$.
   * Final tail sample: Since input ends, remaining linear convolution tail gives: $(-1) \times 2 = -2$.

4. **Concatenate Kept Samples:**
   $$y(n) = \{1, 4, 3, \ 0, 7, 4, \ -7, -7, -1, \ 3, 4, 3, \ -2\}$$

---

### Topic 1.3: Circular Convolution of Sequences using DFT & Matrix Method

#### Question 1.3.1 (Dec 2025 — Final Exam)
> **Question:** Perform the circular convolution, $q(n)$, of two sequences $x(n) = \{1, 2, 3\}$ and $y(n) = \{2, 3, 4, 1\}$.  
> **Exam:** Final Examination (2025–2026), Dec 2025 | **Marks:** 5 Marks  
> **Official Solution Link:** [ANS-Sem-V-EXTC-Digital Signal Processing.pdf](./ANS-Sem-V-EXTC-Digital%20Signal%20Processing.pdf#page=5)

**Step-by-Step Mathematical Solution:**

1. **Equalize Lengths to $N = \max(L_1, L_2) = 4$ by Zero-Padding:**
   $$x(n) = \{1, 2, 3, 0\}, \quad y(n) = \{2, 3, 4, 1\}$$

2. **Construct the Circular Convolution Matrix (Circulant Matrix of $y(n)$):**
   $$q(n) = \begin{bmatrix} y(0) & y(3) & y(2) & y(1) \\ y(1) & y(0) & y(3) & y(2) \\ y(2) & y(1) & y(0) & y(3) \\ y(3) & y(2) & y(1) & y(0) \end{bmatrix} \begin{bmatrix} x(0) \\ x(1) \\ x(2) \\ x(3) \end{bmatrix}$$
   $$\begin{bmatrix} q(0) \\ q(1) \\ q(2) \\ q(3) \end{bmatrix} = \begin{bmatrix} 2 & 1 & 4 & 3 \\ 3 & 2 & 1 & 4 \\ 4 & 3 & 2 & 1 \\ 1 & 4 & 3 & 2 \end{bmatrix} \begin{bmatrix} 1 \\ 2 \\ 3 \\ 0 \end{bmatrix}$$

3. **Multiply Row by Column:**
   * $q(0) = 2(1) + 1(2) + 4(3) + 3(0) = 2 + 2 + 12 + 0 = 16$
   * $q(1) = 3(1) + 2(2) + 1(3) + 4(0) = 3 + 4 + 3 + 0 = 10$
   * $q(2) = 4(1) + 3(2) + 2(3) + 1(0) = 4 + 6 + 6 + 0 = 16$
   * $q(3) = 1(1) + 4(2) + 3(3) + 2(0) = 1 + 8 + 9 + 0 = 18$

**Final Answer:**
$$q(n) = \{16, \ 10, \ 16, \ 18\}$$

---

### Topic 1.4: DFT Properties & Circular Shift Problems

#### Circular Time-Shift Property
$$\mathcal{DFT}_N\{x((n - m))_N\} = X(k) e^{-j \frac{2\pi}{N} k m} = X(k) W_N^{k m}$$

#### Question 1.4.1 (Dec 2025 — Final Exam)
> **Question:** Find the DFT of four-point sequence $x(n) = \{2, 4, 3, 1\}$. Without performing DFT or IDFT, find the DFT of $x_1(n) = x((n-1))_4$.  
> **Exam:** Final Examination (2025–2026), Dec 2025 | **Marks:** 5 Marks  
> **Official Solution Link:** [ANS-Sem-V-EXTC-Digital Signal Processing.pdf](./ANS-Sem-V-EXTC-Digital%20Signal%20Processing.pdf#page=5)

**Step-by-Step Mathematical Solution:**

1. **Calculate the 4-point DFT $X(k)$ of $x(n) = \{2, 4, 3, 1\}$:**
   $$X(k) = \sum_{n=0}^{3} x(n) W_4^{k n}, \quad \text{where } W_4 = e^{-j \pi / 2} = -j$$
   * For $k = 0$:
     $$X(0) = 2 + 4 + 3 + 1 = 10$$
   * For $k = 1$:
     $$X(1) = 2(1) + 4(-j) + 3(-1) + 1(j) = 2 - 4j - 3 + j = -1 - 3j$$
   * For $k = 2$:
     $$X(2) = 2(1) + 4(-1) + 3(1) + 1(-1) = 2 - 4 + 3 - 1 = 0$$
   * For $k = 3$:
     $$X(3) = X^*(1) = -1 + 3j$$
   $$\implies X(k) = \{10, \ -1 - 3j, \ 0, \ -1 + 3j\}$$

2. **Apply Circular Shift Property for $m = 1$:**
   $$X_1(k) = \mathcal{DFT}\{x((n-1))_4\} = X(k) W_4^{1 \cdot k} = X(k) (-j)^k$$
   * For $k = 0$: $X_1(0) = X(0) \cdot (-j)^0 = 10 \times 1 = 10$
   * For $k = 1$: $X_1(1) = X(1) \cdot (-j)^1 = (-1 - 3j)(-j) = j + 3j^2 = -3 + j$
   * For $k = 2$: $X_1(2) = X(2) \cdot (-j)^2 = 0 \times (-1) = 0$
   * For $k = 3$: $X_1(3) = X(3) \cdot (-j)^3 = (-1 + 3j)(j) = -j + 3j^2 = -3 - j$

**Final Answer:**
$$X_1(k) = \{10, \ -3 + j, \ 0, \ -3 - j\}$$

---

#### Question 1.4.2 (March 2026 — Re-Exam)
> **Question:** Find the DFT of $x(n) = \{2, 3, 4, 5\}$. Using these results and not otherwise, find the DFT of $x_1(n) = \{5, 2, 3, 4\}$.  
> **Exam:** Re-Examination (2025–2026), March 2026 | **Marks:** 5 Marks  
> **Official Solution Link:** [ANS_Re-Exam_Digital Signal Processing_2025-2026.pdf](./Sem-V%20QP%20Misc/sem%205%20last%20year%20reexam/Digital%20Signal%20Processing/ANS_Re-Exam_Digital%20Signal%20Processing%28DJS23ECPC501%29_Semester%20V_2025-2026.pdf#page=5)

**Step-by-Step Mathematical Solution:**

1. **Compute DFT of $x(n) = \{2, 3, 4, 5\}$:**
   * $X(0) = 2 + 3 + 4 + 5 = 14$
   * $X(1) = 2(1) + 3(-j) + 4(-1) + 5(j) = 2 - 3j - 4 + 5j = -2 + 2j$
   * $X(2) = 2(1) + 3(-1) + 4(1) + 5(-1) = 2 - 3 + 4 - 5 = -2$
   * $X(3) = X^*(1) = -2 - 2j$
   $$\implies X(k) = \{14, \ -2 + 2j, \ -2, \ -2 - 2j\}$$

2. **Identify Relation:**
   $$x_1(n) = \{5, 2, 3, 4\} = x((n-1))_4 \quad (\text{circular right shift by } m = 1)$$

3. **Apply Circular Shift Theorem:**
   $$X_1(k) = X(k) W_4^k = X(k) (-j)^k$$
   * $X_1(0) = 14(1) = 14$
   * $X_1(1) = (-2 + 2j)(-j) = 2j - 2j^2 = 2 + 2j$
   * $X_1(2) = (-2)(-1) = 2$
   * $X_1(3) = (-2 - 2j)(j) = -2j - 2j^2 = 2 - 2j$

**Final Answer:**
$$X_1(k) = \{14, \ 2 + 2j, \ 2, \ 2 - 2j\}$$

---

### Topic 1.5: Frequency Analysis of Signals Using the DFT

#### Exam Model / Core Question
> **Question:** Explain frequency analysis of continuous and discrete-time signals using DFT. Define frequency resolution, spectral leakage, and the picket-fence effect, and state how each is controlled.  
> **Type:** Core Model Question | **Marks:** 5 Marks

**Key Derivations & Points for Full Marks:**

1. **Relationship between Continuous Frequency ($f$ or $\Omega$) and DFT Bin Index ($k$):**
   * If a continuous signal $x_a(t)$ is sampled at $F_s = 1/T$ for a duration $T_0 = N T$:
     $$f_k = k \frac{F_s}{N} = \frac{k}{T_0}, \quad \omega_k = \frac{2\pi k}{N} \quad (0 \le k \le N-1)$$
   * **Frequency Resolution ($\Delta f$):**
     $$\Delta f = \frac{F_s}{N} = \frac{1}{T_0}$$
     Resolution depends **only** on the total record length $T_0$, **not** on zero-padding.

2. **Spectral Leakage:**
   * Occurs when the continuous signal contains frequencies that do **not** fall exactly on an integer DFT bin ($f \neq k F_s/N$), causing truncation by a rectangular window in the time domain.
   * In the frequency domain, the spectrum convolves with $\frac{\sin(\pi f N T)}{\sin(\pi f T)}$, spreading energy into adjacent bins.
   * **Remedy:** Apply tapered windows (Hamming, Hanning, Blackman) with lower side-lobe levels.

3. **Picket Fence Effect:**
   * The DFT acts as a bank of discrete bandpass filters sampled at discrete points $\omega_k = 2\pi k / N$. Peaks falling between bins are attenuated (scalloping loss).
   * **Remedy:** **Zero-padding** the sequence in the time domain interpolates the DFT spectrum, reducing scalloping loss and improving visual peak location.

---

## Part 2: Characteristics, Design & Realization of FIR Digital Filters

```
                                FIR Digital Filters
                                         │
        ┌────────────────────────────────┼────────────────────────────────┐
        ▼                                ▼                                ▼
  Windowing Design            Frequency Sampling Design             FIR Realizations
• Rectangular, Hamming,       • Sample H_d(e^jω) at ω_k = 2πk/N   • Direct Form (transversal)
  Hanning, Blackman           • Interpolate impulse response      • Folded Linear Phase (N/2 mults)
• h(n) = h_d(n) · w(n)        • Type-I (integer delay α = (N-1)/2)• Cascade & Frequency Sampling
```

---

### Topic 2.1: Design of Linear Phase FIR Filters using Window Techniques

#### Window Function Formulas & Characteristics
* Center of symmetry: $\alpha = \frac{N-1}{2}$
* **Rectangular Window**: $w(n) = 1, \quad 0 \le n \le N-1$  
  * Main-lobe width: $\frac{4\pi}{N}$, Peak side-lobe attenuation: $-13\text{ dB}$
* **Hanning Window**: $w(n) = 0.5 - 0.5\cos\left(\frac{2\pi n}{N-1}\right), \quad 0 \le n \le N-1$  
  * Main-lobe width: $\frac{8\pi}{N}$, Peak side-lobe attenuation: $-31\text{ dB}$
* **Hamming Window**: $w(n) = 0.54 - 0.46\cos\left(\frac{2\pi n}{N-1}\right), \quad 0 \le n \le N-1$  
  * Main-lobe width: $\frac{8\pi}{N}$, Peak side-lobe attenuation: $-41\text{ dB}$
* **Blackman Window**: $w(n) = 0.42 - 0.5\cos\left(\frac{2\pi n}{N-1}\right) + 0.08\cos\left(\frac{4\pi n}{N-1}\right)$  
  * Main-lobe width: $\frac{12\pi}{N}$, Peak side-lobe attenuation: $-58\text{ dB}$
* **Bartlett (Triangular) Window**: $w(n) = 1 - \frac{2|n - \alpha|}{N-1}, \quad 0 \le n \le N-1$

---

#### Question 2.1.1 (Dec 2025 — Final Exam)
> **Question:** Design an FIR lowpass filter using a rectangular window for the following specifications: cut-off frequency $\omega_c = \pi/4$, filter length $M = 5$.  
> **Exam:** Final Examination (2025–2026), Dec 2025 | **Marks:** 8 Marks  
> **Official Solution Link:** [ANS-Sem-V-EXTC-Digital Signal Processing.pdf](./ANS-Sem-V-EXTC-Digital%20Signal%20Processing.pdf#page=3)

**Step-by-Step Mathematical Solution:**

1. **Desired Frequency Response:**
   $$H_d(e^{j\omega}) = \begin{cases} e^{-j\omega \alpha}, & |\omega| \le \omega_c = \frac{\pi}{4} \\ 0, & \frac{\pi}{4} < |\omega| \le \pi \end{cases}$$
   where $\alpha = \frac{M-1}{2} = \frac{5-1}{2} = 2$.

2. **Inverse DTFT for Desired Impulse Response $h_d(n)$:**
   $$h_d(n) = \frac{1}{2\pi} \int_{-\omega_c}^{\omega_c} e^{-j\omega \alpha} e^{j\omega n} d\omega = \frac{1}{2\pi} \int_{-\pi/4}^{\pi/4} e^{j\omega(n-2)} d\omega = \frac{\sin\left(\frac{\pi}{4}(n-2)\right)}{\pi(n-2)}$$

3. **Evaluate $h_d(n)$ for $n = 0, 1, 2, 3, 4$:**
   * For $n = 2$ (L'Hôpital's rule limit):
     $$h_d(2) = \frac{\omega_c}{\pi} = \frac{\pi/4}{\pi} = 0.25$$
   * For $n = 1$:
     $$h_d(1) = \frac{\sin\left(\frac{\pi}{4}(1-2)\right)}{\pi(1-2)} = \frac{\sin(-\pi/4)}{-\pi} = \frac{-1/\sqrt{2}}{-\pi} = \frac{1}{\pi\sqrt{2}} \approx 0.2251$$
   * For $n = 0$:
     $$h_d(0) = \frac{\sin\left(\frac{\pi}{4}(0-2)\right)}{\pi(0-2)} = \frac{\sin(-\pi/2)}{-2\pi} = \frac{-1}{-2\pi} = \frac{1}{2\pi} \approx 0.1592$$
   * By symmetry around $\alpha = 2$:
     $$h_d(3) = h_d(1) \approx 0.2251, \quad h_d(4) = h_d(0) \approx 0.1592$$

4. **Apply Rectangular Window $w(n) = 1$ ($0 \le n \le 4$):**
   $$h(n) = h_d(n) \cdot w(n) = \{0.1592, \ 0.2251, \ 0.25, \ 0.2251, \ 0.1592\}$$

5. **Transfer Function $H(z)$:**
   $$H(z) = 0.1592 + 0.2251 z^{-1} + 0.25 z^{-2} + 0.2251 z^{-3} + 0.1592 z^{-4}$$

---

#### Question 2.1.2 (Dec 2024 — Final Exam)
> **Question:** Design a bandpass filter to pass frequencies in the range of $1\text{ to }2\text{ rad/s}$ using a **Hanning window**. Use length of filter $M = 5$.  
> **Exam:** Final Examination (2024–2025), Dec 2024 | **Marks:** 8 Marks  
> **Official Solution Link:** [ANS_Final-Exam_Digital Signal Processing_2024-2025.pdf](./Sem-V%20QP%20Misc/ANS_Final-Exam_Digital%20Signal%20Processing%28DJS22EC504%29_Semester%20V_2024-2025.pdf#page=4)

**Step-by-Step Mathematical Solution:**

1. **Specifications & Cutoff Frequencies:**
   * $\omega_{c1} = 1\text{ rad/s}$, $\omega_{c2} = 2\text{ rad/s}$, $M = 5 \implies \alpha = \frac{5-1}{2} = 2$.
   $$H_d(e^{j\omega}) = \begin{cases} e^{-j 2\omega}, & 1 \le |\omega| \le 2 \\ 0, & \text{otherwise} \end{cases}$$

2. **Compute $h_d(n)$:**
   $$h_d(n) = \frac{1}{2\pi} \left[ \int_{-2}^{-1} e^{j\omega(n-2)} d\omega + \int_{1}^{2} e^{j\omega(n-2)} d\omega \right] = \frac{\sin(2(n-2)) - \sin(1(n-2))}{\pi(n-2)}$$
   * For $n = 2$:
     $$h_d(2) = \frac{\omega_{c2} - \omega_{c1}}{\pi} = \frac{2 - 1}{\pi} = \frac{1}{\pi} \approx 0.3183$$
   * For $n = 1$:
     $$h_d(1) = \frac{\sin(-2) - \sin(-1)}{\pi(-1)} = \frac{-\sin(2\text{ rad}) + \sin(1\text{ rad})}{-\pi} = \frac{-0.9093 + 0.8415}{-\pi} = \frac{-0.0678}{-\pi} \approx 0.0216$$
   * For $n = 0$:
     $$h_d(0) = \frac{\sin(-4) - \sin(-2)}{\pi(-2)} = \frac{-\sin(4) + \sin(2)}{-2\pi} = \frac{-(-0.7568) + 0.9093}{-2\pi} = \frac{1.6661}{-2\pi} \approx -0.2652$$
   * Symmetry: $h_d(3) = h_d(1) \approx 0.0216, \quad h_d(4) = h_d(0) \approx -0.2652$.

3. **Hanning Window Coefficients ($N = 5$):**
   $$w(n) = 0.5 - 0.5\cos\left(\frac{2\pi n}{4}\right) = 0.5 - 0.5\cos\left(\frac{\pi n}{2}\right)$$
   * $w(0) = 0.5 - 0.5(1) = 0$
   * $w(1) = 0.5 - 0.5(0) = 0.5$
   * $w(2) = 0.5 - 0.5(-1) = 1.0$
   * $w(3) = 0.5 - 0.5(0) = 0.5$
   * $w(4) = 0.5 - 0.5(1) = 0$

4. **Windowed Impulse Response $h(n) = h_d(n) \cdot w(n)$:**
   * $h(0) = -0.2652 \times 0 = 0$
   * $h(1) = 0.0216 \times 0.5 = 0.0108$
   * $h(2) = 0.3183 \times 1.0 = 0.3183$
   * $h(3) = 0.0216 \times 0.5 = 0.0108$
   * $h(4) = -0.2652 \times 0 = 0$

**Final Answer:**
$$h(n) = \{0, \ 0.0108, \ 0.3183, \ 0.0108, \ 0\}, \quad H(z) = 0.0108 z^{-1} + 0.3183 z^{-2} + 0.0108 z^{-3}$$

---

### Topic 2.2: Design of Linear Phase FIR Filters using Frequency Sampling Technique

#### Design Methodology (Type-I, Sampled at $\omega_k = \frac{2\pi k}{N}$)
$$h(n) = \frac{1}{N} \sum_{k=0}^{N-1} H(k) e^{j \frac{2\pi}{N} k n}$$
For a linear phase filter with symmetry about $\alpha = \frac{N-1}{2}$, $H(k) = |H(k)| e^{-j \frac{2\pi k}{N}\left(\frac{N-1}{2}\right)}$.  
When expanded, this simplifies to:
$$h(n) = \frac{1}{N} \left[ H(0) + 2 \sum_{k=1}^{\frac{N-1}{2}} |H(k)| \cos\left(\frac{2\pi k}{N}(n - \alpha)\right) \right] \quad (N \text{ odd})$$

---

#### Question 2.2.1 (TT2 — Term Test II)
> **Question:** Design an FIR filter using the Frequency Sampling technique for:
> $$H(e^{j\omega}) = \begin{cases} e^{-j 2\omega}, & 0.3\pi \le |\omega| \le 0.5\pi \\ 0, & \text{otherwise} \end{cases}$$
> for $N = 5$ (Type-I).  
> **Exam:** Term Test II (22/10/2026), Q3.a | **Marks:** 5 Marks

**Step-by-Step Mathematical Solution:**

1. **Sample Frequencies for $N = 5$ ($\omega_k = \frac{2\pi k}{5}, \ k = 0, 1, 2, 3, 4$):**
   * $k = 0 \implies \omega_0 = 0 \implies H(0) = 0$
   * $k = 1 \implies \omega_1 = \frac{2\pi}{5} = 0.4\pi \in [0.3\pi, 0.5\pi] \implies H(1) = e^{-j 2(0.4\pi)} = e^{-j 0.8\pi}$
   * $k = 2 \implies \omega_2 = \frac{4\pi}{5} = 0.8\pi \notin [0.3\pi, 0.5\pi] \implies H(2) = 0$
   * $k = 3 \implies \omega_3 = \frac{6\pi}{5} = 1.2\pi \equiv -0.8\pi \implies H(3) = 0$
   * $k = 4 \implies \omega_4 = \frac{8\pi}{5} = 1.6\pi \equiv -0.4\pi \in [-0.5\pi, -0.3\pi] \implies H(4) = e^{j 0.8\pi}$

2. **Compute Impulse Response via IDFT Formula:**
   $$h(n) = \frac{1}{5} \sum_{k=0}^{4} H(k) e^{j \frac{2\pi k n}{5}} = \frac{1}{5} \left[ e^{-j 0.8\pi} e^{j \frac{2\pi n}{5}} + e^{j 0.8\pi} e^{j \frac{8\pi n}{5}} \right]$$
   Note that $e^{j \frac{8\pi n}{5}} = e^{-j \frac{2\pi n}{5}}$:
   $$h(n) = \frac{1}{5} \left[ e^{j \frac{2\pi}{5}(n - 2)} + e^{-j \frac{2\pi}{5}(n - 2)} \right] = \frac{2}{5} \cos\left(\frac{2\pi}{5}(n - 2)\right)$$

3. **Evaluate for $n = 0, 1, 2, 3, 4$:**
   * $n = 0$: $h(0) = \frac{2}{5}\cos\left(\frac{-4\pi}{5}\right) = 0.4 \times (-0.8090) = -0.3236$
   * $n = 1$: $h(1) = \frac{2}{5}\cos\left(\frac{-2\pi}{5}\right) = 0.4 \times (0.3090) = 0.1236$
   * $n = 2$: $h(2) = \frac{2}{5}\cos(0) = 0.4 \times 1 = 0.4000$
   * $n = 3$: $h(3) = h(1) = 0.1236$
   * $n = 4$: $h(4) = h(0) = -0.3236$

**Final Answer:**
$$h(n) = \{-0.3236, \ 0.1236, \ 0.4000, \ 0.1236, \ -0.3236\}$$

---

### Topic 2.3: Types 1 to 4 Linear Phase FIR Filters

Linear phase condition: $h(n) = \pm h(N - 1 - n)$. Phase delay $\tau_p = \alpha$, Group delay $\tau_g = \alpha = \frac{N-1}{2} = \text{constant}$.

| Filter Type | Symmetry of $h(n)$ | Filter Length $N$ | Inherent Zeros (Fixed at Unit Circle) | Capable Filter Types | Prohibited Filter Types |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Type 1** | **Symmetric** ($h(n) = h(N-1-n)$) | **Odd** | None | **LPF, HPF, BPF, BSF** (Universal) | None |
| **Type 2** | **Symmetric** ($h(n) = h(N-1-n)$) | **Even** | $z = -1$ ($\omega = \pi$) | **LPF, BPF** | **HPF, BSF** (Zero at $\omega=\pi$) |
| **Type 3** | **Antisymmetric** ($h(n) = -h(N-1-n)$) | **Odd** | $z = 1$ ($\omega = 0$), $z = -1$ ($\omega = \pi$) | **BPF, Differentiator, Hilbert** | **LPF, HPF, BSF** |
| **Type 4** | **Antisymmetric** ($h(n) = -h(N-1-n)$) | **Even** | $z = 1$ ($\omega = 0$) | **HPF, BPF, Differentiator** | **LPF, BSF** (Zero at $\omega=0$) |

---

### Topic 2.4: FIR Realization Structures

#### Realization Types
1. **Direct Form (Transversal Filter)**: Requires $N$ multipliers and $N-1$ delays.
2. **Linear-Phase Folded Form (Minimum Multipliers)**:
   Exploits symmetry $h(n) = \pm h(N-1-n)$ by adding symmetric delay taps before multiplying.
   * Multipliers required: $\lfloor N/2 \rfloor$ or $\lceil N/2 \rceil$ (approx. $50\%$ reduction).
3. **Cascade Form**: Factors $H(z)$ into second-order FIR sections: $H(z) = \prod_{k=1}^{K} (b_{0k} + b_{1k}z^{-1} + b_{2k}z^{-2})$.
4. **Frequency Sampling Realization Structure**:
   * Cascades an all-zero **Comb Filter** $H_{\text{comb}}(z) = \frac{1 - z^{-N}}{N}$ with a parallel bank of complex single-pole/second-order resonators:
     $$H(z) = \frac{1 - z^{-N}}{N} \sum_{k=0}^{N-1} \frac{H(k)}{1 - z^{-1} e^{j 2\pi k / N}}$$
   * The poles of the resonators lie on the unit circle at $p_k = e^{j 2\pi k / N}$ and are exactly cancelled by the $N$ zeros of the comb filter.

---

#### Question 2.4.1 (Dec 2025 — Final Exam)
> **Question:** Obtain direct form and cascade form realisations for the transfer function of an FIR system given by:
> $$H(z) = \left(1 - \frac{1}{4}z^{-1} + \frac{3}{8}z^{-2}\right)\left(1 - \frac{1}{8}z^{-1} - \frac{1}{2}z^{-2}\right)$$  
> **Exam:** Final Examination (2025–2026), Dec 2025 | **Marks:** 7 Marks  
> **Official Solution Link:** [ANS-Sem-V-EXTC-Digital Signal Processing.pdf](./ANS-Sem-V-EXTC-Digital%20Signal%20Processing.pdf#page=1)

**Step-by-Step Mathematical Solution:**

1. **Cascade Form Realisation:**
   Let $H(z) = H_1(z) \cdot H_2(z)$, where:
   $$H_1(z) = 1 - \frac{1}{4}z^{-1} + \frac{3}{8}z^{-2}, \quad H_2(z) = 1 - \frac{1}{8}z^{-1} - \frac{1}{2}z^{-2}$$
   * Connect section $H_1(z)$ in cascade with section $H_2(z)$.
   * Intermediate signal $w(n) = x(n) - \frac{1}{4}x(n-1) + \frac{3}{8}x(n-2)$.
   * Output signal $y(n) = w(n) - \frac{1}{8}w(n-1) - \frac{1}{2}w(n-2)$.

```
Cascade Form Block Diagram:

x(n) ──┬─────────────────────(+)────── w(n) ──┬─────────────────────(+)──> y(n)
       │                      ▲               │                      ▲
     [z⁻¹]                    │             [z⁻¹]                    │
       ├─── *( -1/4 ) ────────┤               ├─── *( -1/8 ) ────────┤
     [z⁻¹]                    │             [z⁻¹]                    │
       └─── *( +3/8 ) ────────┘               └─── *( -1/2 ) ────────┘
```

2. **Direct Form Realisation:**
   Expand the product of the polynomials:
   $$H(z) = 1 + \left(-\frac{1}{8} - \frac{1}{4}\right)z^{-1} + \left(-\frac{1}{2} + \frac{1}{32} + \frac{3}{8}\right)z^{-2} + \left(\frac{1}{8} - \frac{3}{64}\right)z^{-3} - \frac{3}{16}z^{-4}$$
   * $z^{-1}$ coeff: $-\frac{1}{8} - \frac{2}{8} = -\frac{3}{8} = -0.375$
   * $z^{-2}$ coeff: $-\frac{16}{32} + \frac{1}{32} + \frac{12}{32} = -\frac{3}{32} = -0.09375$
   * $z^{-3}$ coeff: $\frac{8}{64} - \frac{3}{64} = \frac{5}{64} = +0.078125$
   * $z^{-4}$ coeff: $-\frac{3}{16} = -0.1875$
   $$H(z) = 1 - \frac{3}{8}z^{-1} - \frac{3}{32}z^{-2} + \frac{5}{64}z^{-3} - \frac{3}{16}z^{-4}$$
   * Direct Form realization uses a single delay tapped line of 4 delay elements with tap coefficients $h = [1, -3/8, -3/32, 5/64, -3/16]$.

---

#### Question 2.4.2 (TT2 — Term Test II)
> **Question:** Realize the linear phase FIR filter with the **minimum number of multipliers** for impulse response $h(n) = \{1, -2, 3, 4, -3, 2, -1\}$.  
> **Exam:** Term Test II (22/10/2026), Q3.b | **Marks:** 5 Marks

**Step-by-Step Mathematical Solution:**

1. **Verify Antisymmetry / Symmetry & Length:**
   * Length $N = 7$ (odd).
   * Center $\alpha = \frac{7-1}{2} = 3$. Center sample $h(3) = 4$.
   * Taps:
     * $h(0) = 1, \quad h(6) = -1 \implies h(0) = -h(6)$
     * $h(1) = -2, \quad h(5) = 2 \implies h(1) = -h(5)$
     * $h(2) = 3, \quad h(4) = -3 \implies h(2) = -h(4)$
     * $h(3) = 4$ (nonzero center tap implies mixed / broken pure antisymmetry; realization folds the pairwise symmetric/antisymmetric terms).

2. **Group Shared Multiplier Terms:**
   $$Y(z) = H(z) X(z) = [1 - 2z^{-1} + 3z^{-2} + 4z^{-3} - 3z^{-4} + 2z^{-5} - z^{-6}] X(z)$$
   $$y(n) = 1 \cdot [x(n) - x(n-6)] - 2 \cdot [x(n-1) - x(n-5)] + 3 \cdot [x(n-2) - x(n-4)] + 4 \cdot x(n-3)$$

3. **Hardware Count Comparison:**
   * Direct form: 7 multipliers, 6 delay elements.
   * **Linear-Phase Folded Form:** Only **4 multipliers** (coeffs: $1, -2, 3, 4$), 6 delay elements, and 6 adders/subtractors.

```
Folded Structure:

x(n) ──┬──>[z⁻¹]──┬──>[z⁻¹]──┬──>[z⁻¹]───────────┬──>[z⁻¹]──┬──>[z⁻¹]──┬──>[z⁻¹]
       │          │          │                   │          │          │
       │          │          │                 *(4)         │          │
       │          │          │                   │          │          │
       │          │          └───(+)─── *(3) ───(+)         │          │
       │          │               ▲               ▲         │          │
       │          │              (-)──────────────┼─────────┘          │
       │          │                               │                    │
       │          └──────(+)──── *(-2) ───────────(+)                  │
       │                  ▲                       ▲                    │
       │                 (-)──────────────────────┼────────────────────┘
       │                                          │
       └─────────(+)──── *(1) ────────────────────(+)──> y(n)
                  ▲
                 (-)───────────────────────────────────────────────────┘
```

---

## Part 3: IIR Digital Filters & Realization (Highest Yield / Priority)

```
                                 IIR Digital Filters
                                          │
        ┌─────────────────────────────────┼─────────────────────────────────┐
        ▼                                 ▼                                 ▼
IIR Realization Structures      Analog-to-Digital Mapping         Butterworth Filter Design
• Direct Form I (2N delays)    • IIM: z = e^(sT) (Aliasing)      • Order N from specs (α_p, α_s)
• Direct Form II (Canonic)     • BLT: s = 2/T (1-z^-1)/(1+z^-1)  • Poles on left-half s-plane circle
• Cascade (Biquad sections)    • Frequency Pre-warping:          • BLT bilinear substitution
• Parallel (Partial fractions)   Ω = (2/T) tan(ω/2)              • High sensitivity to wordlength
```

---

### Topic 3.1: IIR Realization Structures (Direct Form I & II, Cascade, Parallel)

| Architecture | Delay Elements ($z^{-1}$) | Multipliers | Feedback Loops | Coefficient Quantization Sensitivity |
| :--- | :--- | :--- | :--- | :--- |
| **Direct Form I (DF-I)** | $N + M$ (Non-canonic) | $N + M + 1$ | Direct overall loop | Very High for high orders ($N \ge 3$) |
| **Direct Form II (DF-II)**| $\max(N, M)$ (Canonic) | $N + M + 1$ | Direct shared loop | Very High (risk of overflow) |
| **Cascade Form** | $\max(N, M)$ (Canonic) | $N + M + 1$ | Isolated 2nd-order biquads | **Low** (Poles decoupled) |
| **Parallel Form** | $\max(N, M)$ (Canonic) | $N + M + 1$ | Independent parallel paths | **Lowest** (Errors do not cascade) |

---

#### Question 3.1.1 (Dec 2025 — Final Exam)
> **Question:**
> 1. Differentiate between FIR and IIR filters.
> 2. If $y(n) = -\frac{1}{4}y(n-1) + \frac{3}{8}y(n-2) + x(n) + 2x(n-1) + x(n-2)$, determine the **parallel form structure**.
> 3. Which of the realisations is better: DFI or DFII? Why?  
> **Exam:** Final Examination (2025–2026), Dec 2025 | **Marks:** 7 Marks  
> **Official Solution Link:** [ANS-Sem-V-EXTC-Digital Signal Processing.pdf](./ANS-Sem-V-EXTC-Digital%20Signal%20Processing.pdf#page=2)

**Step-by-Step Mathematical Solution:**

1. **FIR vs. IIR Filter Comparison:**
   * **Impulse Response**: FIR is finite duration ($h(n) = 0$ for $n \ge N$); IIR is infinite duration.
   * **Stability**: FIR filters are always inherently BIBO stable (all poles at $z=0$); IIR filters can become unstable if poles move outside the unit circle due to coefficient quantization.
   * **Phase**: FIR can achieve strictly linear phase ($\tau_g = \text{const}$); IIR has non-linear phase.
   * **Order/Efficiency**: For identical magnitude specifications, IIR requires a significantly lower order (fewer computations/memory) than FIR.
   * **Implementation**: FIR has no recursive feedback; IIR requires feedback and is susceptible to limit cycle oscillations.

2. **Parallel Form Realisation:**
   Take the Z-transform of the difference equation:
   $$Y(z)\left[1 + \frac{1}{4}z^{-1} - \frac{3}{8}z^{-2}\right] = X(z)\left[1 + 2z^{-1} + z^{-2}\right]$$
   $$H(z) = \frac{1 + 2z^{-1} + z^{-2}}{1 + \frac{1}{4}z^{-1} - \frac{3}{8}z^{-2}}$$

   * **Factor the Denominator Polynomial:**
     Roots of $1 + \frac{1}{4}z^{-1} - \frac{3}{8}z^{-2} = 0$:
     $$\left(1 + \frac{3}{4}z^{-1}\right)\left(1 - \frac{1}{2}z^{-1}\right)$$
     (Check: $\frac{3}{4} - \frac{1}{2} = \frac{1}{4}$, $\frac{3}{4} \times (-\frac{1}{2}) = -\frac{3}{8}$).

   * **Divide Numerator by Denominator (Degrees Equal = 2):**
     $$\frac{z^{-2} + 2z^{-1} + 1}{-\frac{3}{8}z^{-2} + \frac{1}{4}z^{-1} + 1}$$
     Leading term coefficient: $\frac{1}{-3/8} = -\frac{8}{3}$.
     Subtracting $-\frac{8}{3} \times \left[-\frac{3}{8}z^{-2} + \frac{1}{4}z^{-1} + 1\right] = z^{-2} - \frac{2}{3}z^{-1} - \frac{8}{3}$:
     $$\text{Remainder} = \left(2 - \left(-\frac{2}{3}\right)\right)z^{-1} + \left(1 - \left(-\frac{8}{3}\right)\right) = \frac{8}{3}z^{-1} + \frac{11}{3}$$
     Therefore:
     $$H(z) = -\frac{8}{3} + \frac{\frac{8}{3}z^{-1} + \frac{11}{3}}{\left(1 + \frac{3}{4}z^{-1}\right)\left(1 - \frac{1}{2}z^{-1}\right)}$$

   * **Partial Fraction Expansion:**
     $$\frac{\frac{8}{3}z^{-1} + \frac{11}{3}}{\left(1 + \frac{3}{4}z^{-1}\right)\left(1 - \frac{1}{2}z^{-1}\right)} = \frac{A}{1 + \frac{3}{4}z^{-1}} + \frac{B}{1 - \frac{1}{2}z^{-1}}$$
     * For $A$ (set $z^{-1} = -\frac{4}{3}$):
       $$A = \frac{\frac{8}{3}\left(-\frac{4}{3}\right) + \frac{11}{3}}{1 - \frac{1}{2}\left(-\frac{4}{3}\right)} = \frac{-\frac{32}{9} + \frac{33}{9}}{1 + \frac{2}{3}} = \frac{1/9}{5/3} = \frac{1}{9} \times \frac{3}{5} = \frac{1}{15}$$
     * For $B$ (set $z^{-1} = 2$):
       $$B = \frac{\frac{8}{3}(2) + \frac{11}{3}}{1 + \frac{3}{4}(2)} = \frac{\frac{16}{3} + \frac{11}{3}}{1 + \frac{3}{2}} = \frac{27/3}{5/2} = \frac{9}{5/2} = \frac{18}{5}$$
     $$H(z) = -\frac{8}{3} + \frac{1/15}{1 + \frac{3}{4}z^{-1}} + \frac{18/5}{1 - \frac{1}{2}z^{-1}}$$

```
Parallel Form Block Diagram:

                      ┌───────── *( -8/3 ) ─────────────────────────────┐
                      │                                                 │
                      ├──── Section 1 ─────────────────────────(+)──────┼──> y(n)
                      │    w1(n) = x(n) - 3/4 w1(n-1)           ▲       │
x(n) ─────────────────┤    y1(n) = 1/15 w1(n)                   │       │
                      │                                         │       │
                      └──── Section 2 ──────────────────────────┘       │
                           w2(n) = x(n) + 1/2 w2(n-1)                   │
                           y2(n) = 18/5 w2(n)                           │
                                                                        ▼
                                                                       (+)
```

3. **DF-I vs. DF-II Comparison:**
   * **DF-II is strictly better** because it is **canonic in delay elements**.
   * DF-I requires separate delay chains for input and output ($N + M = 2 + 2 = 4$ delays).
   * DF-II shares the intermediate variable $w(n)$ in a single central delay chain, requiring only $\max(N, M) = 2$ delays.
   * **Result:** DF-II halves memory requirements.

---

#### Question 3.1.2 (March 2026 — Re-Exam)
> **Question:** Implement the filter in DF-II realization for $H(z) = \frac{1 + 2z^{-1} + z^{-2}}{1 - 0.5z^{-1} + 0.25z^{-2}}$. Calculate the number of multipliers and delays used. Have the number of delays increased or decreased compared to DF-I?  
> **Exam:** Re-Examination (2025–2026), March 2026 | **Marks:** 7 Marks  
> **Official Solution Link:** [ANS_Re-Exam_Digital Signal Processing_2025-2026.pdf](./Sem-V%20QP%20Misc/sem%205%20last%20year%20reexam/Digital%20Signal%20Processing/ANS_Re-Exam_Digital%20Signal%20Processing%28DJS23ECPC501%29_Semester%20V_2025-2026.pdf#page=2)

**Step-by-Step Mathematical Solution:**

1. **Intermediate State Variable $w(n)$ Formulation:**
   $$H(z) = \frac{Y(z)}{X(z)} = \frac{W(z)}{X(z)} \cdot \frac{Y(z)}{W(z)} = \frac{1}{1 - 0.5z^{-1} + 0.25z^{-2}} \cdot \left(1 + 2z^{-1} + z^{-2}\right)$$
   * Input equation:
     $$w(n) = x(n) + 0.5 w(n-1) - 0.25 w(n-2)$$
   * Output equation:
     $$y(n) = w(n) + 2 w(n-1) + w(n-2)$$

```
Direct Form II Structure:

x(n) ────>(+)──────────────── w(n) ───────────────────>(+)────> y(n)
           ▲                                            ▲
           │                                            │
           ├───── *( +0.5 ) ─────┬───── *( +2.0 ) ──────┤
           │                     │                      │
           │                   [z⁻¹]                    │
           │                     │ w(n-1)               │
           │                     ├──────────────────────┤
           ├───── *( -0.25 ) ────┼───── *( +1.0 ) ──────┘
           │                     │
                               [z⁻¹]
                                 │ w(n-2)
```

2. **Component Counts:**
   * **Delay Elements:**
     * Direct Form I requires: $N + M = 2 + 2 = 4$ delays.
     * Direct Form II requires: $\max(N, M) = 2$ delays.
     * **Conclusion:** The number of delays has **decreased by 2 (50% reduction)**.
   * **Multipliers:**
     * Numerator multipliers: $b_0 = 1$ (trivial), $b_1 = 2$, $b_2 = 1$ (trivial).
     * Denominator feedback multipliers: $-a_1 = 0.5$, $-a_2 = -0.25$.
     * Total multipliers $= 5$ (or $3$ non-trivial multipliers).
   * **Adders:** 4 adders (2 in input loop, 2 in output feedforward path).

---

### Topic 3.2: Mapping of S-Plane to Z-Plane using Impulse Invariance Method (IIM)

#### Fundamental Mapping Formula & Aliasing
* Mapping: Each analog pole $s_k = \sigma_k + j\Omega_k$ maps to a digital pole at $z_k = e^{s_k T} = e^{\sigma_k T} e^{j\Omega_k T}$.
* Stability preservation:
  * If $\sigma_k < 0$ (Left Half of $s$-plane), $|z_k| = e^{\sigma_k T} < 1$ (inside unit circle).
  * If $\sigma_k = 0$ ($j\Omega$ axis), $|z_k| = 1$ (on unit circle).
* **Many-to-One Mapping**:
  Stripping widths of $\frac{2\pi}{T}$ along the $j\Omega$ axis all map onto the exact same unit circle trajectory:
  $$s = \sigma + j\left(\Omega + \frac{2\pi k}{T}\right) \implies z = e^{\sigma T} e^{j\Omega T} e^{j 2\pi k} = e^{\sigma T} e^{j\Omega T}$$
  This causes **spectral aliasing**, making IIM unsuitable for highpass or bandstop filters.
* **Standard Partial Fraction Transform Pair:**
  $$\frac{1}{s - p_k} \ \xrightarrow{\text{IIM}} \ \frac{1}{1 - e^{p_k T} z^{-1}}$$

---

#### Question 3.2.1 (Dec 2025 — Final Exam)
> **Question:** An analog filter has a transfer function $H(s) = \frac{10}{s^2 + 7s + 10}$. Design an equivalent digital filter using the Impulse Invariant Method with $T = 0.2\text{ sec}$.  
> **Exam:** Final Examination (2025–2026), Dec 2025 | **Marks:** 10 Marks  
> **Official Solution Link:** [ANS-Sem-V-EXTC-Digital Signal Processing.pdf](./ANS-Sem-V-EXTC-Digital%20Signal%20Processing.pdf#page=5)

**Step-by-Step Mathematical Solution:**

1. **Partial Fraction Expansion of $H(s)$:**
   $$H(s) = \frac{10}{(s + 2)(s + 5)} = \frac{A}{s + 2} + \frac{B}{s + 5}$$
   * $A = \left. \frac{10}{s + 5} \right|_{s = -2} = \frac{10}{-2 + 5} = \frac{10}{3}$
   * $B = \left. \frac{10}{s + 2} \right|_{s = -5} = \frac{10}{-5 + 2} = -\frac{10}{3}$
   $$H(s) = \frac{10}{3} \left[ \frac{1}{s + 2} - \frac{1}{s + 5} \right]$$

2. **Map Each Pole via $z_k = e^{p_k T}$ ($T = 0.2\text{ s}$):**
   * Pole at $p_1 = -2 \implies z_1 = e^{-2(0.2)} = e^{-0.4} \approx 0.67032$
   * Pole at $p_2 = -5 \implies z_2 = e^{-5(0.2)} = e^{-1.0} \approx 0.36788$

3. **Construct Digital Filter Transfer Function $H(z)$:**
   $$H(z) = \frac{10}{3} \left[ \frac{1}{1 - e^{-0.4} z^{-1}} - \frac{1}{1 - e^{-1.0} z^{-1}} \right] = \frac{10}{3} \left[ \frac{1}{1 - 0.67032 z^{-1}} - \frac{1}{1 - 0.36788 z^{-1}} \right]$$

4. **Combine into a Single Rational Transfer Function:**
   $$H(z) = \frac{10}{3} \cdot \frac{(1 - 0.36788 z^{-1}) - (1 - 0.67032 z^{-1})}{(1 - 0.67032 z^{-1})(1 - 0.36788 z^{-1})}$$
   * Numerator:
     $$\frac{10}{3} [ (0.67032 - 0.36788) z^{-1} ] = \frac{10}{3} [0.30244 z^{-1}] = 1.0081 z^{-1}$$
   * Denominator:
     $$1 - (0.67032 + 0.36788) z^{-1} + (0.67032 \times 0.36788) z^{-2} = 1 - 1.0382 z^{-1} + 0.2466 z^{-2}$$

**Final Answer:**
$$H(z) = \frac{1.0081 z^{-1}}{1 - 1.0382 z^{-1} + 0.2466 z^{-2}}$$

---

#### Question 3.2.2 (March 2026 — Re-Exam)
> **Question:** Convert an analog filter with system function $H(s) = \frac{10}{s^2 + 7s + 10}$ into a digital IIR filter using the Impulse Invariance Method assuming $T = 1\text{ sec}$.  
> **Exam:** Re-Examination (2025–2026), March 2026 | **Marks:** 10 Marks  
> **Official Solution Link:** [ANS_Re-Exam_Digital Signal Processing_2025-2026.pdf](./Sem-V%20QP%20Misc/sem%205%20last%20year%20reexam/Digital%20Signal%20Processing/ANS_Re-Exam_Digital%20Signal%20Processing%28DJS23ECPC501%29_Semester%20V_2025-2026.pdf#page=5)

**Step-by-Step Mathematical Solution:**

1. **Partial Fractions:**
   $$H(s) = \frac{10}{3}\left[\frac{1}{s + 2} - \frac{1}{s + 5}\right]$$

2. **Map Poles for $T = 1\text{ s}$:**
   * $p_1 = -2 \implies z_1 = e^{-2(1)} = e^{-2} \approx 0.13534$
   * $p_2 = -5 \implies z_2 = e^{-5(1)} = e^{-5} \approx 0.00674$

3. **Construct $H(z)$:**
   $$H(z) = \frac{10}{3}\left[\frac{1}{1 - 0.13534 z^{-1}} - \frac{1}{1 - 0.00674 z^{-1}}\right] = \frac{10}{3}\frac{(0.13534 - 0.00674)z^{-1}}{1 - (0.13534 + 0.00674)z^{-1} + (0.13534 \times 0.00674)z^{-2}}$$
   * Numerator: $\frac{10}{3}(0.12860) z^{-1} = 0.42867 z^{-1}$
   * Denominator: $1 - 0.14208 z^{-1} + 0.00091 z^{-2}$

**Final Answer:**
$$H(z) = \frac{0.4287 z^{-1}}{1 - 0.1421 z^{-1} + 0.00091 z^{-2}}$$

---

#### Question 3.2.3 (March 2026 — Re-Exam)
> **Question:** Apply the impulse invariant method and find $H(z)$ for $H(s) = \frac{s + a}{(s + a)^2 + b^2}$.  
> **Exam:** Re-Examination (2025–2026), March 2026 | **Marks:** 8 Marks  
> **Official Solution Link:** [ANS_Re-Exam_Digital Signal Processing_2025-2026.pdf](./Sem-V%20QP%20Misc/sem%205%20last%20year%20reexam/Digital%20Signal%20Processing/ANS_Re-Exam_Digital%20Signal%20Processing%28DJS23ECPC501%29_Semester%20V_2025-2026.pdf#page=7)

**Step-by-Step Mathematical Solution:**

1. **Factor Denominator into Complex Conjugate Poles:**
   $$(s + a)^2 + b^2 = (s + a - jb)(s + a + jb)$$
   Poles: $p_1 = -a + jb, \quad p_2 = -a - jb$.

2. **Partial Fraction Decomposition:**
   $$H(s) = \frac{s + a}{(s + a - jb)(s + a + jb)} = \frac{1/2}{s + a - jb} + \frac{1/2}{s + a + jb}$$

3. **Apply IIM Transformation $\frac{1}{s - p_k} \to \frac{1}{1 - e^{p_k T} z^{-1}}$:**
   $$H(z) = \frac{1}{2}\left[\frac{1}{1 - e^{(-a + jb)T} z^{-1}} + \frac{1}{1 - e^{(-a - jb)T} z^{-1}}\right]$$

4. **Combine over a Common Denominator:**
   * Numerator:
     $$\frac{1}{2} \left[ \left(1 - e^{-a T} e^{-j b T} z^{-1}\right) + \left(1 - e^{-a T} e^{j b T} z^{-1}\right) \right] = \frac{1}{2} \left[ 2 - e^{-a T} (e^{j b T} + e^{-j b T}) z^{-1} \right] = 1 - e^{-a T} \cos(b T) z^{-1}$$
   * Denominator:
     $$\left(1 - e^{-a T} e^{j b T} z^{-1}\right)\left(1 - e^{-a T} e^{-j b T} z^{-1}\right) = 1 - e^{-a T}(e^{j b T} + e^{-j b T}) z^{-1} + e^{-2a T} z^{-2} = 1 - 2 e^{-a T} \cos(b T) z^{-1} + e^{-2a T} z^{-2}$$

**Final Answer:**
$$H(z) = \frac{1 - e^{-a T}\cos(b T) z^{-1}}{1 - 2 e^{-a T}\cos(b T) z^{-1} + e^{-2a T} z^{-2}}$$

---

### Topic 3.3: Bilinear Transformation (BLT) & Butterworth Filter Design

#### Bilinear Transformation Principles
* **Mapping Substitution**:
  $$s = \frac{2}{T} \left( \frac{1 - z^{-1}}{1 + z^{-1}} \right) = \frac{2}{T} \left( \frac{z - 1}{z + 1} \right)$$
* **Nonlinear Frequency Warping**:
  $$\Omega = \frac{2}{T} \tan\left(\frac{\omega}{2}\right) \iff \omega = 2 \arctan\left(\frac{\Omega T}{2}\right)$$
  * Maps entire continuous frequency range $-\infty < \Omega < \infty$ uniquely onto $-\pi < \omega < \pi$.
  * **Completely eliminates aliasing**, but requires pre-warping of critical frequencies.

#### Butterworth Lowpass Filter Design Steps
1. **Pre-warp digital corner frequencies**: $\Omega_p = \frac{2}{T}\tan(\frac{\omega_p}{2})$, $\Omega_s = \frac{2}{T}\tan(\frac{\omega_s}{2})$.
2. **Determine Filter Order $N$**:
   $$N \ge \frac{\log_{10}\left(\sqrt{\frac{10^{0.1 \alpha_s} - 1}{10^{0.1 \alpha_p} - 1}}\right)}{\log_{10}\left(\frac{\Omega_s}{\Omega_p}\right)} = \frac{\log_{10}(D_s / D_p)}{\log_{10}(\Omega_s / \Omega_p)}$$
   Round $N$ up to the nearest integer.
3. **Determine 3-dB Cutoff Frequency $\Omega_c$**:
   $$\Omega_c = \frac{\Omega_p}{\left(10^{0.1 \alpha_p} - 1\right)^{1 / (2N)}}$$
4. **Determine Normalized Poles on the S-Plane Circle of Radius $\Omega_c$**:
   $$s_k = \Omega_c e^{j \left[ \frac{\pi}{2} + \frac{(2k - 1)\pi}{2N} \right]}, \quad k = 1, 2, \dots, N$$
   Keep only poles in the Left Half of the S-plane ($\text{Re}\{s_k\} < 0$).
5. **Substitute $s = \frac{2}{T} \left(\frac{1 - z^{-1}}{1 + z^{-1}}\right)$ into $H(s)$ to obtain $H(z)$**.

---

#### Question 3.3.1 (TT2 — Term Test II)
> **Question:** Determine the order $N$ and cutoff frequency $\Omega_c$ of a Butterworth analog lowpass filter for specifications:
> $$0.9 \le |H(j\Omega)| \le 1 \quad \text{for } 0 \le \Omega \le 0.2\pi, \quad |H(j\Omega)| \le 0.2 \quad \text{for } 0.4\pi \le \Omega \le \pi$$  
> **Exam:** Term Test II (22/10/2026), Q1 | **Marks:** 5 Marks

**Step-by-Step Mathematical Solution:**

1. **Identify Given Specifications:**
   * Passband edge $\Omega_p = 0.2\pi\text{ rad/s}$, Passband magnitude $A_p = 0.9$
   * Stopband edge $\Omega_s = 0.4\pi\text{ rad/s}$, Stopband magnitude $A_s = 0.2$

2. **Convert to Attenuation Parameters:**
   * $\frac{1}{\sqrt{1 + \epsilon^2}} = 0.9 \implies 1 + \epsilon^2 = \frac{1}{0.81} = 1.2346 \implies \epsilon^2 = 0.2346 \implies \epsilon = 0.4843$
   * $\frac{1}{\sqrt{1 + \lambda^2}} = 0.2 \implies 1 + \lambda^2 = \frac{1}{0.04} = 25 \implies \lambda^2 = 24 \implies \lambda = \sqrt{24} \approx 4.899$

3. **Compute Filter Order $N$:**
   $$N \ge \frac{\log_{10}(\lambda / \epsilon)}{\log_{10}(\Omega_s / \Omega_p)} = \frac{\log_{10}(4.899 / 0.4843)}{\log_{10}(0.4\pi / 0.2\pi)} = \frac{\log_{10}(10.1156)}{\log_{10}(2)} = \frac{1.0050}{0.3010} \approx 3.338$$
   Rounding up to the nearest integer:
   $$N = 4$$

4. **Compute Cutoff Frequency $\Omega_c$:**
   $$\Omega_c = \frac{\Omega_p}{(\epsilon)^{1/N}} = \frac{0.2\pi}{(0.4843)^{1/4}} = \frac{0.2\pi}{0.8345} \approx 0.2396\pi \approx 0.753\text{ rad/s}$$

**Final Answer:**
$$N = 4, \quad \Omega_c = 0.753\text{ rad/s} \quad (0.24\pi\text{ rad/s})$$

---

#### Question 3.3.2 (TT2 — Term Test II)
> **Question:**
> 1. Find poles and system transfer function $H(s)$ of a 3rd-order normalized Butterworth filter ($N = 3, \Omega_c = 1$).
> 2. Apply Bilinear Transformation (BLT) with $T = 1\text{ s}$ to obtain the digital filter $H(z)$ from $H(s) = \frac{1}{(s + 1)(s^2 + s + 1)}$.  
> **Exam:** Term Test II (22/10/2026), Q2.a & Q2.b | **Marks:** 5 Marks each (10 Marks total)

**Step-by-Step Mathematical Solution:**

**Part 1: Find Poles and $H(s)$ for $N = 3$:**
* Pole angles for $N = 3$:
  $$\theta_k = \frac{\pi}{2} + \frac{(2k - 1)\pi}{2(3)} = \frac{\pi}{2} + \frac{(2k - 1)\pi}{6}, \quad k = 1, 2, 3$$
  * For $k = 1$: $\theta_1 = 90^\circ + 30^\circ = 120^\circ \implies s_1 = e^{j 120^\circ} = -\frac{1}{2} + j \frac{\sqrt{3}}{2}$
  * For $k = 2$: $\theta_2 = 90^\circ + 90^\circ = 180^\circ \implies s_2 = e^{j 180^\circ} = -1$
  * For $k = 3$: $\theta_3 = 90^\circ + 150^\circ = 240^\circ \implies s_3 = e^{j 240^\circ} = -\frac{1}{2} - j \frac{\sqrt{3}}{2}$
* System transfer function:
  $$H(s) = \frac{1}{(s - s_2)(s - s_1)(s - s_3)} = \frac{1}{(s + 1)\left(s + \frac{1}{2} - j\frac{\sqrt{3}}{2}\right)\left(s + \frac{1}{2} + j\frac{\sqrt{3}}{2}\right)} = \frac{1}{(s + 1)(s^2 + s + 1)}$$

**Part 2: Apply BLT with $T = 1\text{ s}$:**
* BLT substitution:
  $$s = \frac{2}{T}\left(\frac{1 - z^{-1}}{1 + z^{-1}}\right) = 2\left(\frac{1 - z^{-1}}{1 + z^{-1}}\right)$$
* Expand denominator polynomial:
  $$D(s) = (s + 1)(s^2 + s + 1) = s^3 + 2s^2 + 2s + 1$$
* Substitute $s = 2 \frac{1 - z^{-1}}{1 + z^{-1}}$:
  $$H(z) = \frac{1}{\left(2\frac{1-z^{-1}}{1+z^{-1}}\right)^3 + 2\left(2\frac{1-z^{-1}}{1+z^{-1}}\right)^2 + 2\left(2\frac{1-z^{-1}}{1+z^{-1}}\right) + 1} = \frac{(1 + z^{-1})^3}{8(1 - z^{-1})^3 + 8(1 - z^{-1})^2(1 + z^{-1}) + 4(1 - z^{-1})(1 + z^{-1})^2 + (1 + z^{-1})^3}$$
* Expand polynomials:
  * Numerator: $(1 + z^{-1})^3 = 1 + 3z^{-1} + 3z^{-2} + z^{-3}$
  * Term 1: $8(1 - 3z^{-1} + 3z^{-2} - z^{-3}) = 8 - 24z^{-1} + 24z^{-2} - 8z^{-3}$
  * Term 2: $8(1 - z^{-1})(1 - z^{-2}) = 8(1 - z^{-1} - z^{-2} + z^{-3}) = 8 - 8z^{-1} - 8z^{-2} + 8z^{-3}$
  * Term 3: $4(1 + z^{-1})(1 - z^{-2}) = 4(1 + z^{-1} - z^{-2} - z^{-3}) = 4 + 4z^{-1} - 4z^{-2} - 4z^{-3}$
  * Term 4: $1(1 + 3z^{-1} + 3z^{-2} + z^{-3}) = 1 + 3z^{-1} + 3z^{-2} + z^{-3}$
* Sum terms by powers of $z^{-1}$:
  * Constant: $8 + 8 + 4 + 1 = 21$
  * $z^{-1}$: $-24 - 8 + 4 + 3 = -25$
  * $z^{-2}$: $24 - 8 - 4 + 3 = 15$
  * $z^{-3}$: $-8 + 8 - 4 + 1 = -3$

**Final Answer:**
$$H(z) = \frac{1 + 3z^{-1} + 3z^{-2} + z^{-3}}{21 - 25z^{-1} + 15z^{-2} - 3z^{-3}}$$

---

### Topic 3.4: Frequency Transformations in the Digital Domain

To transform a prototype digital lowpass filter with cutoff $\theta_p$ into another desired filter with cutoff $\omega_c$, substitute $z^{-1}$ with an allpass mapping function $g(z^{-1})$:

$$z^{-1} \longrightarrow g(z^{-1})$$

| Target Filter Type | Transformation Substitution $g(z^{-1})$ | Parameter Equations |
| :--- | :--- | :--- |
| **Lowpass $\to$ Lowpass** | $\frac{z^{-1} - a}{1 - a z^{-1}}$ | $a = \frac{\sin\left(\frac{\theta_p - \omega_c}{2}\right)}{\sin\left(\frac{\theta_p + \omega_c}{2}\right)}$ |
| **Lowpass $\to$ Highpass** | $-\frac{z^{-1} + a}{1 + a z^{-1}}$ | $a = -\frac{\cos\left(\frac{\theta_p + \omega_c}{2}\right)}{\cos\left(\frac{\theta_p - \omega_c}{2}\right)}$ |
| **Lowpass $\to$ Bandpass** | $-\frac{z^{-2} - \frac{2 a k}{k + 1} z^{-1} + \frac{k - 1}{k + 1}}{1 - \frac{2 a k}{k + 1} z^{-1} + \frac{k - 1}{k + 1} z^{-2}}$ | $a = \frac{\cos\left(\frac{\omega_{c2} + \omega_{c1}}{2}\right)}{\cos\left(\frac{\omega_{c2} - \omega_{c1}}{2}\right)}, \quad k = \cot\left(\frac{\omega_{c2} - \omega_{c1}}{2}\right)\tan\left(\frac{\theta_p}{2}\right)$ |
| **Lowpass $\to$ Bandstop** | $\frac{z^{-2} - \frac{2 a}{1 + k} z^{-1} + \frac{1 - k}{1 + k}}{1 - \frac{2 a}{1 + k} z^{-1} + \frac{1 - k}{1 + k} z^{-2}}$ | $a = \frac{\cos\left(\frac{\omega_{c2} + \omega_{c1}}{2}\right)}{\cos\left(\frac{\omega_{c2} - \omega_{c1}}{2}\right)}, \quad k = \tan\left(\frac{\omega_{c2} - \omega_{c1}}{2}\right)\tan\left(\frac{\theta_p}{2}\right)$ |

---

## Complete Topic Cross-Reference Index

| Exam Question | Exam Paper & Year | Topic | Official PDF Answer Link |
| :--- | :--- | :--- | :--- |
| **Q1.a [8M]** | Final Exam (Dec 2025) | 8-pt Radix-2 DIT-FFT | [ANS Dec 2025](./ANS-Sem-V-EXTC-Digital%20Signal%20Processing.pdf#page=1) |
| **Q1.b.i [7M]** | Final Exam (Dec 2025) | FIR Direct & Cascade Realization | [ANS Dec 2025](./ANS-Sem-V-EXTC-Digital%20Signal%20Processing.pdf#page=1) |
| **Q1.b.ii [7M]** | Final Exam (Dec 2025) | FIR vs IIR & Parallel IIR Realization | [ANS Dec 2025](./ANS-Sem-V-EXTC-Digital%20Signal%20Processing.pdf#page=2) |
| **Q2.a [8M]** | Final Exam (Dec 2025) | FIR Rectangular Window LPF ($M=5$) | [ANS Dec 2025](./ANS-Sem-V-EXTC-Digital%20Signal%20Processing.pdf#page=3) |
| **Q3.a [10M]** | Final Exam (Dec 2025) | IIM Filter Conversion ($T=0.2\text{ s}$) | [ANS Dec 2025](./ANS-Sem-V-EXTC-Digital%20Signal%20Processing.pdf#page=5) |
| **Q3.b.i [5M]** | Final Exam (Dec 2025) | DFT Circular Shift Property | [ANS Dec 2025](./ANS-Sem-V-EXTC-Digital%20Signal%20Processing.pdf#page=5) |
| **Q3.b.ii [5M]** | Final Exam (Dec 2025) | Circular Convolution Matrix Method | [ANS Dec 2025](./ANS-Sem-V-EXTC-Digital%20Signal%20Processing.pdf#page=5) |
| **Q1.a [8M]** | Re-Exam (March 2026) | 8-pt Radix-2 DIF-FFT | [ANS Re-Exam 2025-26](./Sem-V%20QP%20Misc/sem%205%20last%20year%20reexam/Digital%20Signal%20Processing/ANS_Re-Exam_Digital%20Signal%20Processing%28DJS23ECPC501%29_Semester%20V_2025-2026.pdf#page=1) |
| **Q1.b.i [7M]** | Re-Exam (March 2026) | FIR Folded Linear Phase Structure | [ANS Re-Exam 2025-26](./Sem-V%20QP%20Misc/sem%205%20last%20year%20reexam/Digital%20Signal%20Processing/ANS_Re-Exam_Digital%20Signal%20Processing%28DJS23ECPC501%29_Semester%20V_2025-2026.pdf#page=1) |
| **Q1.b.ii [7M]** | Re-Exam (March 2026) | IIR DF-II Multiplier & Delay Count | [ANS Re-Exam 2025-26](./Sem-V%20QP%20Misc/sem%205%20last%20year%20reexam/Digital%20Signal%20Processing/ANS_Re-Exam_Digital%20Signal%20Processing%28DJS23ECPC501%29_Semester%20V_2025-2026.pdf#page=2) |
| **Q3.a [10M]** | Re-Exam (March 2026) | IIM Filter Conversion ($T=1\text{ s}$) | [ANS Re-Exam 2025-26](./Sem-V%20QP%20Misc/sem%205%20last%20year%20reexam/Digital%20Signal%20Processing/ANS_Re-Exam_Digital%20Signal%20Processing%28DJS23ECPC501%29_Semester%20V_2025-2026.pdf#page=5) |
| **Q3.b.i [5M]** | Re-Exam (March 2026) | Circular Shift DFT Evaluation | [ANS Re-Exam 2025-26](./Sem-V%20QP%20Misc/sem%205%20last%20year%20reexam/Digital%20Signal%20Processing/ANS_Re-Exam_Digital%20Signal%20Processing%28DJS23ECPC501%29_Semester%20V_2025-2026.pdf#page=5) |
| **Q3.b.ii [5M]** | Re-Exam (March 2026) | Overlap-Add Long Sequence Filtering | [ANS Re-Exam 2025-26](./Sem-V%20QP%20Misc/sem%205%20last%20year%20reexam/Digital%20Signal%20Processing/ANS_Re-Exam_Digital%20Signal%20Processing%28DJS23ECPC501%29_Semester%20V_2025-2026.pdf#page=6) |
| **Q4.a [8M]** | Re-Exam (March 2026) | IIM Complex Conjugate Poles | [ANS Re-Exam 2025-26](./Sem-V%20QP%20Misc/sem%205%20last%20year%20reexam/Digital%20Signal%20Processing/ANS_Re-Exam_Digital%20Signal%20Processing%28DJS23ECPC501%29_Semester%20V_2025-2026.pdf#page=7) |
| **Q3.a [8M]** | Final Exam (Dec 2024) | FIR Hanning BPF Design ($M=5$) | [ANS Dec 2024](./Sem-V%20QP%20Misc/ANS_Final-Exam_Digital%20Signal%20Processing%28DJS22EC504%29_Semester%20V_2024-2025.pdf#page=4) |
| **Q3.b.i [7M]** | Final Exam (Dec 2024) | Overlap-Save Long Sequence Filtering | [ANS Dec 2024](./Sem-V%20QP%20Misc/ANS_Final-Exam_Digital%20Signal%20Processing%28DJS22EC504%29_Semester%20V_2024-2025.pdf#page=5) |
| **Q1 [5M]** | Term Test II (2026) | Butterworth Order $N$ & Cutoff $\Omega_c$ | User Upload (TT2 Q1) |
| **Q2.a/b [10M]** | Term Test II (2026) | Butterworth Poles & BLT $T=1\text{ s}$ | User Upload (TT2 Q2.a & Q2.b) |
| **Q3.a [5M]** | Term Test II (2026) | FIR Frequency Sampling Design ($N=5$) | User Upload (TT2 Q3.a) |
| **Q3.b [5M]** | Term Test II (2026) | Folded Linear Phase Realization | User Upload (TT2 Q3.b) |
| **Q3.a [5M]** | Term Test I (2026) | Complex 4-pt DIT-FFT Butterfly | User Upload (TT1 Q3.a) |