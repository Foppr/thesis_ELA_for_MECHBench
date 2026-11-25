import numpy as np

class AdaptiveTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Define frequency and amplitude parameters for trigonometric components
        self.frequencies = np.linspace(1.0, 8.0, min(dim, 20))
        self.amplitudes = 1.0 + 0.5 * np.sin(np.arange(min(dim, 20)) * 0.5)
        # Polynomial conditioning exponents
        self.exponents = 2.0 + 3.0 * np.random.rand(min(dim, 20))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Trigonometric wave component with varying frequencies and amplitudes
        trig_term = 0.0
        for i in range(min(self.dim, 20)):
            freq = self.frequencies[i]
            amp = self.amplitudes[i]
            trig_term += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] / 2.0)
        
        # Polynomial conditioning with adaptive exponents
        poly_term = 0.0
        for i in range(self.dim):
            exp = self.exponents[i % len(self.exponents)]
            poly_term += (x[i] ** exp) * np.exp(-0.1 * np.abs(x[i]))
        
        # Adaptive gradient modulation based on neighbor interactions
        grad_mod = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            k = (i + 2) % self.dim
            diff_ij = x[j] - x[i]
            diff_ik = x[k] - x[i]
            grad_mod += np.tanh(diff_ij) * np.cos(diff_ik) * \
                       (1.0 + 0.3 * np.sin(i * 0.3)) * \
                       np.exp(-0.05 * (x[i]**2 + x[j]**2))
        
        # Sharp transition regions with sigmoidal mixing
        sharp_term = 0.0
        for i in range(self.dim):
            transition = 1.0 / (1.0 + np.exp(-5.0 * (x[i] - np.mean(x))))
            sharp_term += transition * np.sin(3.0 * x[i]) * \
                         np.cos(2.0 * x[i]) * \
                         (1.0 + 0.4 * np.cos(i * 0.7))
        
        # Combined objective with dynamic weights
        result = 0.3 * np.sum(x**2) + 0.4 * trig_term + 0.2 * poly_term + \
                 0.15 * grad_mod + 0.1 * sharp_term
        
        return result