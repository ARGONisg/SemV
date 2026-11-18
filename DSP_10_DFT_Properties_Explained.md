Here is the complete, plain-English breakdown of all **10 DFT properties** from your handwritten notes, with an intuitive explanation and a concrete step-by-step numerical example for each.

---

### Reference Sequence (Used Across the Examples)
To make every property easy to verify, let $N = 4$ and choose the base sequence:
$$x(n) = \{1, \; 2, \; 3, \; 4\} \quad \text{for } n = 0, 1, 2, 3$$

Its 4-point DFT $X(k) = \sum_{n=0}^{3} x(n) e^{-j \frac{2\pi}{4} kn} = \sum_{n=0}^{3} x(n) (-j)^{kn}$ evaluates to:
* $X(0) = 1 + 2 + 3 + 4 = \mathbf{10}$
* $X(1) = 1 - 2j - 3 + 4j = \mathbf{-2 + 2j}$
* $X(2) = 1 - 2 + 3 - 4 = \mathbf{-2}$
* $X(3) = 1 + 2j - 3 - 4j = \mathbf{-2 - 2j}$

$$\mathbf{X(k) = \{10, \; -2+2j, \; -2, \; -2-2j\}}$$

---

## 1. Linearity

### Formula:
$$a \cdot x_1(n) + b \cdot x_2(n) \;\xleftrightarrow{\text{DFT}_N}\; a \cdot X_1(k) + b \cdot X_2(k)$$

### Plain-English Meaning:
If you scale signals by constants $a, b$ and add them in the time domain, their frequency spectra scale and add by the exact same constants. The DFT is a strictly linear transformation.

### Numerical Example:
* Let $x_1(n) = \{1, 2, 3, 4\} \implies X_1(k) = \{10, -2+2j, -2, -2-2j\}$
* Let $x_2(n) = \{1, 0, 1, 0\} \implies X_2(k) = \{2, 0, 2, 0\}$
* Construct $y(n) = 2x_1(n) + 3x_2(n)$:
  $$y(n) = 2\{1, 2, 3, 4\} + 3\{1, 0, 1, 0\} = \{2+3, 4+0, 6+3, 8+0\} = \mathbf{\{5, 4, 9, 8\}}$$
* By Linearity, without calculating the DFT of $y(n)$ from scratch:
  $$Y(k) = 2 X_1(k) + 3 X_2(k)$$
  * $Y(0) = 2(10) + 3(2) = \mathbf{26}$
  * $Y(1) = 2(-2+2j) + 3(0) = \mathbf{-4 + 4j}$
  * $Y(2) = 2(-2) + 3(2) = \mathbf{2}$
  * $Y(3) = 2(-2-2j) + 3(0) = \mathbf{-4 - 4j}$
  $$\mathbf{Y(k) = \{26, \; -4+4j, \; 2, \; -4-4j\}}$$

---

## 2. Periodicity

### Formula:
$$x(n + N) = x(n) \quad \text{for all } n, \qquad X(k + N) = X(k) \quad \text{for all } k$$

### Plain-English Meaning:
The DFT assumes that your finite $N$-point block is just one period of an infinitely repeating sequence. If you evaluate past the $N$-th index, it repeats periodically. In $N=4$, index $k=4$ is the same as $k=0$, index $k=5$ is $k=1$, etc.

### Numerical Example:
For $N = 4$ and $X(k) = \{10, -2+2j, -2, -2-2j\}$:
* $X(4) = X(4 - 4) = X(0) = \mathbf{10}$
* $X(5) = X(5 - 4) = X(1) = \mathbf{-2 + 2j}$
* $X(-1) = X(-1 + 4) = X(3) = \mathbf{-2 - 2j}$

---

## 3. Periodic Extension & Circular Shifting Representation

### Formula:
$$x_p(n) = \sum_{l=-\infty}^\infty x(n - lN), \qquad x' (n) = x((n - k))_N$$

### Plain-English Meaning:
Because the DFT treats signals as periodic, a shift in time is **circular**. Imagine the $N$ samples arranged clockwise on a circle. Shifting by $k$ doesn't drop samples off the end; samples that fall off the right wrap around to the beginning.

```
       x(0)=1                 Shift by 1 (Clockwise)         x'(0)=4
    x(3)=4    x(1)=2                 ----->              x'(3)=3    x'(1)=1
       x(2)=3                                                x'(2)=2
```

### Numerical Example:
For $x(n) = \{1, 2, 3, 4\}$ with $N = 4$:
* Shifting circularly by 1 position to the right ($l = 1$):
  * $n = 0 \implies x((0 - 1))_4 = x((-1))_4 = x(3) = \mathbf{4}$
  * $n = 1 \implies x((1 - 1))_4 = x(0) = \mathbf{1}$
  * $n = 2 \implies x((2 - 1))_4 = x(1) = \mathbf{2}$
  * $n = 3 \implies x((3 - 1))_4 = x(2) = \mathbf{3}$
* Result: $x((n-1))_4 = \mathbf{\{4, 1, 2, 3\}}$.

---

## 4. Circular Time Reversal

### Formula:
$$x((-n))_N = x(N - n) \;\xleftrightarrow{\text{DFT}_N}\; X((-k))_N = X(N - k)$$

### Plain-English Meaning:
Reversing a sequence circularly leaves index $0$ fixed in place, while reversing all the other $(N-1)$ samples. Its DFT is also reversed in the exact same way (sample $k=0$ stays, while bins $1$ to $N-1$ are reversed).

### Numerical Example:
For $x(n) = \{1, 2, 3, 4\}$ ($N = 4$):
* $x((-0))_4 = x(0) = \mathbf{1}$
* $x((-1))_4 = x(4 - 1) = x(3) = \mathbf{4}$
* $x((-2))_4 = x(4 - 2) = x(2) = \mathbf{3}$
* $x((-3))_4 = x(4 - 3) = x(1) = \mathbf{2}$
$$x_{\text{rev}}(n) = \mathbf{\{1, 4, 3, 2\}}$$
* Its DFT is $X(N - k)$:
  * $k = 0 \implies X(0) = \mathbf{10}$
  * $k = 1 \implies X(4 - 1) = X(3) = \mathbf{-2 - 2j}$
  * $k = 2 \implies X(4 - 2) = X(2) = \mathbf{-2}$
  * $k = 3 \implies X(4 - 3) = X(1) = \mathbf{-2 + 2j}$
  $$\mathbf{X_{\text{rev}}(k) = \{10, \; -2-2j, \; -2, \; -2+2j\}}$$

---

## 5. Circular Time Shift

### Formula:
$$x((n - l))_N \;\xleftrightarrow{\text{DFT}_N}\; X(k) \cdot e^{-j \frac{2\pi k l}{N}} = X(k) \cdot W_N^{kl}$$

### Plain-English Meaning:
Circularly shifting a sequence in time by $l$ positions **does not change its magnitude spectrum**; it only introduces a linear phase shift of $- \frac{2\pi kl}{N}$ radians at each frequency bin $k$.

### Numerical Example:
*(Direct past exam question: "Find DFT of $x((n-1))$ without calculating DFT")*
* Take $x(n) = \{1, 2, 3, 4\}$ circularly shifted by $l = 1 \implies x((n-1))_4 = \{4, 1, 2, 3\}$.
* The phase multiplication factor for $N = 4, l = 1$ is:
  $$e^{-j \frac{2\pi k (1)}{4}} = e^{-j \frac{\pi k}{2}} = (-j)^k$$
* Compute each bin:
  * $k = 0 \implies X(0) \cdot (-j)^0 = 10 \cdot 1 = \mathbf{10}$
  * $k = 1 \implies X(1) \cdot (-j)^1 = (-2 + 2j) \cdot (-j) = 2j - 2j^2 = \mathbf{2 + 2j}$
  * $k = 2 \implies X(2) \cdot (-j)^2 = -2 \cdot (-1) = \mathbf{2}$
  * $k = 3 \implies X(3) \cdot (-j)^3 = (-2 - 2j) \cdot (j) = -2j - 2j^2 = \mathbf{2 - 2j}$
$$\mathbf{X_{\text{shifted}}(k) = \{10, \; 2+2j, \; 2, \; 2-2j\}}$$

---

## 6. Circular Frequency Shift (Modulation)

### Formula:
$$x(n) \cdot e^{j \frac{2\pi l n}{N}} \;\xleftrightarrow{\text{DFT}_N}\; X((k - l))_N$$

### Plain-English Meaning:
Multiplying a time sequence by a complex exponential $e^{j \frac{2\pi ln}{N}}$ circularly shifts its entire DFT spectrum to the right by $l$ bins. (This is the discrete equivalent of frequency modulation).

### Numerical Example:
Let $l = 1$, $N = 4$. Multiply $x(n) = \{1, 2, 3, 4\}$ by $e^{j \frac{2\pi (1) n}{4}} = j^n$:
* $n = 0: 1 \cdot j^0 = \mathbf{1}$
* $n = 1: 2 \cdot j^1 = \mathbf{2j}$
* $n = 2: 3 \cdot j^2 = \mathbf{-3}$
* $n = 3: 4 \cdot j^3 = \mathbf{-4j}$
$$x_{\text{mod}}(n) = \{1, \; 2j, \; -3, \; -4j\}$$
* Its DFT is circularly shifted by $l = 1$ to the right: $X_{\text{mod}}(k) = X((k - 1))_4$:
  * $k = 0 \implies X((0 - 1))_4 = X(3) = \mathbf{-2 - 2j}$
  * $k = 1 \implies X((1 - 1))_4 = X(0) = \mathbf{10}$
  * $k = 2 \implies X((2 - 1))_4 = X(1) = \mathbf{-2 + 2j}$
  * $k = 3 \implies X((3 - 1))_4 = X(2) = \mathbf{-2}$
$$\mathbf{X_{\text{mod}}(k) = \{-2-2j, \; 10, \; -2+2j, \; -2\}}$$

---

## 7. Complex Conjugate

### Formula:
$$x^*(n) \;\xleftrightarrow{\text{DFT}_N}\; X^*((-k))_N = X^*(N - k)$$
$$x^*((-n))_N = x^*(N - n) \;\xleftrightarrow{\text{DFT}_N}\; X^*(k)$$

### Plain-English Meaning:
Taking the complex conjugate of a signal flips the signs of imaginary parts and reverses the frequency axis. 
* **Crucial consequence for real signals:** If $x(n)$ is purely real, $x^*(n) = x(n)$, which forces $X(k) = X^*(N - k)$ (**Hermitian / Conjugate Symmetry**). This is why the real part of $X(k)$ is symmetric, and the imaginary part is antisymmetric!

### Numerical Example:
Let $x(n) = \{1+j, \; 2, \; 3-j, \; 4\}$.
Then $x^*(n) = \{1-j, \; 2, \; 3+j, \; 4\}$.
* If $X(k) = \{X(0), X(1), X(2), X(3)\}$, then the DFT of $x^*(n)$ is:
  $$\mathbf{X_{\text{conj}}(k) = \{X^*(0), \; X^*(3), \; X^*(2), \; X^*(1)\}}$$

---

## 8. Circular Convolution

### Formula:
$$x_1(n) \mathbin{\textcircled{N}} x_2(n) \;\xleftrightarrow{\text{DFT}_N}\; X_1(k) \cdot X_2(k)$$
$$x_3(n) = \sum_{m=0}^{N-1} x_1(m) x_2((n - m))_N$$

### Plain-English Meaning:
Circular convolution in the time domain is equivalent to **simple point-by-point multiplication in the frequency domain**. This is the single most important property of DFT, enabling fast convolution using FFT algorithms.

### Numerical Example:
Let $x_1(n) = \{1, 2, 3, 4\}$ and $x_2(n) = \{1, 1, 2, 0\}$ ($N = 4$).
* $X_1(k) = \{10, \; -2+2j, \; -2, \; -2-2j\}$
* $X_2(k) = \{4, \; -1-j, \; 2, \; -1+j\}$
* Point-by-point product in frequency domain:
  * $k = 0: 10 \times 4 = \mathbf{40}$
  * $k = 1: (-2+2j)(-1-j) = 2 + 2j - 2j - 2j^2 = \mathbf{4}$
  * $k = 2: (-2) \times 2 = \mathbf{-4}$
  * $k = 3: (-2-2j)(-1+j) = \mathbf{4}$
  $$X_3(k) = \{40, \; 4, \; -4, \; 4\}$$
* Taking IDFT: $x_3(n) = \frac{1}{4} \sum_{k=0}^3 X_3(k) e^{j \frac{2\pi kn}{4}}$:
  $$\mathbf{x_3(n) = \{11, \; 11, \; 7, \; 11\}}$$
  *(Matches the circular matrix convolution $\begin{bmatrix} 1 & 0 & 2 & 1 \\ 1 & 1 & 0 & 2 \\ 2 & 1 & 1 & 0 \\ 0 & 2 & 1 & 1 \end{bmatrix} \begin{bmatrix} 1 \\ 2 \\ 3 \\ 4 \end{bmatrix} = \begin{bmatrix} 11 \\ 11 \\ 7 \\ 11 \end{bmatrix}$).*

---

## 9. Multiplication (Modulation / Dual of Convolution)

### Formula:
$$x_1(n) \cdot x_2(n) \;\xleftrightarrow{\text{DFT}_N}\; \frac{1}{N} \left[ X_1(k) \mathbin{\textcircled{N}} X_2(k) \right]$$

### Plain-English Meaning:
The exact dual of Property 8: Multiplying two signals sample-by-sample in the time domain results in the **circular convolution of their frequency spectra**, scaled by $\frac{1}{N}$.

### Numerical Example:
Let $x_1(n) = \{1, 2, 3, 4\}$ and $x_2(n) = \{1, 0, 1, 0\}$.
* Product in time: $y(n) = x_1(n) \cdot x_2(n) = \{1\cdot 1, \; 2\cdot 0, \; 3\cdot 1, \; 4\cdot 0\} = \mathbf{\{1, 0, 3, 0\}}$.
* Its direct DFT:
  * $Y(0) = 1 + 0 + 3 + 0 = \mathbf{4}$
  * $Y(1) = 1 - 3 = \mathbf{-2}$
  * $Y(2) = 1 + 3 = \mathbf{4}$
  * $Y(3) = 1 - 3 = \mathbf{-2}$
  $$\mathbf{Y(k) = \{4, -2, 4, -2\}}$$
* This exactly equals $\frac{1}{4} [X_1(k) \mathbin{\textcircled{4}} X_2(k)]$.

---

## 10. Parseval's Theorem (Conservation of Energy)

### Formula:
$$\sum_{n=0}^{N-1} x_1(n) x_2^*(n) = \frac{1}{N} \sum_{k=0}^{N-1} X_1(k) X_2^*(k)$$
For $x_1(n) = x_2(n) = x(n)$ (Total Signal Energy):
$$\mathbf{\sum_{n=0}^{N-1} |x(n)|^2 = \frac{1}{N} \sum_{k=0}^{N-1} |X(k)|^2}$$

### Plain-English Meaning:
Total signal energy is strictly conserved across domains. You can compute the total energy by summing the squared values in the time domain, or by summing the squared magnitudes in the frequency domain and dividing by $N$. Both give the exact same number.

### Numerical Example:
Take $x(n) = \{1, 2, 3, 4\}$ and $X(k) = \{10, \; -2+2j, \; -2, \; -2-2j\}$:
1. **Energy in Time Domain:**
   $$E = \sum_{n=0}^{3} |x(n)|^2 = 1^2 + 2^2 + 3^2 + 4^2 = 1 + 4 + 9 + 16 = \mathbf{30}$$
2. **Energy in Frequency Domain:**
   * $|X(0)|^2 = 10^2 = 100$
   * $|X(1)|^2 = (-2)^2 + (2)^2 = 4 + 4 = 8$
   * $|X(2)|^2 = (-2)^2 = 4$
   * $|X(3)|^2 = (-2)^2 + (-2)^2 = 4 + 4 = 8$
   $$\text{Sum} = 100 + 8 + 4 + 8 = 120$$
   Dividing by $N = 4$:
   $$E = \frac{1}{4} \times 120 = \mathbf{30}$$

Both sides yield **$30$**, proving Parseval's theorem.

---

### Summary Checklist for Exam Proofs

| No. | Property Name | Time Domain | DFT Domain | Common Exam Question |
| :---: | :--- | :--- | :--- | :--- |
| **1** | Linearity | $a x_1(n) + b x_2(n)$ | $a X_1(k) + b X_2(k)$ | Standard 2-mark proof |
| **2** | Periodicity | $x(n + N) = x(n)$ | $X(k + N) = X(k)$ | Index wrapping |
| **3** | Circular Representation | $x_p(n) = \sum x(n-lN)$ | Periodic sampling | Concept explanation |
| **4** | Time Reversal | $x((-n))_N$ | $X((-k))_N = X(N-k)$ | Reverse sequence DFT |
| **5** | Circular Time Shift | $x((n-l))_N$ | $X(k) W_N^{kl}$ | Find DFT without calculating |
| **6** | Circular Freq Shift | $x(n) W_N^{-ln}$ | $X((k-l))_N$ | Modulation proof |
| **7** | Complex Conjugate | $x^*(n)$ | $X^*(N-k)$ | Hermitian symmetry proof |
| **8** | Circular Convolution | $x_1(n) \mathbin{\textcircled{N}} x_2(n)$ | $X_1(k) X_2(k)$ | High-yield 5-mark proof |
| **9** | Multiplication | $x_1(n) x_2(n)$ | $\frac{1}{N} [X_1(k) \mathbin{\textcircled{N}} X_2(k)]$ | Dual of convolution |
| **10** | Parseval's Theorem | $\sum \Vert x(n)\Vert ^2$ | $\frac{1}{N} \sum \Vert X(k)\Vert ^2$ | Standard 5-mark proof |