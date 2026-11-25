import numpy as np

class ChaoticDelayedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute delay indices for time-delayed interactions
        self.delay_indices = [max(0, i - 2) for i in range(dim)]
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = np.sum(x**2) / self.dim
        
        # Chaotic logistic map components with delayed feedback
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Delayed chaotic dynamics
            delayed_x = x[self.delay_indices[i]] if self.delay_indices[i] < self.dim else 0.0
            # Logistic-like chaotic behavior with time-delayed coupling
            chaotic_val = 4.0 * xi * (1.0 - xi) + 0.3 * delayed_x * (1.0 - delayed_x)
            f2 += np.sin(chaotic_val * 10.0)**2
        
        # Multi-scale sinusoidal modulations with varying frequencies and amplitudes
        f3 = 0.0
        for i in range(self.dim):
            xi = x[i]
            freqs = [5.0, 12.0, 20.0, 30.0]
            amps = [0.8, 0.6, 0.4, 0.2]
            mod = 0.0
            for f, a in zip(freqs, amps):
                mod += a * np.sin(f * xi) * np.cos(f * xi**1.5)
            f3 += mod**2
        
        # Cross-dimensional coupling with asymmetric interaction weights
        f4 = 0.0
        for i in range(self.dim - 1):
            xi, xj = x[i], x[i+1]
            # Asymmetric coupling with exponential weighting
            coupling = np.exp(-0.5 * (xi - xj)**2) * (xi**3 + 0.5 * xj**2)
            f4 += coupling
        
        # Fractional power chaotic components with varying exponents
        f5 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Varying fractional exponents to increase nonlinearity
            exps = [1.3, 2.7, 3.1, 4.9]
            frac_val = np.sum([0.5 * np.abs(xi)**(exp + np.sin(i)) for exp in exps])
            f5 += frac_val
        
        # Saddle point structure with multi-scale interference
        f6 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Multi-scale saddle points with varying curvatures
            f6 += (xi**4 - 2.0 * xi**2) * np.cos(5.0 * xi)
        
        # Combine all components with adjusted weights
        return f1 + 0.5 * f2 + 0.3 * f3 + 0.2 * f4 + 0.4 * f5 + 0.1 * f6