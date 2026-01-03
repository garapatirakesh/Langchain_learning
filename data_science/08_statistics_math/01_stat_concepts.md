# Statistics, Probability, and Calculus for Data Science

## 1. Statistics (The Science of Data)

### Descriptive vs Inferential
- **Descriptive**: Summarizing data (Mean, Median, Standard Deviation). "What happened?"
- **Inferential**: Using a sample to make guesses about the whole population. "What *will* happen?"

### Distributions
- **Normal (Gaussian)**: The Bell Curve. 68% of data is within 1 $\sigma$, 95% within 2 $\sigma$.
- **Bernoulli**: Coin flip (0 or 1).
- **Binomial**: Result of N coin flips.
- **Poisson**: Count of events in a time interval.

### Hypothesis Testing
- **Null Hypothesis ($H_0$)**: "Nothing interesting is happening."
- **Alternative Hypothesis ($H_1$)**: "Something changed."
- **P-Value**: Evidence against $H_0$. If P < 0.05, we reject $H_0$.

---

## 2. Probability (The Measure of Certainty)

### Rules
- **Sum Rule**: P(A or B) = P(A) + P(B) - P(A and B).
- **Product Rule**: P(A and B) = P(A) * P(B|A).

### Bayes' Theorem
The foundation of modern AI.
$$ P(A|B) = \frac{P(B|A)P(A)}{P(B)} $$
- **Prior P(A)**: What we thought before seeing data.
- **Likelihood P(B|A)**: How likely is the data given our theory?
- **Posterior P(A|B)**: Our new belief.

---

## 3. Calculus (The Engine of Optimization)

### Derivatives (Slopes)
- **Concept**: How much does $y$ change if I nudge $x$?
- **In ML**: Calculating the **Gradient** (Direction of steepest ascent).
- **Optimization**: We want to minimize Error. So we go in the *opposite* direction of the gradient ($w = w - \alpha \nabla w$).

### Chain Rule
- **Concept**: If $y$ depends on $u$, and $u$ depends on $x$, then $\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}$.
- **In ML**: This is **Backpropagation**. The error at the output layer is passed back through hidden layers by multiplying derivatives.
