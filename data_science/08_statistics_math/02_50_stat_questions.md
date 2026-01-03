# 50 Complex Statistics & Math Interview Questions + Answers

## Section 1: Probability Theory

**1. Explain the Monty Hall Problem.**
*   **Answer**: In a game show, there are 3 doors. Behind one is a car; others are goats. You pick a door. The host (who knows what's behind doors) opens another door with a goat. Should you switch? Yes. 
*   **Why**: Your initial pick has a 1/3 chance. The remaining two doors combined have 2/3. Since the host eliminates one goat door, the 2/3 probability shifts entirely to the other unopened door.

**2. What is the Birthday Paradox?**
*   **Answer**: In a room of just 23 people, there's a 50.7% chance at least two share a birthday. 
*   **Why**: We look at the probability of *no one* sharing a birthday. As people are added, the number of possible pairings increases quadratically ($n(n-1)/2$), leading to a surprising rapid increase in the coincidence probability.

**3. Derive the formula for Bayes' Theorem.**
*   **Answer**: Start with $P(A \cap B) = P(A|B)P(B)$ and $P(A \cap B) = P(B|A)P(A)$. Setting them equal: $P(A|B)P(B) = P(B|A)P(A)$. Solving for $P(A|B)$ gives $P(A|B) = \frac{P(B|A)P(A)}{P(B)}$.

**4. 10 coin flips, probability of exactly 5 heads?**
*   **Answer**: Use Binomial PMF: $\binom{10}{5} (0.5)^5 (0.5)^5 = 252 \times \frac{1}{1024} \approx 24.6\%$.

**5. Joint, Marginal, and Conditional probability.**
*   **Joint $P(X, Y)$**: Probability of $X$ and $Y$ happening together.
*   **Marginal $P(X)$**: Probability of $X$ occurring alone (summing/integrating out $Y$).
*   **Conditional $P(X|Y)$**: Probability of $X$ given $Y$ has occurred. $P(X|Y) = \frac{P(X, Y)}{P(Y)}$.

**6. What is Markov Chain?**
*   **Answer**: A stochastic process where the future state depends only on the current state and not on the sequence of events that preceded it ("Memoryless").

**7. Difference between Covariance and Independence.**
*   **Answer**: Independence implies 0 covariance. However, 0 covariance DOES NOT imply independence (they could have a non-linear relationship like $Y = X^2$).

**8. What is the Law of Total Probability?**
*   **Answer**: It expresses the total probability of an outcome which can be realized via several distinct events. $P(A) = \sum_n P(A|B_n)P(B_n)$.

**9. Explain Expectation ($E[X]$) and Variance ($Var(X)$).**
*   **Expectation**: The long-term average value of a random variable. $\sum x \cdot P(x)$.
*   **Variance**: The average of the squared deviations from the mean. $E[X^2] - (E[X])^2$.

**10. What is Chebyshev's Inequality?**
*   **Answer**: Guarantees that in any probability distribution, no more than $1/k^2$ of the distribution's values can be more than $k$ standard deviations away from the mean.

## Section 2: Statistical Inference

**11. Explain CLT to a non-technical person.**
*   **Answer**: No matter how messy or weird your original pile of data is, if you take many groups of samples and average them, those averages will always form a nice Bell Curve.

**12. Standard Error vs Standard Deviation?**
*   **Std Dev (SD)**: Measures the spread of individual data points in a sample.
*   **Std Error (SE)**: Measures the spread of the sample *mean* if you were to repeat the experiment many times. $SE = \frac{SD}{\sqrt{n}}$.

**13. MLE for Gaussian Distribution.**
*   **Answer**: By maximizing the log-likelihood function, we find that the MLE for the mean $\hat{\mu}$ is the sample mean ($\frac{1}{n} \sum x_i$) and for variance $\hat{\sigma}^2$ is the sample variance.

**14. t-test vs z-test?**
*   **z-test**: Used when sample size is large (>30) and population variance is known.
*   **t-test**: Used when sample size is small (<30) or population variance is unknown (relying on sample variance instead).

**15. What is ANOVA?**
*   **Answer**: Analysis of Variance. It checks if the means of 3 or more groups are different by comparing the variance between groups to the variance within groups.

**16. Type I vs Type II errors.**
*   **Type I**: False Positive. Rejecting the Null when it's true (convicting an innocent person).
*   **Type II**: False Negative. Failing to reject the Null when it's false (letting a guilty person go).

**17. What is Statistical Power?**
*   **Answer**: $1 - \beta$. The probability of correctly rejecting the Null Hypothesis when the Alternative is true. High power means you are likely to detect an effect if it exists.

**18. Multiple Comparisons Problem?**
*   **Answer**: The more tests you run, the higher the chance of finding a result by pure luck (False Positive). **Bonferroni Correction** fixes this by dividing the required p-value (e.g., 0.05) by the number of tests.

**19. What is a Confidence Interval?**
*   **Answer**: If we repeated this experiment 100 times, 95 of those calculated intervals would contain the true population mean. It is an interval estimation of the population parameter.

**20. Chi-Square Goodness of Fit vs Independence.**
*   **Goodness of Fit**: Checks if one categorical variable matches an expected distribution.
*   **Independence**: Checks if two categorical variables are related.

## Section 3: Calculus & Optimization

**21. What is a Gradient?**
*   **Answer**: A vector pointing in the direction of the steepest increase of a function. Its components are the partial derivatives with respect to each variable.

**22. Chain Rule in Backpropagation.**
*   **Answer**: To get the error at a weight in a deep layer, we multiply the derivatives layer-by-layer backwards from the output. $\frac{\partial Loss}{\partial w} = \frac{\partial Loss}{\partial Out} \cdot \frac{\partial Out}{\partial w}$.

**23. What is Convexity?**
*   **Answer**: A function $f$ is convex if the line segment between any two points on the graph lies above the graph. Critically, it ensures that any local minimum is the **Global Minimum**.

**24. Global vs Local Minima.**
*   **Global**: The absolute lowest point of the function.
*   **Local**: The lowest point in a specific neighborhood. (Deep Learning often gets stuck in local minima or saddle points).

**25. What is the Hessian Matrix?**
*   **Answer**: A square matrix of second-order partial derivatives. It describes the local curvature of the function.

**26. Newton's Method.**
*   **Answer**: Optimization that uses the 2nd derivative (Hessian) to take much more accurate steps toward the minimum. $x_{n+1} = x_n - \frac{f'(x_n)}{f''(x_n)}$.

**27. Lagrangian Multiplier.**
*   **Answer**: A strategy for finding the local maxima and minima of a function subject to equality constraints.

**28. L1 vs L2 Norm mathematically.**
*   **L1 (Manhattan)**: $\sum |x_i|$.
*   **L2 (Euclidean)**: $\sqrt{\sum x_i^2}$.

**29. Taylor Series.**
*   **Answer**: Representing a function as an infinite sum of terms calculated from its derivatives at a single point ($a$). It's used to approximate complex functions.

**30. Why Log-Likelihood?**
*   **Answer**: 1. Prevents underflow (multiplying 1,000 tiny probabilities becomes 0; adding logs stays manageable). 2. Turns products (hard to derive) into sums (easy to derive).

## Section 4: Distributions

**31. Normal Distribution Properties.**
*   **Symmetry**: Mean = Median = Mode.
*   **Empirical Rule**: 68/95/99.7% of data within 1/2/3 standard deviations.

**32. Poisson vs Exponential.**
*   **Poisson**: Counts events per time unit (Discrete).
*   **Exponential**: Models the *waiting time* between those events (Continuous).

**33. What is a Beta Distribution?**
*   **Answer**: A family of continuous probability distributions defined on the interval [0, 1]. In Bayesian stats, it represents our uncertainty about a probability (like click-through rate).

**34. What is the Gamma Function?**
*   **Answer**: An extension of the factorial function to complex and real numbers ($n! = \Gamma(n+1)$).

**35. Student's t-distribution.**
*   **Answer**: Similar to Normal but has "heavier tails". Used when we have small sample sizes and don't know the population's true standard deviation.

**36. Uniform vs Normal.**
*   **Uniform**: Every outcome in a range is equally likely (rectangular shape).
*   **Normal**: Center values are most likely (bell shape).

**37. What is a CDF?**
*   **Answer**: Cumulative Distribution Function. $F(x) = P(X \leq x)$. It tells you the probability that the variable will be less than or equal to $x$.

**38. Q-Q Plot.**
*   **Answer**: Quantile-Quantile plot. If the points fall on a straight 45-degree line, the two distributions (usually your data vs a Theoretical Normal) are the same.

**39. Box-Cox Transformation.**
*   **Answer**: A power transformation that transforms non-normal data into a normal distribution by finding an optimal parameter $\lambda$.

**40. Bernoulli vs Binomial.**
*   **Bernoulli**: A single trial with 2 outcomes (pass/fail).
*   **Binomial**: The sum of $n$ independent Bernoulli trials.

## Section 5: Advanced Applied Math

**41. Eigenvalues and Eigenvectors.**
*   **Concept**: When you apply a transformation (Matrix $A$), the **Eigenvectors** are the directions that don't change orientation (only scale). **Eigenvalues** are the factors by which they scale.

**42. SVD (Singular Value Decomposition).**
*   **Answer**: Decomposing any matrix into three matrices ($U \Sigma V^T$). Used in PCA for dimension reduction and in recommendation algorithms.

**43. Cosine Similarity vs Dot Product.**
*   **Dot Product**: Measures both magnitude and direction.
*   **Cosine Similarity**: Measures only the angle/direction. It's the Dot Product normalized by lengths.

**44. Kernel Density Estimation (KDE).**
*   **Answer**: A non-parametric way to estimate the probability density function (smoothing a histogram into a continuous line).

**45. Monte Carlo Simulation.**
*   **Answer**: Using repeated random sampling to solve a problem that might be deterministic in principle. (e.g., estimating Pi by throwing random darts at a circle).

**46. KL Divergence.**
*   **Answer**: Measures how one probability distribution $Q$ is different from a reference distribution $P$. Used in training VAEs and LLMs (RLHF).

**47. Jensen's Inequality.**
*   **Concept**: For a convex function, the value of the function at the average is less than the average value of the function. $f(E[x]) \leq E[f(x)]$.

**48. Correlation vs Causation.**
*   **Correlation**: Two things happen together.
*   **Causation**: One thing *causes* the other. A confounding variable (e.g., hot weather) can cause both Ice Cream sales and Sunburns, making them correlate even though one doesn't cause the other.

**49. A/B Testing.**
*   **Answer**: A randomized controlled experiment where you compare a test version against a control to measure statistically significant improvements.

**50. Numerical Integration.**
*   **Answer**: Techniques like the **Trapezoidal Rule** used to find the area under a curve (integral) when the function is unknown or too complex to solve analytically.
