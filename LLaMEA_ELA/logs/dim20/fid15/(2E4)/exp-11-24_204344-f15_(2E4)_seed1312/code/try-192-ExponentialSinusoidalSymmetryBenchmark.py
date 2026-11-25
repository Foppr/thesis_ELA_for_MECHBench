import numpy as np

class ExponentialSinusoidalSymmetryBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Base exponential sinusoidal landscape
        result = 0.0
        for i in range(self.dim):
            # Exponential modulation with sinusoidal components
            exp_mod = np.exp(0.5 * np.abs(x[i])) * np.sin(x[i]**2)
            sin_mod = np.sin(3.0 * x[i]) * np.cos(2.0 * x[i])
            result += exp_mod + sin_mod
        
        # Fractional calculus inspired smoothing with memory effects
        fractional_term = 0.0
        for i in range(self.dim):
            # Approximate fractional derivative effect using weighted sum
            weight_sum = 0.0
            for j in range(1, min(5, self.dim)):
                if i + j < self.dim:
                    weight = 1.0 / (j ** 1.5)
                    weight_sum += weight * np.sin(x[i] * x[i+j])
            fractional_term += weight_sum
        
        # Adaptive coupling strengths with dynamic frequency modulation
        coupling_term = 0.0
        for i in range(self.dim):
            freq_mod = 2.0 + 1.5 * np.sin(i * 0.7)
            for j in range(i+1, min(i+3, self.dim)):
                coupling = (x[i]**2 + x[j]**2) * np.exp(-0.1 * np.abs(x[i] - x[j]))
                coupling *= np.sin(freq_mod * (x[i] + x[j]))
                coupling_term += coupling
        
        # Asymmetric energy wells with dynamic frequency modulation
        well_term = 0.0
        for i in range(self.dim):
            # Create asymmetric wells using piecewise functions
            if x[i] < 0:
                well = (x[i]**3) * np.exp(-0.5 * x[i]**2)
            else:
                well = x[i]**4 * np.cos(x[i])
            well_term += well
        
        # Cross-dimensional symmetry breaking terms
        symmetry_break = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Break symmetry with non-linear coupling
                symmetry_break += np.tanh((x[i] * x[j])**2) * np.sin(x[i] + x[j])
        
        # Global scaling and complexity enhancement based on dimensionality
        total = 0.3 * result + 0.25 * fractional_term + 0.2 * coupling_term + 0.15 * well_term + 0.1 * symmetry_break
        
        # Enhanced chaos through dimensionality-dependent scaling
        scaling = 1.0 + 0.2 * self.dim + 0.05 * np.sin(self.dim * 0.3)
        
        return total * scaling