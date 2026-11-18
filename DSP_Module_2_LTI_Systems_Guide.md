# Module 2: Analysis of Linear Time-Invariant (LTI) Systems
## Exam-Only Preparation Guide

> **Applied Hard Filters:**
> * ❌ **Completely Dropped:** Composite Radix FFT, Chebyshev-II, Elliptical Filters.
> * ⬇️ **Filtered Out (Per Instructions):** Digital Resonators, Digital Sinusoidal Oscillators, Chebyshev-I.

---

# Topic 1: Effect of Poles and Zeros on Frequency Response & Filter Classification

### Question 1.1 (PYQ)
* **Exam:** Final Examination (Academic Year 2024–2025)
* **Paper / Question:** [QP_Final-Exam_Digital Signal Processing(DJS22EC504)_Semester V_2024-2025.pdf](./Sem-V%20QP%20Misc/QP_Final-Exam_Digital%20Signal%20Processing%28DJS22EC504%29_Semester%20V_2024-2025.pdf) — **Q1.b.i (10 Marks)**
* **Official Answer PDF:** [ANS_Final-Exam_Digital Signal Processing(DJS22EC504)_Semester V_2024-2025.pdf](./Sem-V%20QP%20Misc/ANS_Final-Exam_Digital%20Signal%20Processing%28DJS22EC504%29_Semester%20V_2024-2025.pdf) *(Pages 1–3)*
* **Question Statement:**
  > *"Explain the impact of poles and zeros on IIR filter. Identify the type of filter described by system function as:*
  > $$H(z) = \frac{z^{-1} - c_1}{1 - c_1 z^{-1}}$$
  > *where $c_1$ and $c_2$ are constants. Also justify your answer."*

#### Step-by-Step Mathematical Solution:

#### 1. Impact of Poles and Zeros on Frequency Response
Given a general rational transfer function:
$$H(z) = K \frac{\prod_{m=1}^M (z - z_m)}{\prod_{k=1}^N (z - p_k)}$$

Evaluating on the unit circle $z = e^{j\omega}$, the frequency response is represented geometrically by vectors from the zeros and poles to a point $e^{j\omega}$:
$$|H(e^{j\omega})| = |K| \frac{\prod_{m=1}^M |e^{j\omega} - z_m|}{\prod_{k=1}^N |e^{j\omega} - p_k|} = |K| \frac{\prod V_m(\omega)}{\prod U_k(\omega)}$$
$$\angle H(e^{j\omega}) = \sum_{m=1}^M \angle(e^{j\omega} - z_m) - \sum_{k=1}^N \angle(e^{j\omega} - p_k)$$

* **Impact of Poles ($p_k$):**
  * As the frequency point $e^{j\omega}$ approaches a pole $p_k$, the distance vector $U_k(\omega) \to 0$, causing the magnitude $|H(e^{j\omega})|$ to **peak / amplify**.
  * Placing poles close to the unit circle inside the left half creates sharp passbands or resonant peaks.
  * **Stability Constraint:** For causal stability, all poles must lie strictly inside the unit circle ($|p_k| < 1$).
* **Impact of Zeros ($z_m$):**
  * As $e^{j\omega}$ approaches a zero $z_m$, the distance vector $V_m(\omega) \to 0$, causing the magnitude $|H(e^{j\omega})|$ to **drop / attenuate**.
  * Placing a zero directly on the unit circle ($z_m = e^{j\omega_0}$) introduces a **transmission null / notch** ($|H(e^{j\omega_0})| = 0$).

---

#### 2. Identification and Proof of $H(z) = \frac{z^{-1} - c_1}{1 - c_1 z^{-1}}$
* **Pole-Zero Locations:**
  * Zero: $z^{-1} - c_1 = 0 \implies \mathbf{z_{\text{zero}} = \frac{1}{c_1}}$
  * Pole: $1 - c_1 z^{-1} = 0 \implies \mathbf{z_{\text{pole}} = c_1}$
  * The pole and zero lie at **conjugate reciprocal locations** with respect to the unit circle ($z_{\text{zero}} = \frac{1}{z_{\text{pole}}^*}$).
* **Magnitude Response Evaluation ($z = e^{j\omega}$):**
  $$H(e^{j\omega}) = \frac{e^{-j\omega} - c_1}{1 - c_1 e^{-j\omega}} = \frac{e^{-j\omega}(1 - c_1 e^{j\omega})}{1 - c_1 e^{-j\omega}}$$
  Taking the magnitude:
  $$|H(e^{j\omega})| = |e^{-j\omega}| \cdot \frac{|1 - c_1 e^{j\omega}|}{|1 - c_1 e^{-j\omega}|}$$
  Since $1 - c_1 e^{j\omega}$ and $1 - c_1 e^{-j\omega}$ are complex conjugates of each other, their magnitudes are identical ($|A| = |A^*|$):
  $$\mathbf{|H(e^{j\omega})| = 1 \cdot \frac{|1 - c_1 e^{j\omega}|}{|1 - c_1 e^{j\omega}|} = 1 \quad \text{for all } \omega}$$
* **Conclusion & Justification:**
  The system is an **All-Pass Filter**. It passes all frequency components with unity gain ($|H(e^{j\omega})| = 1$) while introducing a frequency-dependent phase delay used for phase equalization.

---

### Question 1.2 (Targeted Model Question — Pole-Zero Placement Rules)
* **Syllabus Topic:** *Position of Poles and Zeros for Low Pass, High Pass, Band Pass, Band Stop filters*
* **Question Statement:**
  > *"State the pole-zero placement rules on the Z-plane for designing Lowpass, Highpass, Bandpass, and Bandstop digital filters. Sketch their pole-zero patterns."*

#### Step-by-Step Mathematical Solution:

| Filter Type | Zero Locations ($z_m$) | Pole Locations ($p_k$) | Geometric Reason |
| :--- | :--- | :--- | :--- |
| **Lowpass (LPF)** | Zeros placed at or near $z = -1$ ($\omega = \pi$). | Poles placed inside unit circle near $z = +1$ ($\omega = 0$). | Distance to zeros is minimized at $\pi$ (maximum attenuation); distance to poles is minimized at $0$ (high gain). |
| **Highpass (HPF)** | Zeros placed at or near $z = +1$ ($\omega = 0$, DC null). | Poles placed inside unit circle near $z = -1$ ($\omega = \pi$). | Null at $\omega = 0$; resonance peak at $\omega = \pi$. |
| **Bandpass (BPF)** | Zeros placed at both $z = +1$ ($\omega = 0$) and $z = -1$ ($\omega = \pi$). | Complex conjugate poles at $p_{1,2} = r e^{\pm j\omega_0}$ ($0 < \omega_0 < \pi$). | Rejection at DC and Nyquist; selective amplification around passband center $\omega_0$. |
| **Bandstop (BSF)** | Complex conjugate zeros directly on unit circle at $z_{1,2} = e^{\pm j\omega_0}$. | Poles placed at same angle $\omega_0$ at radius $r < 1$ ($p_{1,2} = r e^{\pm j\omega_0}$). | Exact transmission null at $\omega_0$; poles confine attenuation to a narrow notch band. |

```
     Lowpass (LPF)               Highpass (HPF)               Bandpass (BPF)
         Im                          Im                          Im
          |                           |                           |
       x  |                        x  |                     x     |     x
     (pole)                       (pole)                  (pole)  |   (pole)
   -------+---o---> Re         ---o---+-------> Re     ---o-------+-------o---> Re
          | (zero at -1)   (zero at +1)   (pole)      (zero at -1)|(zero at +1)
       x  |                        x  |                           |
```

---

# Topic 2: Second-Order Notch Filter Design

### Question 2.1 (PYQ)
* **Exam:** Final Examination (Academic Year 2025–2026)
* **Paper / Question:** [QP-Sem-V-EXTC-Digital Signal Processing.pdf](./QP-Sem-V-EXTC-Digital%20Signal%20Processing.pdf) — **Q2.b.i (7 Marks)**
* **Official Answer PDF:** [ANS-Sem-V-EXTC-Digital Signal Processing.pdf](./ANS-Sem-V-EXTC-Digital%20Signal%20Processing.pdf) *(Pages 3–4)*
* **Question Statement:**
  > *"Design a second-order notch filter with a notch at center frequency = 120 Hz. Take distance of pole from origin is 0.98. Assume a sampling rate of 600 samples/second."*

#### Step-by-Step Mathematical Solution:

#### Step 1: Calculate Digital Notch Frequency $\omega_0$
$$\omega_0 = \frac{2\pi f_0}{f_s} = \frac{2\pi \times 120}{600} = \frac{2\pi}{5}\text{ rad} = 0.4\pi\text{ rad} = 72^\circ$$
$$\cos(\omega_0) = \cos(72^\circ) = \frac{\sqrt{5} - 1}{4} \approx 0.309017$$

#### Step 2: Zero Placement (Perfect Null at $\omega_0$)
Place complex conjugate zeros on the unit circle at angle $\pm \omega_0$:
$$z_{1,2} = e^{\pm j \omega_0} = e^{\pm j \frac{2\pi}{5}}$$
$$N(z) = (z - e^{j\omega_0})(z - e^{-j\omega_0}) = z^2 - 2\cos(\omega_0)z + 1$$
$$N(z) = z^2 - 2(0.309017)z + 1 = \mathbf{z^2 - 0.6180 z + 1}$$
In negative powers of $z$:
$$N(z) = 1 - 0.6180 z^{-1} + z^{-2}$$

#### Step 3: Pole Placement (Narrow Notch Bandwidth)
Place poles at the same angle $\pm \omega_0$ at radius $r = 0.98$:
$$p_{1,2} = r e^{\pm j \omega_0} = 0.98 e^{\pm j \frac{2\pi}{5}}$$
$$D(z) = (z - r e^{j\omega_0})(z - r e^{-j\omega_0}) = z^2 - 2r\cos(\omega_0)z + r^2$$
$$2r\cos(\omega_0) = 2(0.98)(0.309017) \approx 0.6057$$
$$r^2 = (0.98)^2 = 0.9604$$
$$D(z) = \mathbf{z^2 - 0.6057 z + 0.9604} = 1 - 0.6057 z^{-1} + 0.9604 z^{-2}$$

#### Step 4: Transfer Function $H(z)$
$$\mathbf{H(z) = \frac{z^2 - 0.6180 z + 1}{z^2 - 0.6057 z + 0.9604} = \frac{1 - 0.6180 z^{-1} + z^{-2}}{1 - 0.6057 z^{-1} + 0.9604 z^{-2}}}$$

#### Step 5: Difference Equation & 3-dB Bandwidth
From $Y(z)[1 - 0.6057 z^{-1} + 0.9604 z^{-2}] = X(z)[1 - 0.6180 z^{-1} + z^{-2}]$:
$$\mathbf{y(n) = 0.6057 y(n-1) - 0.9604 y(n-2) + x(n) - 0.6180 x(n-1) + x(n-2)}$$

* **3-dB Bandwidth:**
  $$\Delta \omega_{3\text{dB}} \approx 2(1 - r) = 2(1 - 0.98) = 0.04\text{ rad}$$
  $$\Delta f_{3\text{dB}} = \frac{\Delta \omega_{3\text{dB}} \cdot f_s}{2\pi} = \frac{0.04 \times 600}{2\pi} \approx \mathbf{3.82\text{ Hz}}$$

---

# Topic 3: Comb Filter Design (FIR and IIR)

### Question 3.1 (Targeted Model Question — Comb Filter Design)
* **Syllabus Topic:** *Comb Filters*
* **Question Statement:**
  > *"Derive the transfer function, pole-zero plot, and magnitude response of:*
  > *(a) An FIR Comb Filter with periodic nulls,*
  > *(b) An IIR Comb Filter with periodic sharp peaks.*
  > *State how the notch frequencies are determined by delay parameter $L$."*

#### Step-by-Step Mathematical Solution:

#### 1. FIR Comb Filter (Periodic Rejection / Notching)
* **Transfer Function:**
  $$H(z) = 1 - z^{-L}$$
* **Zeros:**
  Solve $1 - z^{-L} = 0 \implies z^L = 1 = e^{j 2\pi k}$:
  $$\mathbf{z_k = e^{j \frac{2\pi k}{L}}, \quad k = 0, 1, 2, \dots, L-1}$$
  $H(z)$ has $L$ zeros evenly distributed around the unit circle at intervals of $\frac{2\pi}{L}$.
* **Frequency Response:**
  $$H(e^{j\omega}) = 1 - e^{-j\omega L} = e^{-j\frac{\omega L}{2}} \left( e^{j\frac{\omega L}{2}} - e^{-j\frac{\omega L}{2}} \right) = 2j e^{-j\frac{\omega L}{2}} \sin\left(\frac{\omega L}{2}\right)$$
  $$|H(e^{j\omega})| = 2 \left|\sin\left(\frac{\omega L}{2}\right)\right|$$
* **Notch Frequencies (Nulls):**
  Nulls occur where $\sin\left(\frac{\omega L}{2}\right) = 0 \implies \mathbf{\omega_k = \frac{2\pi k}{L}}$.
  At these frequencies, $|H(e^{j\omega_k})| = 0$, rejecting all harmonics of base frequency $f_0 = \frac{f_s}{L}$.

---

#### 2. IIR Comb Filter (Periodic Resonances with Narrow Peaks)
* **Transfer Function:**
  To convert broad sinusoidal notches into sharp passband teeth or sharp notches, introduce poles at radius $\alpha < 1$:
  $$H(z) = \frac{1 - z^{-L}}{1 - \alpha z^{-L}}, \quad 0 < \alpha < 1$$
* **Poles and Zeros:**
  * Zeros: $z_k = e^{j \frac{2\pi k}{L}}$ (on unit circle).
  * Poles: $p_k = \alpha^{1/L} e^{j \frac{2\pi k}{L}}$ (inside unit circle at same angles).
* **Magnitude Characteristic:**
  * Away from nulls: $|H(e^{j\omega})| \approx 1$.
  * Exactly at $\omega_k = \frac{2\pi k}{L}$: $|H(e^{j\omega_k})| = 0$ with narrow 3-dB notch bandwidth controlled by $\alpha$:
    $$\Delta \omega \approx \frac{2(1 - \alpha)}{L}$$

---

# Topic 4: All-Pass Systems and Phase Equalization

### Question 4.1 (Targeted Model Question — All-Pass Characteristics & Decomposition)
* **Syllabus Topic:** *All-Pass Filters & Minimum-Phase/All-Pass Decomposition*
* **Question Statement:**
  > *"State the general transfer function of an $N$-th order All-Pass filter. Prove that its magnitude is unity for all frequencies and explain how any non-minimum phase system can be decomposed into a minimum phase system cascaded with an all-pass system."*

#### Step-by-Step Mathematical Solution:

#### 1. General Transfer Function of All-Pass System
An $N$-th order all-pass system with poles $p_k$ strictly inside the unit circle ($|p_k| < 1$) has transfer function:
$$H_{\text{ap}}(z) = \prod_{k=1}^N \frac{z^{-1} - p_k^*}{1 - p_k z^{-1}} = \frac{z^{-N} A^*(z^{-1})}{A(z)}$$
where each pole at $p_k$ has a paired zero at conjugate reciprocal location $z_k = \frac{1}{p_k^*}$.

#### 2. Proof of Unity Magnitude Response
For each section:
$$H_k(e^{j\omega}) = \frac{e^{-j\omega} - p_k^*}{1 - p_k e^{-j\omega}} = e^{-j\omega} \frac{1 - p_k^* e^{j\omega}}{1 - p_k e^{-j\omega}}$$
Notice that the numerator $(1 - p_k^* e^{j\omega})$ is the complex conjugate of the denominator $(1 - p_k e^{-j\omega})$.
Since $|W| = |W^*|$ for any complex number:
$$|H_k(e^{j\omega})| = |e^{-j\omega}| \cdot \frac{|1 - p_k^* e^{j\omega}|}{|1 - p_k e^{-j\omega}|} = 1 \cdot 1 = 1 \quad \text{for all } \omega$$
Therefore:
$$\mathbf{|H_{\text{ap}}(e^{j\omega})| = \prod_{k=1}^N |H_k(e^{j\omega})| = 1 \quad \text{for all } \omega}$$

#### 3. Minimum-Phase and All-Pass Decomposition
Any causal, stable non-minimum phase filter $H(z)$ containing zeros $z_i$ outside the unit circle ($|z_i| > 1$) can be uniquely factored as:
$$\mathbf{H(z) = H_{\text{min}}(z) \cdot H_{\text{ap}}(z)}$$
* To flip an unstable zero $z_i$ ($|z_i| > 1$) into the unit circle at $\frac{1}{z_i^*}$ without changing the filter's magnitude response:
  $$(1 - z_i z^{-1}) = \underbrace{\left(1 - \frac{1}{z_i^*} z^{-1}\right)}_{\text{Minimum Phase Zero}} \cdot \underbrace{\left( \frac{z^{-1} - z_i^*}{1 - \frac{1}{z_i^*} z^{-1}} \right) (-z_i)}_{\text{All-Pass Section}}$$
* **Result:** $|H(e^{j\omega})| = |H_{\text{min}}(e^{j\omega})|$. The all-pass filter only alters the phase, allowing phase equalization without affecting magnitude response.

---

# Topic 5: Minimum-Phase, Maximum-Phase, and Mixed-Phase Systems

### Question 5.1 (PYQ)
* **Exam:** Final Examination (January 2023)
* **Paper / Question:** [Digital Signal Processing QP.pdf](./Sem-V%20QP%20Misc/Digital%20Signal%20Processing%20QP.pdf) — **Q3.a (7 Marks)**
* **Question Statement:**
  > *"Determine the zeros of the following FIR systems and indicate whether the system is minimum phase, maximum phase or mixed phase:*
  > *(i) $H_1(z) = 1 + 2z^{-1} - 6z^{-2}$*
  > *(ii) $H_2(z) = 1 - 2z^{-1} - 6z^{-2}$*
  > *Comment on the stability of the minimum and maximum phase system."*

#### Step-by-Step Mathematical Solution:

#### 1. System (i): $H_1(z) = 1 + 2z^{-1} - 6z^{-2} = \frac{z^2 + 2z - 6}{z^2}$
* Poles: Two poles at $z = 0$ (origin).
* Zeros: Solve $z^2 + 2z - 6 = 0$:
  $$z = \frac{-2 \pm \sqrt{2^2 - 4(1)(-6)}}{2} = \frac{-2 \pm \sqrt{28}}{2} = -1 \pm \sqrt{7} \approx -1 \pm 2.6458$$
  $$z_{1} = -1 + 2.6458 = \mathbf{+1.6458} \implies |z_1| = 1.6458 > 1 \quad (\text{Outside unit circle})$$
  $$z_{2} = -1 - 2.6458 = \mathbf{-3.6458} \implies |z_2| = 3.6458 > 1 \quad (\text{Outside unit circle})$$
* **Classification:** Since **all zeros lie strictly outside the unit circle**, $H_1(z)$ is a **Maximum-Phase System**.

---

#### 2. System (ii): $H_2(z) = 1 - 2z^{-1} - 6z^{-2} = \frac{z^2 - 2z - 6}{z^2}$
* Poles: Two poles at $z = 0$ (origin).
* Zeros: Solve $z^2 - 2z - 6 = 0$:
  $$z = \frac{2 \pm \sqrt{(-2)^2 - 4(1)(-6)}}{2} = \frac{2 \pm \sqrt{28}}{2} = 1 \pm \sqrt{7} \approx 1 \pm 2.6458$$
  $$z_{1} = 1 + 2.6458 = \mathbf{+3.6458} \implies |z_1| = 3.6458 > 1 \quad (\text{Outside unit circle})$$
  $$z_{2} = 1 - 2.6458 = \mathbf{-1.6458} \implies |z_2| = 1.6458 > 1 \quad (\text{Outside unit circle})$$
* **Classification:** Since **all zeros lie strictly outside the unit circle**, $H_2(z)$ is also a **Maximum-Phase System**.

---

#### 3. Stability Comparison
* In causal FIR filters, all poles are at the origin ($z = 0$). Because $|z_{\text{pole}}| = 0 < 1$, **all causal FIR systems are unconditionally stable**, regardless of whether they are minimum-phase, maximum-phase, or mixed-phase.
* **The Critical Difference (Inverse System Stability):**
  * For $H(z)$, its inverse filter is $H^{-1}(z) = \frac{1}{H(z)}$.
  * The zeros of $H(z)$ become the poles of $H^{-1}(z)$.
  * If $H(z)$ is **minimum-phase** (zeros inside unit circle), $H^{-1}(z)$ has its poles inside the unit circle and is **stable and causal**.
  * If $H(z)$ is **maximum-phase or mixed-phase**, $H^{-1}(z)$ will have poles outside the unit circle, making its causal inverse **unstable**.

---

### Question 5.2 (PYQ)
* **Exam:** Re-Examination (Academic Year 2025–2026)
* **Paper / Question:** [QP_Re-Exam_Digital Signal Processing(DJS23ECPC501)_Semester V_2025-2026.pdf](./Sem-V%20QP%20Misc/sem%205%20last%20year%20reexam/Digital%20Signal%20Processing/QP_Re-Exam_Digital%20Signal%20Processing%28DJS23ECPC501%29_Semester%20V_2025-2026.pdf) — **Q2.b.ii (7 Marks)**
* **Official Answer PDF:** [ANS_Re-Exam_Digital Signal Processing(DJS23ECPC501)_Semester V_2025-2026.pdf](./Sem-V%20QP%20Misc/sem%205%20last%20year%20reexam/Digital%20Signal%20Processing/ANS_Re-Exam_Digital%20Signal%20Processing%28DJS23ECPC501%29_Semester%20V_2025-2026.pdf)
* **Question Statement:**
  > *"The pole-zero plot of a system has zeros at $z = 0.5$ and $z = 2$, with two poles at $z = 0$. Determine:*
  > *(a) Whether the filter is FIR or IIR,*
  > *(b) Whether the filter is Lowpass, Highpass, Bandpass, or Bandstop,*
  > *(c) Whether it is Minimum-phase, Maximum-phase, or Mixed-phase system."*

#### Step-by-Step Mathematical Solution:
1. **Transfer Function:**
   $$H(z) = (1 - 0.5z^{-1})(1 - 2z^{-1}) = 1 - 2.5z^{-1} + z^{-2} = \frac{z^2 - 2.5z + 1}{z^2}$$
2. **Part (a): FIR or IIR Filter?**
   * All poles are located strictly at the origin ($z = 0$). There are no non-zero finite denominator poles.
   * **Answer:** It is an **FIR Filter**.
3. **Part (b): Filter Frequency Selective Nature:**
   * Evaluate at DC ($\omega = 0 \implies z = 1$):
     $$H(1) = (1 - 0.5)(1 - 2) = (0.5)(-1) = -0.5 \implies |H(e^{j0})| = 0.5$$
   * Evaluate at Nyquist ($\omega = \pi \implies z = -1$):
     $$H(-1) = (1 + 0.5)(1 + 2) = (1.5)(3) = 4.5 \implies |H(e^{j\pi})| = 4.5$$
   * Gain increases monotonically from $0.5$ at $\omega = 0$ to $4.5$ at $\omega = \pi$.
   * **Answer:** It is a **Highpass Filter**.
4. **Part (c): Phase Classification:**
   * Zero 1: $z_1 = 0.5 \implies |z_1| = 0.5 < 1$ (**inside unit circle**).
   * Zero 2: $z_2 = 2.0 \implies |z_2| = 2.0 > 1$ (**outside unit circle**).
   * **Answer:** Since zeros exist both inside and outside the unit circle, it is a **Mixed-Phase System**.

---

# Topic 6: Ideal Filter Characteristics & Paley-Wiener Theorem

### Question 6.1 (Targeted Model Question — Causality & Realizability of Ideal Filters)
* **Syllabus Topic:** *Ideal Filter Characteristics & Paley-Wiener Causality Theorem*
* **Question Statement:**
  > *"Explain why an ideal brick-wall lowpass filter is non-causal and physically unrealizable. State the Paley-Wiener theorem criterion and explain its physical significance in filter design."*

#### Step-by-Step Mathematical Solution:

#### 1. Ideal Lowpass Filter Impulse Response
An ideal brick-wall lowpass filter has frequency response:
$$H_d(e^{j\omega}) = \begin{cases} 1, & |\omega| \le \omega_c \\ 0, & \omega_c < |\omega| \le \pi \end{cases}$$

Taking the Inverse Discrete-Time Fourier Transform (IDTFT):
$$h_d(n) = \frac{1}{2\pi} \int_{-\omega_c}^{\omega_c} 1 \cdot e^{j\omega n} d\omega = \frac{1}{2\pi} \left[ \frac{e^{j\omega n}}{jn} \right]_{-\omega_c}^{\omega_c} = \frac{\sin(\omega_c n)}{\pi n} = \frac{\omega_c}{\pi} \text{sinc}\left(\frac{\omega_c n}{\pi}\right)$$

* **Non-Causality:** The $\text{sinc}$ function extends indefinitely from $n = -\infty$ to $n = +\infty$. Since $h_d(n) \ne 0$ for $n < 0$, the filter requires knowledge of future inputs, making it **physically unrealizable in real-time**.

---

#### 2. Paley-Wiener Causality Theorem
For an LTI system with frequency response $H(e^{j\omega})$ to be causal and have a square-integrable impulse response ($\sum |h(n)|^2 < \infty$), the magnitude response must satisfy the **Paley-Wiener Criterion**:
$$\mathbf{\int_{-\pi}^{\pi} |\ln |H(e^{j\omega})|| \, d\omega < \infty}$$
*(In analog continuous-time domains: $\int_{-\infty}^{\infty} \frac{|\ln |H(j\Omega)||}{1 + \Omega^2} d\Omega < \infty$)*

#### 3. Physical Significance in Filter Design:
1. **No Infinite Stopband Attenuation:**
   If a filter has an ideal stopband where $|H(e^{j\omega})| = 0$ over a finite band of frequencies, then $\ln |H(e^{j\omega})| = \ln(0) = -\infty$.
   The integral over that interval evaluates to $-\infty$, **violating the Paley-Wiener theorem**.
2. **Transition Band Requirement:**
   The filter magnitude $|H(e^{j\omega})|$ can drop to zero at discrete frequencies (isolated nulls), but **cannot be zero over any continuous band of non-zero width**.
3. **Implication:** Any physically realizable causal digital filter must have:
   * A non-zero transition band with a finite transition slope.
   * Finite (non-infinite) attenuation in the stopband (e.g., stopband ripple).

---

### Master Topic Summary Checklist

```
+---------------------------------------------------------------------------------------------------------+
| Topic                       | Governing Equation / Rule                     | Exam Classification Key   |
+---------------------------------------------------------------------------------------------------------+
| Pole/Zero Frequency Impact  | |H(\omega)| = K \prod |e^{j\omega}-z_m| / \prod |e^{j\omega}-p_k|      | Zero=Null, Pole=Peak      |
| All-Pass Transfer Function  | H(z) = (z^{-1} - a*) / (1 - a z^{-1})         | |H(e^{j\omega})| = 1      |
| Notch Filter Transfer Func  | H(z) = (1 - 2cos\omega_0 z^{-1} + z^{-2}) /   | Zeros on circle (r=1)     |
|                             |        (1 - 2r cos\omega_0 z^{-1} + r^2 z^{-2})| Poles inside (r < 1)      |
| Notch 3-dB Bandwidth        | \Delta \omega_{3dB} \approx 2(1 - r)          | BW in Hz = \Delta\omega f_s / 2\pi |
| FIR Comb Filter (Nulls)     | H(z) = 1 - z^{-L}                             | Zeros at \omega_k = 2\pi k / L |
| Minimum Phase System        | All zeros strictly INSIDE unit circle (|z|<1) | Causal & stable inverse   |
| Maximum Phase System        | All zeros strictly OUTSIDE unit circle (|z|>1)| Causal inverse unstable   |
| Mixed Phase System          | Zeros both INSIDE and OUTSIDE unit circle     | Standard linear-phase FIR |
| Paley-Wiener Criterion      | \int_{-\pi}^\pi |\ln |H(e^{j\omega})|| d\omega < \infty | No brick-wall stopbands   |
+---------------------------------------------------------------------------------------------------------+
```