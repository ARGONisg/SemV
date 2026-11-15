# Prof. Santosh WTRFD Final Exam Blueprint, Analysis & Full Transcript
**Course:** Wave Theory and Radio Frequency Design (`DJS23ECPC502` / `DJS23EPC502`)  
**Program:** B.Tech EXTC, Semester V — DJSCE  
**Document Purpose:** Complete faculty exam blueprint, question templates, elimination list, and verbatim audio call transcript.

---

## Part 1: Comprehensive Exam Blueprint & Analysis

### 1. Overall Paper Structure (60 Marks Total)
* **Section 1: Electromagnetism (30 Marks)** — Questions 1 & 2
* **Section 2: RF Engineering & Transmission Lines (30 Marks)** — Questions 3 & 4
* **Mark Pattern per Question:** $15\text{ Marks}$ each, split into $5\text{ Marks}$ (compulsory sub-question) and $10\text{ Marks}$ (with internal choice: `(i) OR (ii)`).

```
[WTRFD Final Exam: 60 Marks]
  ├── SECTION 1: ELECTROMAGNETISM (30 Marks)
  │     ├── Q1 (15 Marks): Electrostatics
  │     │     ├── Part A (5 Marks): Basic Electrostatics (Point + Line + Sheet Charge combination)
  │     │     └── Part B (10 Marks with Option): E-field Derivation OR Electrostatic Energy / Divergence
  │     │
  │     └── Q2 (15 Marks): Magnetostatics, Time-Varying Fields & Waves
  │           ├── Part A (5 Marks): Basic Magnetostatics (Biot-Savart / Ampere's Law)
  │           └── Part B (10 Marks with Option): Maxwell Derivation / Boundary Condition / Plane Waves
  │
  └── SECTION 2: RF ENGINEERING & TRANSMISSION LINES (30 Marks)
        ├── Q3 (15 Marks): Smith Chart & Transmission Lines
        │     ├── Part A (5 Marks): Basic Smith Chart Plotting (z_L, SWR circle, Gamma, VSWR, y_L)
        │     └── Part B (10 Marks with Option): Transmission Line Zin (Smith + Analytical) OR LC Matching
        │
        └── Q4 (15 Marks): RF Passives & Filter Design
              ├── Part A (5 Marks): Butterworth Low-Pass Filter Design (Insertion Loss Method ONLY)
              └── Part B (10 Marks with Option): High-Frequency Resistor / Capacitor (7–8 Point Table)
```

---

### 2. The "Zero-Fluff" Elimination List (What NOT to Study)
Prof. Santosh explicitly eliminated the following topics from the final examination:
1. ❌ **NO Stub Matching** on Smith Chart (*"Stub matching nahi, stub matching nahi"*).
2. ❌ **NO Image Parameter Method** ($k$-constant, $m$-derived) for filter design (*"Image parameter nahi hai, wo tumko nahi hai"*).
3. ❌ **NO Chebyshev, Elliptic, High-Pass, Bandpass, or Bandstop Filters!**  
   Only **Butterworth (Maximally Flat / Binomial) Low-Pass Filter** (*"Na high pass hai, na band pass, na band stop... Sirf Butterworth Low Pass"*).
4. ❌ **NO Transmission Line theoretical derivations** (*"Transmission line ka derivation? Nahi"*).
5. ❌ **NO S-Parameters or ABCD Parameter questions** (*"Skip kar sakte ho filhal"*).
6. ❌ **NO Solenoid / Toroid derivations**.
7. ❌ **NO Separate Coaxial Cable skin depth derivations** (skin depth is only applied inside the RF passives resistor model).

---

### 3. Detailed Question-by-Question Templates

#### Question 1 (15 Marks): Electrostatics
* **Part A (5 Marks): Combined Field Calculation**
  * Find resultant $\vec{E}$ at a given coordinate due to a simultaneous combination of:
    1. Point Charge: $\vec{E}_1 = \frac{Q}{4\pi\epsilon R^2} \hat{a}_R$
    2. Infinite Line Charge: $\vec{E}_2 = \frac{\rho_L}{2\pi\epsilon\rho} \hat{a}_\rho$
    3. Infinite Sheet Charge: $\vec{E}_3 = \frac{\rho_s}{2\epsilon} \hat{a}_n$
    * Resultant: $\vec{E}_{total} = \vec{E}_1 + \vec{E}_2 + \vec{E}_3$.
* **Part B (10 Marks with Option):**
  * **Option 1 (Derivation):** Derive electric field intensity $\vec{E}$ due to an infinite line charge of uniform density $\rho_L$ (using Coulomb's law or Gauss's law) or infinite sheet charge $\rho_s$.
  * **Option 2 (TT1 Problem - Energy / Divergence):**
    * *Divergence Theorem:* Given $\vec{D} = 3r^2 \hat{a}_r\text{ C/m}^2$, verify divergence theorem $\oint \vec{D} \cdot d\vec{S} = \int (\nabla \cdot \vec{D}) dV$ on spherical shell between $r=1\text{ m}$ and $r=2\text{ m}$.
    * *Stored Electrostatic Energy:* Given electric potential $V(x, y, z) = 4x^2 + 5y^2 + 2z^2\text{ V}$, compute $\vec{E} = -\nabla V = -(8x\hat{a}_x + 10y\hat{a}_y + 4z\hat{a}_z)$, then integrate total energy $W_E = \frac{1}{2}\epsilon \int |\vec{E}|^2 dV$ over the unit cube $0 \le x, y, z \le 1$.

#### Question 2 (15 Marks): Magnetostatics & Waves
* **Part A (5 Marks): Basic Magnetostatics**
  * Biot-Savart Law formulation. Calculate $\vec{H}$ at a point due to:
    * Infinite filament: $H = \frac{I}{2\pi\rho}\hat{a}_\phi$
    * Finite filament: $H = \frac{I}{4\pi\rho}(\sin\alpha_2 - \sin\alpha_1)\hat{a}_\phi$
* **Part B (10 Marks with Option):**
  * **Option 1 (Maxwell's Derivations):** Complete derivation of all 4 Maxwell's equations in differential and integral forms, focusing on Ampere's circuital law inconsistency and Maxwell's displacement current correction ($\vec{J}_d = \frac{\partial\vec{D}}{\partial t}$).
  * **Option 2 (TT2 Boundary Condition Problem):**
    * Given magnetic boundary interface normal to one axis:
      $$\vec{B}_1 = \mu_0(43.5\hat{a}_x + 24.0\hat{a}_z), \quad \vec{B}_2 = \mu_0(22.0\hat{a}_x + 24.0\hat{a}_z)$$
    * Identify normal component ($B_n = 24.0\mu_0\hat{a}_z$) and tangential components ($B_{t1} = 43.5\mu_0\hat{a}_x, B_{t2} = 22.0\mu_0\hat{a}_x$).
    * Use boundary condition $\frac{\tan\theta_1}{\tan\theta_2} = \frac{B_{t1} / B_{n1}}{B_{t2} / B_{n2}} = \frac{43.5}{22.0} \approx 1.977$.
  * **Option 3 (TT2 Plane Wave / Curl Problem):**
    * Given $\vec{B} = B_m e^{j(\omega t + \beta z)}\hat{a}_y$, use Maxwell's curl equation $\nabla \times \vec{H} = \epsilon_0 \frac{\partial\vec{E}}{\partial t}$ in free space to show $\vec{E} = -\frac{\omega B_m}{\beta}e^{j(\omega t + \beta z)}\hat{a}_x$.
    * Plane wave in lossy dielectrics: Calculate $\alpha, \beta, \gamma, \eta, v_p, \tan\theta$.

#### Question 3 (15 Marks): Smith Chart & Transmission Lines
* **Part A (5 Marks): Basic Smith Chart Plotting**
  * Given $Z_L$ (e.g. $120 - j140\,\Omega$) and $Z_0 = 50\,\Omega$.
  * Normalize $z_L = Z_L / Z_0 = 2.4 - j2.8$.
  * Plot $z_L$ on Smith Chart, draw constant-SWR circle centered at $(1, 0)$.
  * Read reflection coefficient magnitude $|\Gamma|$ and angle $\angle\Gamma$ on peripheral scale.
  * Read VSWR $S$ directly from right-hand intersection of SWR circle with horizontal real axis.
  * Find load admittance $y_L$ by drawing straight line through center to opposite side of SWR circle ($180^\circ$ shift).
* **Part B (10 Marks with Option):**
  * **Option 1 (TT2 Question 2b — $Z_{in}$ Determination & Verification):**
    * Transmission line: $Z_0 = 50\,\Omega$, length $l = 85\text{ cm}$, $\epsilon_r = 2.1$, $f = 2\text{ GHz}$, $Z_L = 120 - j140\,\Omega$.
    * Compute wave velocity $v_p = \frac{c}{\sqrt{\epsilon_r}} = \frac{3 \times 10^8}{\sqrt{2.1}} = 2.07 \times 10^8\text{ m/s}$.
    * Compute wavelength $\lambda = \frac{v_p}{f} = \frac{2.07 \times 10^8}{2 \times 10^9} = 0.1035\text{ m} = 10.35\text{ cm}$.
    * Electrical length: $\frac{l}{\lambda} = \frac{85}{10.35} = 8.2125\lambda \equiv 0.2125\lambda$ (after subtracting 8 full wavelengths).
    * On Smith Chart: From normalized $z_L$, rotate $0.2125\lambda$ clockwise towards generator (WTG) on outer rim. Read normalized $z_{in}$ and scale $Z_{in} = z_{in} \cdot Z_0$.
    * **Analytical Verification:** Verify using lossless transmission line formula:
      $$Z_{in} = Z_0 \frac{Z_L + j Z_0 \tan(\beta l)}{Z_0 + j Z_L \tan(\beta l)}$$
  * **Option 2 (TT2 Question 2a — LC Impedance Matching):**
    * Match $Z_L = 120 - j140\,\Omega$ to $Z_0 = 50\,\Omega$ using an L-type matching network on Smith Chart.
    * Determine reactive element values ($L$ and $C$) at frequency $f$ and verify analytically.

#### Question 4 (15 Marks): RF Passives & Filter Design
* **Part A (5 Marks): Butterworth Low-Pass Filter Design (Insertion Loss Method)**
  * **Given:** Cutoff frequency $f_c$, characteristic impedance $Z_0$, and required attenuation/insertion loss $IL$ (in dB) at stopband frequency $f_s$.
  * **Step 1:** Calculate minimum filter order $N$:
    $$N \ge \frac{\log_{10}(10^{IL/10} - 1)}{2 \log_{10}(\omega_s / \omega_c)}$$
  * **Step 2:** Look up prototype low-pass element values $g_1, g_2, \dots, g_N$ from standard Butterworth table.
  * **Step 3:** Denormalize component values:
    $$L_k = \frac{Z_0 g_k}{\omega_c}, \quad C_k = \frac{g_k}{Z_0 \omega_c} \quad (\text{where } \omega_c = 2\pi f_c)$$
  * **Step 4:** Draw final low-pass ladder circuit with component values.
* **Part B (10 Marks with Option): RF Behavior of Passives (Ludwig Chapter 1 / TT1 Question 2)**
  * Given a nominal $250\,\Omega$ (or $550\,\Omega$) metal film resistor operated at radio frequencies with AWG 26 copper leads of length $l = 1.5\text{ cm}$ and parallel stray capacitance $C_a = 2.5\text{ pF}$.
  * **Lead Inductance Calculation:** Wire diameter $d = 0.404\text{ mm}$ for AWG 26.
    $$L = 2l \left[\ln\left(\frac{4l}{d}\right) - 0.75\right] \times 10^{-7}\text{ H}$$
  * **Equivalent Circuit & Impedance Formulation:**
    $$Z(j\omega) = \frac{R + j\omega L}{(1 - \omega^2 L C_a) + j\omega R C_a}$$
  * **The 7–8 Point Frequency Table:** Compute $|Z|$ and phase $\angle Z$ at:
    * $10\text{ MHz}, 100\text{ MHz}, 500\text{ MHz}, 1\text{ GHz}, 1.5\text{ GHz}, 2\text{ GHz}, 3\text{ GHz}$.
  * Identify transition frequency where resistor shifts from purely resistive to reactive behavior.

---

## Part 2: Verbatim Transcript of Prof. Santosh Briefing Call

```text
Santosh: paper hai aap log ka, lagbhag—uh, lagbhag 30 marks ka. Ye electromagnetism hai, 30 marks ka baaki portion hai.
Santosh: thik hai, to—matlab, pehle 2 question electromagnetism par, baaki ke 2-1 question... uh, third question hoga RF behavior par. Aur, haan, third question RF behavior par hoga, aur is par hoga apna smith chart par, basic smith chart, thik hai?
Santosh: jo aap logo ne experiment mein kiya hai. Jo aap logo ne experiment mein kiya hai, uske bahar ka hum kuch bhi nahi pooch rahe.
Santosh: thik hai?
Santosh: sunayi de raha hai?
Speaker 2: Yes sir.
Speaker 3: Yes, yes sir.
Santosh: Haan. To smith chart mein purely jo aapne experiment mein kiya hai, wahi karna hai. Uske bahar ka kuch nahi karna.
Santosh: pehli cheez: smith chart hai, 15 marks ka. Likh lo chahiye to.
Santosh: Smith chart 15 marks ka hai. Filter design 5 marks ka hai, 20 marks ho gaya ye.
Santosh: RF behavior 10 marks ka hai, 30 marks ho gaya. Samajh rahe hain?
Santosh: likh rahe ho ki nahi?
Speaker 3: sir, RF behavior mein—
Santosh: deko, RF behavior hai 10 marks ka. Smith chart 15 marks ka hai. Ek question 5 marks ka, aur ek question 10 marks ka.
Santosh: thik hai?
Speaker 3: filter design?
Santosh: filter design 5 marks.
Santosh: toh ye ho gaya 30 marks.
Speaker 3: sir, derivation hai kya?
Santosh: arey batata hoon, pehle scheme toh samajh le. matlab, kya pattern hai. ye 30 marks ka ho gaya.
Santosh: aur electromagnetism 30 marks ka hai. pehle 2 question honge electromagnetism ke, woh honge 30 marks ke.
Santosh: toh usme bhi kaisa hai ki pattern wahi hai. dekho, 5-10-10.
Santosh: samajh rahe hain?
Santosh: 10 mein option hai. haan, 10 mein option hai.
Santosh: thik hai? 10 mein option hai. har question mein 10 mein option hai.
Santosh: fine?
Speaker 3: hello. sir, woh electrostatics aur magnetostatics mein jo experiments ke 10 question hain, utna karenge toh chalega kya?
Santosh: ye kaun? sarvesh hai?
Speaker 3: nahi, shlok. E3.
Santosh: shlok, achha. haan, kya bol raha hai? aawaz woh-
Speaker 3: sir, electrostatics aur magnetostatics ke liye jo experiments mein 2-10 question hain, utna karenge toh chalega?
Santosh: chalega. suno, kaisa hai ki—infact, usse bhi easy questions aayenge.
Santosh: thik hai? woh jo maine dala tha, woh thoda tough tha. usse bhi easy questions aayenge.
Santosh: toh tum log kya karo, jo apna ekdam initial sums hote hain na, jo koi bhi topic par—jaise, suppose, you start from electrostatics.
Santosh: thik hai? koi note kar raha hai isme se? kaun note kar raha hai?
Santosh: mere ko ye batao.
Speaker 3: yes sir, kar rahe hain.
Santosh: nahi toh baad mein fir poochte rahoge mere ko poori raat. sabka ek-ek message aata rahega.
Santosh: aur note kaun kar raha hai? who is noting?
Speaker 3: sir, kar rahe hain note. main kar raha hoon.
Santosh: kaun?
Speaker 3: tanish.
Santosh: sushant, sushant.
Speaker 3: sushant, haan.
Santosh: achha, tanish haath uthaya tha. haan, toh kaisa hai ki—uh, haan. toh pehla question hai 5 marks ka, electrostatics par.
Santosh: thik hai? To isme ekdam basic electrostatics, jo tum log 12th level par—apan physics 12th, physics level par—thik hai? Jaise, suppose, Coulomb law kya hai, Gauss law kya hai, Faraday's law kya hai, flux kya hai, magnetic—magnetic flux density kya hota hai.
Santosh: Ye sab cheezein basic ekdam.
Santosh: Thik hai?
Santosh: Sunai de raha hai?
Speaker 3: Yes sir.
Santosh: Haan. Ab us par numerical agar aayega, samjho, option mein. Isme agar numerical in case aaya—mostly, dekho, theory bhi expect kar rahe ho.
Santosh: Theory bhi aayega, thoda bahut. Kyunki humko Shirpur wale bachchon ke hisaab se paper banana padta hai, because sister organization.
Santosh: To unka level thoda low rehta hai, comparatively. Compare to your batches, unka level thoda low rehta hai.
Santosh: To unke liye thoda easy banate hain paper, bas. Relatively.
Santosh: To—to thoda theory bhi expect karo. Theory bhi aa sakta hai.
Santosh: Jaise-jaise maine bataya, theory, Gauss law, Maxwell equation—ye to bada—ye to theory aana hi chahiye aapko. Maxwell equations kya hain, aur uske derivations khaas karke aane chahiye.
Santosh: Thik hai? To pehla question hai, samjho, 5. Electrostatics total 30 marks ka hai.
Santosh: To electrostatics mein 5 marks ka ek question hai, aur 10 marks ka option mein ek question hai. Waise hi dusre part mein bhi 5 marks ka ek question hai, aur 10 marks ka option mein ek question hai.
Santosh: Thik hai? To there is an option. Don't worry.
Santosh: 10-10 marks wale mein option. To total 5-10, 5-10.
Santosh: Theek hai? Toh aise 15-15 ke 30 marks ho gaye. Electrostatics, magnetostatics.
Santosh: Samajh mein aaya sabko?
Speaker 2: Ekdam.
Santosh: Samajh mein aaya ki nahi?
Speaker 3: Yes sir. Sir, 10 marks waale questions mein Maxwell wagera?
Santosh: Haan. Ab question kaise aa sakte hain? Jaise, suppose, jaise maine bataya, ekdam basic electrostatics toh karna hi hai sabko.
Santosh: Aisa mat socho ki woh nahi aayega. Woh bhi karna hai.
Santosh: Theek hai? Basic magnetostatics, Ampere, circuit, aur law pata hona chahiye. Basic electrostatics mein jaise aapko E bar due to a line charge, E bar due to a sheet charge, E bar due to a point charge—ye sab bhi pata hona chahiye.
Santosh: Jo 12th mein karte ho tum log. Samajh rahe hain?
Speaker 3: Yes sir.
Santosh: Sunai de raha hai?
Speaker 3: Sir, boundary conditions aayega ki nahi? Boundary conditions waale question.
Santosh: Boundary condition aayega. Ek sum aayega. Boundary condition.
Santosh: Ek sum hoga boundary condition mein.
Santosh: Theek hai? Agar koi nahi kar raha hai, toh possibly option mein bhi aa sakta hai. Matlab, agar samjho time nahi mil raha hai, koi nahi kar paa raha hai, toh ho sakta hai possibly woh option mein rahe.
Santosh: but question aayega boundary.
Santosh: theek hai?
Santosh: haan. Abhi jaise magnetostatics mein kya-kya aana chahiye?
Santosh: jaise Ampere, circuit, aur law aana chahiye. Uske baad, samjho, tumhe—uh—H bar due to a—haan, H bar due to a current, infinite current carrying conductor.
Santosh: Uske baad, aur finite ke liye phir uske baad—aur kya hai?
Santosh: displacement, current, density. Phir ye sab jo basic-basic concept hain magnetostatics ke, wo sab pata hone chahiye.
Santosh: Theek hai? Aur electrostatics ke.
Speaker 3: Sir, solenoid wagera nahi aayega na? Solenoid, toroid, wo bhi hai.
Santosh: Uh, solenoid...
Santosh: Mostly uska derivation toh nahi hai. Nahi hai uska derivation.
Speaker 3: Theek hai sir.
Santosh: Theek hai? Haan. Ye ho gaya electrostatics, magnetostatics.
Santosh: Boundary condition par ek sum aa sakta hai. Possibly option mein aap chhod sakte ho.
Santosh: Doosra, ye jo karna chahiye, wo hai plane waves par sums. Jo tumhara shayad hum log nahi le paaye the.
Santosh: Plane wave par sums aayenge. Toh kaise sums aayenge, thoda main bhej deta hoon.
Santosh: chahiye toh ek—mere ko 10-15 minute baithne do. Thoda bana ke bhejta hoon.
Speaker 3: Sir, is sab par thoda question—do-do na, ek-ek, do-do question ho sake toh. Electromagnetism.
Santosh: Question wahi bata raha hoon na re abhi. Tere ko theory part bataya maine, samajh liya?
Speaker 3: Haan sir, woh samjha. Solve karne ke liye question aap bhej—bhej sakte toh bhejo.
Santosh: Haan, theek hai. Main woh time wale bhejta hoon.
Speaker 2: Sir, DD Dooma Maxwell ka kaisa bheja tha, waisa bhej dena.
Santosh: Haan, jaisa Maxwell ka bheja tha na, waisa ek sum aayega pakka. H diya rahega.
Speaker 3: Sir, aapne jo solved examples bole the solve karne, woh wala important jo diya tha, waisa hi. Sir, waisa PDF bhej do hum log ko questions practice karne ke liye. Waisa bol do.
Santosh: Are baba, end sample main nahi bhej sakta. Samajh rahe ho? There is a restriction.
Speaker 3: Sir, bhej do sir. Kya hota hai?
Santosh: Sir, hum kisi ko nahi—
Speaker 3: सर, हमने टीटी—सर, टीटी2 के टाइम भेजा था ना, वही।
Santosh: End samp mein question bank dena allowed nahi hota hai. Theek hai?
Speaker 2: Sir, toh phir kaun se book se kar rahe hain aap? Woh bol do na.
Santosh: Bata raha hoon, bata raha hoon, bata raha hoon. Pehle toh tum log theory part samajh gaye?
Santosh: Theory part samajh gaye kya? Theory part.
Santosh: Theory part mein kya-kya poochha ja sakta hai? Jaise maine bataya, e bar due to line charge, sheet charge, point charge.
Santosh: Phir aisa bhi sum ho sakta hai ki, samjho, ek point charge bhi diya hai, ek line charge bhi diya hai, aur ek sheet charge bhi diya hai. Aur because of all three configurations, calculate E at a given point.
Santosh: Jaise 12th mein kiya hoga shayad tum log. Samajh rahe hain?
Speaker 3: Haan sir.
Santosh: Haan?
Speaker 3: Haan sir.
Santosh: Samajh mein aaya kya? Kya bola maine? Calculate E at a given point, because of a point charge, because of a line charge, because of a sheet charge.
Santosh: Samjho, teeno configuration de diya. Aur un teeno configuration ke wajah se kisi ek point par aap field nikaal sakte ho.
Santosh: Samajh mein aa raha hai?
Santosh: Haan?
Speaker 3: Yes sir.
Santosh: Haan sir.
Speaker 3: Haan sir.
Santosh: Samajh mein aa raha na?
Speaker 3: Haan sir.
Santosh: Toh ye ek configuration possible hai. Dusra configuration kya ho sakta hai? Ki—uh—H bar nikalne bol sakte hain. 
Santosh: Theek hai? Samjho, do—uh—koi ek current conductor hai, kisi ek point par. Us conductor ke wajah se H bar nikalo.
Santosh: Current carrying conductor hai. Basic Biot Savarts law, Ampere, circuital law.
Santosh: Hai na?
Santosh: Samjha?
Speaker 3: Yes sir.
Santosh: Aur Maxwell equation toh sabko karna hi hai. Maxwell ke charo equation, charo equation ke derivation, Maxwell ke—karna hi hai sabko. Samajh rahe hain?
Santosh: Hmm?
Santosh: Haan ki na?
Speaker 3: Haan sir.
Santosh: Haan. Maxwell ke charo equation ka derivation, with explanation, the rules, the laws, the inconsistencies. Specially woh Ampere circuital law mein aata hai na?
Santosh: Displacement current nahi pakda Ampere ne. Baad mein Maxwell ne correction kiya usko.
Santosh: Samajh rahe hain?
Speaker 3: Haan sir.
Santosh: Haan. Ye ho gaya theory part. Numericals mein, jaise maine bataya, electrostatics mein pucha ja sakta hai E bar at any point, because of different configuration.
Santosh: Thik hai? Fir uske baad--uh--conductor, current carrying conductor ke wajah se H at any point.
Santosh: ठीक है? फिर उसके बाद E हो गया, H हो गया। फिर मैक्सवेल इक्वेशन पर एक आधा सम आ जाएगा, जो हमने टीटी2 में किया था।
Santosh: फाइन? ये सब हो गया, जो तुमने ऑलरेडी किया हुआ है टीटी1, टीटी2।
Santosh: Iske alawa ek type ka sum aur aayega, jo hai plane waves par. Reflection, wave reflections par aayega.
Santosh: Thik hai? Boundary condition. Toh agar time hai toh boundary condition kar lo.
Santosh: Samjha sabko?
Speaker 3: Sir, plane waves 5 marks ka aayega.
Santosh: Plane wave ho sakta hai 10 marks ka aaye. Par 10 marks wale mein option hai.
Santosh: 10 marks wale mein option hai.
Santosh: Thik hai?
Speaker 3: Sir, plane wave ke saath option mein plane wave ka hi aayega ki kuch aur aayega? Jo TT mein tha woh.
Santosh: Toh--uh--nahi, plane wave ke saath plane wave option mein nahi aayega.
Speaker 3: Okay sir.
Santosh: Haan. Lekin time hai toh plane wave bhi karo.
Santosh: theek hai? Aur-aur kya?
Santosh: Uh-ye ho gaya plain waves. Aur-samajh mein aaya?
Santosh: Yahan tak? Aur koi doubt?
Santosh: Poocho.
Speaker 2: Haan sir, kaun se text books hain? Karna hai jidhar se questions aayenge. Like, wo type ke questions aayenge.
Santosh: Okay. Okay. Text book mere khyal se abhi padhne ka time nahi hai tumhare paas.
Santosh: Teen-char din hi hain.
Santosh: तुम लोग टीटी1, टीटी2 किससे पढ़े थे?
Speaker 2: Jo aapne questions diye the, experiments.
Speaker 3: PDF bheja tha, usne kiya hai sir.
Santosh: Haan. Toh abhi tum log William Hayt use karte ho?
Speaker 3: Kya?
Santosh: William Hayt ya phir- sir, aapne wo questions Schaum's electromagnetics se diye the, Schaum se diye the. Haan, wo problems hain, usme theory nahi hai na? Dikkat hua hai.
Speaker 2: Sir, theory ke nahi, nahi, nahi. Jidhar se questions aa sakte hain, similar type ke, waise hi. Solved example.
Santosh: Maine abhi jo bola, tum logo ne note kiya? Pehle ye batao.
Speaker 2: Haan sir.
Santosh: Jitna kar sakte ho, wo toh—utna toh tum yahaan se bhi kar sakte ho, google wagera se, gemini se, gpt se.
Santosh: Samajh rahe hain? Maine jitna abhi tum log ko bataya, uske liye book ki zaroorat hai kya?
Speaker 3: Nahi sir, but—
Santosh: Uske liye book ki zaroorat nahi hai filhal.
Speaker 3: Sir, previous year paper ke sums kare kya?
Santosh: Previous year ke paper mere ko dekhna padega. Mere ko yaad nahi hai abhi previous year ke paper. Dekhna hai toh ek-aad question utha ke dekh lo.
Santosh: Ho sakta hai same hi rahe.
Speaker 2: Sir, plane wave wale ka questions—
Santosh: Haan, kya?
Speaker 2: Plane wave ka aapne bataya, uska expected kahaan se? Matlab kaun se resource se expected hai wo aa sake.
Santosh: Plane wave ke problems tum log—uh—plane waves ke problems schaum se kar sakte ho.
Speaker 2: Sir, plane waves ke toh aap bhejne wale the na?
Santosh: Achha, theek hai, main bhejta hoon. Chalo.
Speaker 3: Sir, question bank ki bhej do na sir, please.
Santosh: Haan?
Speaker 3: Question bank ki bhej do na aap, please.
Santosh: Nahi bola na maine. Tere ko samajh mein nahi aa raha hai kya? Jitna bataya utna kar.
Santosh: Thik hai? Jo maine theory part bataya, aur problems ke liye jaise maine bataya, e bar at any point, h bar at any point.
Santosh: ठीक है? मैक्सवेल इक्वेशन्स, जो टीटी2 में किया था। तो ये तीन टाइप के सम कर ले।
Santosh: Aur chautha, plane waves ka jo baat hai, woh chahiye toh main bhejta hoon reference ke liye.
Santosh: Thik hai? Toh aise char type ke hi sums aayenge. Uske alawa nahi aayenge.
Santosh: Samajh mein aaya?
Speaker 2: Yes.
Santosh: Thik hai. Aur kya doubt poochho?
Speaker 3: Sir, Amit sir, question line ka derivation hai kya?
Santosh: Haan?
Speaker 3: Transmission line ka derivation.
Santosh: Transmission line ka derivation. Nahi.
Speaker 3: Woh last do baar aaya hai, isliye.
Santosh: nahi hai, nahi hai. Theek hai.
Speaker 3: to kya kar dein? Khaali formule se? Bol.
Speaker 2: sir, S mein matrix aur wo ABCD parameter wagaira.
Santosh: nahi, wo bhi skip kar sakte ho filhal.
Speaker 2: sir, transmission line mein se kya aa sakta hai?
Santosh: dekho, transmission line mein jaise main bataunga. Do question basically—haan, 15 marks ka hai transmission line.
Santosh: theek hai?
Santosh: samajh rahe hain?
Speaker 3: haan sir.
Speaker 2: haan sir.
Santosh: 15 marks ka hai transmission. Theek hai? To usmein bhi kaisa hai?
Santosh: 10-10, matlab 10 marks mein kya aayega? Mostly tum log ka aa raha hai behaviour 10 marks ka.
Santosh: samajh rahe hain?
Santosh: yaani—
Speaker 3: sir, RF—
Santosh: total 30 me se—sun—30 me se 10 to RF behavior hai. 5 to filter design hai. bacha 15.
Santosh: 15 Smith chart hai. 15 Smith chart hai.
Santosh: usme bhi ek to ekdam basic Smith chart hai, jo hum log experiment karte the, five-six waghera. ekdam basic.
Santosh: plotting the points waghera.
Speaker 3: VSWR warna.
Santosh: plotting VSWR, gamma, and then all those things. thik hai? aur 10 marks me option me kya aa sakta hai?
Santosh: ek to Zadin puch sakte hain. uske option me puch sakte hain LC matching.
Santosh: जो अपना टीटी2 में।
Santosh: यानी टीटी2—
Speaker 3: stub matching hai sir.
Santosh: stub matching nahi. stub matching nahi.
Santosh: टीटी2 कर लो पेपर अच्छे से बस। टीटी2 सिलेबस।
Santosh: तुम्हारा—उह—15। हाँ, टीटी1, टीटी2 के पेपर कर लो।
Santosh: tumhara 30 marks to pura hi ho gaya. yaani jo Amit sir ka part hai 30 marks, wo to apna jo paper me hua hai utna hi karna hai.
Santosh: uske alawa karna hi nahi. samajh me aaya ye part?
Speaker 3: sir, toh transmission line karna hai ki nahi?
Santosh: hai na? problem transmission line pe rehta hai. hai na?
Santosh: Zin nikalna hai.
Speaker 3: derivation ke liye hota hai na sir transmission ka?
Santosh: derivation. derivation.
Speaker 3: sir, sir, loss—
Santosh: nahi, loss hi nahi. sab loss-loss.
Speaker 3: sir, sir, RF behavior mein woh 10 samples nikalne ke liye—
Santosh: behavior 10 marks ka hai.
Speaker 3: sir, but woh 10 samples nikalne ke liye bahut time jata hai. toh 5 nikal sakte hain kya? ki 10 hi nikal lein?
Speaker 3: 10 frequency samples hi le lein?
Santosh: dekho, tum log ko jitna jamega utna nikalo.
Speaker 3: matlab kitna minimum chahiye? kitna samples chahiye table mein?
Santosh: nikalo. atleast 7-8 points toh hone chahiye. waise bhi 10 marks ka question hai, toh 7-8 point toh expected hai.
Speaker 3: 7-8 points. chalega sir.
Speaker 3: Theek hai.
Santosh: Theek hai. Toh mostly RF behavior tum log kar loge na? Woh jo chart tha ek apne paas, yaad hai na?
Santosh: Woh jo PDF share kiya tha maine, ek matlab starting mein ekdam experiment one ke liye.
Speaker 3: Ludwig ka.
Santosh: Are, Ludwig ka.
Speaker 2: Sir, please send kar do na.
Santosh: Sir, Ludwig ka share kar do na. Ludwig ka tha na starting ke kuch pages.
Santosh: Dhoondhna padega. Ludwig ka bhi.
Santosh: Theek hai.
Speaker 3: Sir, experiment 1, 2, 3 toh hai na woh?
Santosh: Haan, 1, 2, 3. Usmein tum log register karo ya acche se—koi ek acche se karo bas. Register ya capacitor.
Santosh: Ek karo, acche se karo. Register, capacitor.
Santosh: Samajh mein aaya? Haan?
Speaker 3: Sir, yeh RF behavior bol rahe ho na?
Santosh: Haan.
Santosh: RF behaviour 10 marks ka hai.
Santosh: theek hai?
Speaker 2: Main toh chahungi parents ko.
Santosh: Tumko kuch toh de denge. Ek metal film resistor de denge, ya phir ek apna ek capacitor de denge. Aur uska capacitance de denge.
Santosh: Resistor hai toh resistance de denge. Aur saath mein uska gauge de denge.
Santosh: Kitne gauge ka hai, kya hai.
Santosh: Uske baad stray capacitance agar rahega toh woh de denge. Haan.
Santosh: Aur agar capacitor hai, uska loss tangent vagaira rahega toh woh bhi de denge. Toh yaani jo apna basically numerical hai Ludwig ka.
Santosh: Samajh rahe hain?
Speaker 3: Sir, aap bol rahe ho resistor ya capacitor mein se koi bhi ek na.
Santosh: Sir, abhi check kar. Matlab ek toh karo hi kam se kam. Woh bol raha hoon.
Santosh: Samajh rahe hain?
Speaker 3: Formula sheet milega?
Santosh: Formula sheet sir ne bola toh hai Revathi mam ko share karne ko. Ab madam ne exam cell mein update kiya hai ki nahi kiya, mujhe pata nahi. Woh shayad kal Monday khulega, toh mujhe ab follow up lena padega uska shayad.
Santosh: Bola toh hai formula sheet ke liye, sir.
Santosh: lekin main kya bol raha hoon? formula tum log yaad bhi kar sakte ho na?
Santosh: utna hi to yaad karna hai. baaki kaun sa formula hai?
Santosh: achha, theek hai, mostly sheet denge.
Speaker 3: sir, poora subjective formula hai.
Santosh: haan?
Speaker 3: haan sir, poora subjective formula hai.
Santosh: dekho, tumko maine abhi kya bola samajha? register, induct—register aur capacitor karna hai.
Santosh: theek hai?
Santosh: paani bharne aata hai kya re idhar?
Speaker 3: nahi sir, nahi bola. maine eco bola, isliye nahi aaya.
Santosh: to—haan, samajh mein aaya yahaan tak?
Speaker 3: haan sir, aap bas wo plane waves aur jo bhi pdf possible ho, wo bhej do sir.
Santosh: सर, आपके जो पार्ट का है, उसमें प्लेन वेव्स ही एक्स्ट्रा है ना अभी, एंड सेम के लिए। और वो भी ऑप्शन में आएगा। तो फिर टीटी1 और टीटी2 करेंगे तो भी चलेगा ना बस?
Santosh: wo agar option mein hai to.
Santosh: haan. lekin maine jo bataya ekdam starting mein, ekdam basic—
Speaker 3: Ek minute sir.
Speaker 3: Sir?
Speaker 3: Sir, aap mute kar do.
Santosh: Haan, bolo.
Speaker 3: हाँ सर, तो वही टीटी1 और टीटी2 का करेंगे तो।
Santosh: हाँ, वही मैं बोल रहा हूँ ना, टीटी1, टीटी2 अच्छे से करो, बस और क्या?
Speaker 2: Sir, filter design kidhar se karna hai?
Santosh: Haan, filter design ka chahiye toh main bhejta hoon.
Santosh: Filter design ka chahiye toh main bhejta hoon.
Santosh: Theek hai? Z-in nikalne aata hai na sabko, theoretically aur analytic apna Smith chart se.
Speaker 3: Yes sir, yes sir.
Speaker 2: Sir, aap woh bhi bhejo na, electro aur magnetostatics ke thode sums.
Santosh: Yeh kaun hai?
Speaker 3: Are, jo experiment mein kiya hai wahi.
Speaker 2: Nahi, but sir said na, uske pehle bhi thode, matlab dusre type ke aa sakte hain.
Santosh: Are, maine bataya na starting mein. Theory, theory. We have not extensively covered the theory in in class.
Santosh: Because wo 12th level ka hai, toh maine nahi kiya tha. E due to a point charge, line charge, sheet charge, flux, ye sab cheezein re.
Santosh: Wo karo. Theory part.
Santosh: Kya confusion hai? Batao mere ko.
Santosh: Chalo. Batao, jaldi batao.
Santosh: 2 minute aur hain.
Speaker 3: Sir, matlab wo questions jo hai, wo jo hum logon ne lab mein kiya, wahi hai, right? Electrostatics and magnetostatics ke.
Santosh: Haan, usse easy hai in fact.
Speaker 3: Sir, wo E using—sir, wo E using of line charge aur wo sab, uska derivation nahi hai na? Uske sirf sums hi hai na?
Santosh: Uska derivation karna hai, wahi toh bol raha hoon. Theory bol raha hoon na, theory. E due to a line charge, E due to a sheet charge.
Speaker 3: Uska derivation aa sakta hai?
Santosh: Haan, theory bol raha hoon, matlab derivation.
Speaker 3: Theek hai. Sir, ye theory ka koi material hai sir?
Santosh: Are, ye toh simple, Google mein daalna, mil gaya. 50 kahin se bhi kar lo, E due to a line charge.
Speaker 2: Aur sir, do questions hain waise. Module five sir, filter design ke liye.
Santosh: filter design ka, dekho, main ek PDF share karta hoon abhi. Main tumhare Teams mein daal deta hoon. Kahan gaya?
Santosh: Kaise karein isko? Isko minimize karta hoon.
Speaker 3: filter design aur plane waves dono dekho sir.
Santosh: Post in a channel.
Speaker 2: Haan, yes sir. Second module mein time variation, wave propagation ka kaise work karta hai? Numerical.
Santosh: Maine ek PDF share kiya, uske starting ke 3-4 page, at least 5-6 page starting ke, insertion loss method hai. Haan, filter design pe thoda main aur comment karna chahunga, kyunki shayad tum log ko sir ne utna detail mein bataya nahi hoga, exam point of view matlab. Maine ek Teams mein dala hai.
Santosh: Achha, theek hai, baitho. Peeche baith jao.
Santosh: To haan, filter design karna hai. Kaise karna hai?
Santosh: Achha, tum log ko baaki sab samajh gaya? Baaki 55 marks ka samajh gaya?
Speaker 2: Sir, aap marks distribution de sakte ho module wise.
Santosh: Arey, bataya na maine starting mein. Tum log kaun note kar raha hai? Sushant?
Speaker 3: Haan sir, maine--
Santosh: 30 marks ka electromagnetism hai. 5-10, 15-15 ke do question hain.
Santosh: Samajh rahe hain? Electrostatics, magnetostatics, and time varying fields.
Santosh: Yeh ho gaya.
Speaker 2: To ye teen topics mila ke 30 marks bol rahe ho.
Santosh: 30 marks ho gaye. Baaki 30 marks mein tumhara 10 marks ka RF behavior hai, 15 marks ka Smith chart hai, 5 marks ka filter design.
Santosh: Noted?
Speaker 2: Haan sir, thank you.
Santosh: Theek hai. Ab Smith chart wahi jo humne lab mein kiya hua hai. RF behavior wahi jo humne lab mein kiya hua hai.
Santosh: Sorted?
Santosh: Haan ki na?
Speaker 3: Haan sir. Yes sir.
Santosh: Hello? Haan.
Speaker 3: Sir, sir, filter designing mein sir, wo coefficients, wo formula sheet mein diya jayega na?
Santosh: Haan, uska chart diya jayega. Filter design mein ek cheez dhyan rakho, tumko ek hi type ka filter poochha gaya hai. Ek hi method hai, aur us method mein bhi teen type ke hain, but tumko usme se ek hi type ka hai.
Santosh: To tum log wo PDF khologe, to fir bhi main jo bol raha hoon wo note kar lo. Sabse pehla, tumko sirf filter design mein tumhe hai sirf insertion loss method.
Santosh: Likh lo, insertion, yaani to insert. Insertion loss method.
Santosh: Kya hota hai insertion loss method? Insertion loss method matlab samjho ek source hai aur ek load hai.
Santosh: Us source aur load ke beech mein tumne ek filter laga diya. To kya hoga?
Santosh: There will be some reflection. Hai ki nahi?
Santosh: There will be some power loss. And that is what we have to calculate.
Santosh: Ki kitna loss ho sakta hai. To humko filter kaise design karna hai, kitne order ka hona chahiye, aur kya uski cut off frequency honi chahiye.
Santosh: Theek hai?
Santosh: Samajh rahe hain? To kya note kiya sabse pehla?
Santosh: Ki insertion loss method, ye ek method hai. Ek dusra method hai image parameter, wo tumko nahi hai.
Santosh: Samajh rahe hain?
Santosh: To maine jo PDF share kiya hai, wo cut PDF share, crop karke share kiya hai. Utna hi padhna hai, maine jitna bheja hai.
Santosh: Aur usme bhi maine saare type ke bhej diye hain, but tumko sirf pehle 6-7 page padhne hain. Tumhe jo exam mein aayega, dhyan dena, tumhe jo exam mein aayega, wo hai mostly ye, kya bolte hain?
Santosh: Mostly, haan, likh lo chahiye to. Exam mein tumhe sirf Butterworth filter hai.
Santosh: Chebyshev nahi hai, elliptic nahi hai. Likho, exam mein kya hai?
Speaker 3: Butterworth filter.
Santosh: Butterworth, sirf Butterworth. theek hai? No Chebyshev, no elliptical.
Santosh: To Butterworth ka dusra naam hai maximally flat. To ho sakta hai question frame karte wakt maine thoda bahut rephrase kiya ho, to tension nahi lene ka.
Santosh: Butterworth bol sakte hain hum usko. Usko binomial bol sakte hain.
Santosh: usko maximally flat bol sakte hain. Ye teeno naam kiske hain?
Santosh: teeno?
Speaker 3: Butterworth.
Santosh: teeno Butterworth hi hain.
Speaker 3: Butterworth ke.
Santosh: haan, toh iska matlab kya hai Butterworth filter ka? Matlab ye hai, maximally flat matlab kya? Matlab ek filter hota hai.
Santosh: filter sabne dekha hai, response. Filter, response, filter ka frequency response sabko pata hai.
Santosh: sabne EDC wagaira mein kiya rahega na, filter ka frequency response. Toh low pass filter hai agar, toh low pass mein woh low frequencies ko pass karta hai, aur phir ek cut off rehta hai, aur phir uske baad woh attenuate karta hai.
Santosh: hai ki nahi? samajh rahe hain?
Speaker 3: Sir, aapki aawaz nahi aa rahi.
Santosh: low pass filter pata hai na sabko?
Speaker 3: Yes sir, yes sir.
Santosh: uska frequency response pata hai?
Speaker 3: Yes sir.
Santosh: toh ek hota hai pass band, ek hota hai stop band. Toh pass band mein agar uska jo response hai, woh agar flat hai, toh usko bolte hain maximally flat ya phir Butterworth.
Santosh: doosra hota hai chebyshev, jisme ripples hote hain pass band me.
Santosh: samajh rahe hain? to tumko exam me kya aayega?
Speaker 3: butterworth.
Santosh: butterworth. theek hai? to kya diya rahega?
Santosh: question me kya diya rahega butterworth? bola rahega design a filter, maximally band pass, maximally flat, maximally flat filter, ya design a butterworth filter, ya design a binomial filter.
Santosh: aur specially exam me low pass hi hai tum log. na high pass hai, na band pass hai, na band stop hai.
Santosh: sirf low pass. to ekdum neesh problem aayega.
Santosh: maximally flat, low pass. samajh me aaya?
Santosh: clear hai?
Speaker 2: sir, LC impedance matching hai kya?
Santosh: pehle filter khatam kar lete hain. wo hai. 10 mark ka, wo bhi hai.
Santosh: theek hai? LC matching. but mostly wo Z_in ke comparison, Z_in ke option me aayega.
Santosh: jahan tak mujhe lag raha hai, jahan tak mujhe lag raha hai, wo Z_in ke comparison me aayega.
Santosh: theek hai? theek hai? to samajh me aaya?
Santosh: hello?
Speaker 3: haan sir. Yes sir. Yes sir.
Santosh: haan, toh filter mein kya aayega? Matlab kaisa rahega question?
Speaker 3: insertion Butterworth, woh bhi low pass mein hi.
Santosh: haan, Butterworth, woh bhi low pass mein. Bas. Toh diya kya-kya rahega suppose tumhe?
Santosh: cut off frequency diya rahega.
Santosh: theek hai? Low pass ka ek cut off frequency hota hai. Aur jahan hum filter ko insert kar rahe hain, jis transmission line mein, uska characteristic impedance diya rahega.
Santosh: theek hai? Aur filter ko insert karne ke baad transmission line mein jo loss hoga, theek hai? Jo insertion loss hota hai, woh diya rahega.
Santosh: samajh rahe hain?
Santosh: tum log ek kaam karo, chahiye toh main iska ek chhota, ek 10-15 minute ka ek video bana ke bhejta hoon tumko. Woh sir ne liya tha shayad na, filter design?
Speaker 2: no sir, start bhi nahi kiya.
Santosh: start nahi kiya? Sir bol rahe the, goonga karke.
Speaker 3: nahi.
Santosh: achha. Nahi toh extra lecture rakha tha na kuch filter design ke liye sir ne? Main Gorakhpur mein tha tabhi.
Santosh: online.
Speaker 3: nahi, nahi rakha.
Speaker 2: nahi rakha.
Speaker 3: sir rakha tha, 4th november ko rakha tha, but koi aaya nahi tha usme. And kisi ko pata hi nahi tha wo lecture hai.
Santosh: achha theek hai. Suno, filter design bada aasaan hai. 10-15 minute ka video bana ke bhej deta hoon main.
Santosh: tum log dekh lena.
Santosh: theek hai? Fine?
Santosh: hello?
Speaker 3: yes sir, yes sir.
Santosh: aur kuch poochhna hai?
Speaker 3: sir, plane waves ka bhi bhej do.
Santosh: plane waves ke kuch reference samples, example bhej deta hoon. Theek?
Speaker 3: sir, rf behaviour ka bhejna tha na aapko.
Santosh: rf behaviour wahi ludwig ka re, baba.
Speaker 3: wahi sir, wo nahi.
Speaker 2: mujhe experiment one aur two me jo tha wahi karna hai na, rf.
Santosh: haan, resistance diya rahega. Tumko stray capacitance diya rahega. Aur formule se inductance nikaal sakte ho.
Santosh: phir bas, phir frequency daalo. Value nikaalo.
Santosh: Z-in nikaalo, plot karo bas.
Santosh: Theek hai? Dekh lo ek baar. Ludwig dekh lo.
Santosh: Ludwig ke pehle 3-4 page. First chapter Ludwig ka.
Santosh: Theek hai?
Santosh: Jisko pata hai thoda help karo baaki log ko. Aur kya?
Santosh: Aur kya doubt hai? Bolo jaldi-jaldi.
Speaker 3: Sir, sir, Meet sir ke portion me se theory aisa kuch nahi aayega?
Santosh: Nahi.
Speaker 3: Numericals?
Santosh: Only numericals.
Speaker 3: Sir, wo skin depth ka numerical wagaira hai kya?
Santosh: Nahi. Bataya na maine numerical me kya hai.
Santosh: Skin depth toh wo toh aayega hi na, part hai na. It's a part of the RF behavior na.
Santosh: RF behavior me skin depth aata hai na re baba.
Santosh: Aisa alag se coaxial cable wagera uska nahi hai. RF behavior mein aa jata hai wo.
Santosh: Theek hai?
Santosh: Samajh rahe hain ki nahi?
Santosh: Bolo, kaun bol raha hai?
Speaker 3: Sir, wo lossless electric ka numerical aayega kya?
Santosh: Lossless kya? Z_in nikalne ka?
Santosh: Z_in nikalne ka bol raha hai na?
Speaker 3: Wo dielectric, mu_r, epsilon_r, wo.
Speaker 3: Haan sir, wo Z_in ka hi hai.
Santosh: Haan to Z_in mein to poochte hi hai na wo sab. Theoretically aur smith chart se dono karna hi hai na.
Santosh: Kya hua? Nahi samjha.
Santosh: Haan?
Santosh: Hello? Kaun hai ye?
Santosh: Rishabh tha na shayad?
Santosh: Rishabh?
Speaker 3: haan sir, wo keh raha tha ki wo lossless dialectic, mu r, epsilon r.
Santosh: dekh, tere ko Z in nikalne bolenge. kisi transmission line ka, jiska load impedance diya hoga, characteristic impedance diya hoga, frequency diya hoga, length diya hoga. aur dialectic constant diya hoga us medium.
Santosh: transmission line jis medium mein hai, us medium ka dialectic constant.
Santosh: uska transmission line ka jo dialectic constant hai, haan.
Speaker 2: sir, wo smith chart mein T pi network aur stub matching nahi karna hai.
Santosh: nahi karo, chalega.
Santosh: aur kuch?
Santosh: I think theek hai na itna? khaali filter design mein thoda problem rahega tum log ko understand.
Santosh: main ek 10-15 minute ka video bana ke bhej deta hoon.
Santosh: theek hai?
Speaker 3: Thank you sir.
Santosh: mere khyal se itna karo, full pura attempt kar paoge. theek hai? filter ka main bhejta hoon.
Santosh: filter ka bhejta hoon aur kuch sample problem plane waves ke bhej deta hoon.
Santosh: aur kuch?
Speaker 2: sir, boundary condition?
Santosh: Boundary condition toh ek sum aayega, bola na maine. Option me rahega mostly. But karke rakho boundary.
Santosh: क्या है? एच1, एचटी1, एचएन1?
Santosh: Haan bolo.
Speaker 3: Aapko woh last year ka do paper bheja hai sir. Usme woh plane wave ka do question hai. Woh ek bar aap dekh sakte hain kya waisa hi aayega kya?
Speaker 3: Haan.
Santosh: Achha, ek minute, dekhta hoon.
Santosh: Last year ka hai kya ye?
Santosh: Theek hai. Dekh, pehla question kya hai? D bar diya hua hai.
Santosh: Haan, aisa question bhi aa sakta hai. D bar diya hua hai.
Santosh: Aur total charge, yaani apna ye lagane ka hai. Gauss divergence theorem.
Santosh: Fir dekh, H due to a finite length conductor. Bola tha maine tumko.
Santosh: Hain ki nahi? H due to infinite, H due to finite.
Santosh: Theek hai. Wave equations in free space. Theory poochha hai.
Santosh: Fir uske baad question B me dekh, H diya hua hai, beta poochha hai, lambda poochha hai, T poochha hai.
Santosh: Samajh rahe hain? Bas ye aise hi sums kar lo.
Santosh: Aur kya? E diya hua hai, H poochha hai.
Santosh: Maxwell equation. Samajh rahe hain?
Speaker 3: Sir, woh question two derivation hi tha woh transmission line ka. Wahi poochh raha tha ki woh hai ya nahi.
Santosh: Question two transmission line derivation. Nahi, transmission line ka derivation.
Santosh: Transmission line. Kaun sa?
Santosh: Main 2000 iska dekh raha hoon. 25-26 ka.
Santosh: 25-26 dekh raha hoon re main. Ek minute ruk, dekhta hoon pattern same hai kya.
Santosh: Ruk, let me check.
Speaker 3: Achha, woh wave equation ka hai sir. Theek hai, theek hai.
Santosh: Haan, pattern I think let me check. Arre, pattern same hi hai is baar bhi. Humne bhi aise hi kiya hai is baar.
Santosh: Question one.
Speaker 3: Nahi, woh RF bhi last time 35 marks ka aaya tha.
Santosh: Question three. Arre baba, same hi pattern hai. Ekdam same hai pattern.
Santosh: Last ke do paper kar lo chahiye toh. Same pattern hai.
Santosh: 25-26 ka toh same hai. 24-25 ka dekhna padega.
Santosh: achha, ye re exam ka hai. ye jo bheja tune.
Santosh: kya hai?
Santosh: wo regular wala rahega shayad na. haan, regular.
Santosh: ek kaam karo, ye ayushman wo share kar de group mein baaki log ko bhi. wo do paper kar lo.
Santosh: kuch doubt hai toh usmein poochho. dekho, same pattern hai.
Santosh: are, ye toh same hi hai. ek minute, ek minute.
Speaker 3: nahi, wo alag hai.
Santosh: haan, ek minute. wapas wahi khola shayad. haan, E diya hua hai.
Santosh: V poochha hai. jo humne tutorials mein kiya hua hai.
Santosh: filamentary current carrying conductor hai. Biot's Savart's law.
Santosh: maine bola na, H nikalna rahega. H at any point.
Santosh: samajh rahe hain?
Santosh: haan ki na? wave propagation in lossy.
Santosh: achha, wave propagation in lossy poochh raha tha kya tu? ok, ok.
Santosh: nahi, aisa theory question. haan, theory question aayega re.
Santosh: Ek lossy ke liye theory question aa sakta hai. Ek lossy, ek lossless ke liye.
Santosh: Barabar hai.
Santosh: To ye do paper kar lo last ke. Bahut hai mujhe lagta hai.
Santosh: Itna hi bahut ho jayega tumhare liye.
Santosh: Samajh rahe hain?
Santosh: Bolo.
Speaker 3: Haan sir.
Santosh: Last ke do paper kar lo. I think this will be more than enough. Khali values badalenge lagbhag.
Santosh: Same hi hai. Maine dekha nahi tha paper.
Santosh: Theek hai. It is almost same. What we have planned this year.
Santosh: Theek hai?
Speaker 3: Sir, wo last year ka jo paper hai, usme Smith chart ke options hain.
Santosh: Actually main nahi padhaya tha na last year. To iske liye mere ko maloom nahi tha. But theek hai.
Santosh: Maine abhi dekha. It is almost same.
Santosh: No doubt. No issue.
Santosh: Haan, kya bol raha hai?
Speaker 3: Sir, main bol raha tha ki jo Smith chart ke bhi questions hain, uska bhi options jo rahega, woh bhi same hi options mein aayenge.
Santosh: Yes, yes. Similar pattern, similar flow, everything is same.
Speaker 3: Okay sir.
Santosh: Theek hai? Pattern is same, flow is same. Haan.
Speaker 2: Sir, woh Poisson's equation and woh Laplace equation nahi hai na?
Santosh: Mein poochha ja sakta hai. Poochh sakte hain.
Santosh: Ismein nahi dikh raha tha paper mein. Last ke do paper mein nahi dikh raha hai.
Santosh: But humne dala ek-aad question aisa bhi dala hai. Toh aa bhi sakta hai.
Santosh: But mujhe lagta hai ki tum log ye last ke do paper kar loge na. You can attempt full.
Santosh: Don't worry.
Santosh: Theek hai?
Speaker 2: Toh sir, ye derivation hai. Ye wave equation and free space.
Santosh: Yes, yes. Wave equation derivation hai. Maxwell ka derivation hai.
Santosh: E bar due to a line charge. E bar due to a sheet charge.
Santosh: e bar due to H bar because of a finite length. H due to a infinite length conductor.
Santosh: jo abhi paper me dekha na humne. waise hi.
Santosh: thik hai?
Santosh: any other thing? last do paper kar lo.
Santosh: that is more than enough. maine dekha nahi tha abhi tak.
Santosh: abhi bhej diya usne. to maine dekha.
Santosh: similar pattern, similar flow, similar set of options. samjhe?
Speaker 3: yes sir.
Santosh: chalo, I think we can stop.
```
