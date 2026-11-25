import numpy as np

class AdaptivePolynomialSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Scale input to [-5, 5] domain if needed
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Polynomial base with adaptive coefficients
        for i in range(self.dim):
            coeff = 1.0 + 0.3 * np.sin(0.5 * i)
            result += coeff * (x[i] ** 4) + 0.5 * (x[i] ** 3) + 0.2 * (x[i] ** 2)
        
        # Exponential decay with directional dependence
        for i in range(self.dim):
            direction_factor = np.exp(-0.1 * abs(x[i]))
            result += 0.8 * np.exp(-0.5 * (x[i] ** 2)) * direction_factor
        
        # Sinusoidal components with varying frequencies and amplitudes
        for i in range(self.dim):
            freq = 2.0 + 0.5 * i
            amp = 1.0 + 0.2 * np.cos(0.3 * i)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] / 2.0)
        
        # Cross-dimensional coupling with adaptive weights
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.3 + 0.1 * np.sin(0.2 * (i + j))
                result += weight * np.sin(x[i] * x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Radial component with adaptive frequency
        if self.dim >= 2:
            r = np.sqrt(np.sum(x[:2]**2))
            freq = 3.0 + 0.2 * self.dim
            result += 0.6 * np.sin(freq * r) * np.exp(-0.2 * r)
        
        # Asymmetric terms with threshold-based scaling
        for i in range(self.dim):
            if x[i] > 0:
                result += 0.4 * np.exp(-0.3 * x[i]) * (1.0 + 0.1 * x[i]**3)
            else:
                result += 0.5 * np.exp(-0.4 * abs(x[i])) * (1.0 + 0.15 * abs(x[i])**3)
        
        # Boundary attraction with variable strength
        for i in range(self.dim):
            boundary_strength = 0.2 + 0.1 * np.sin(i)
            result += boundary_strength * (5.0 - abs(x[i]))**2
        
        # High-frequency oscillatory component with adaptive amplitude
        for i in range(self.dim):
            amp = 0.8 + 0.2 * np.cos(0.4 * i)
            result += amp * np.sin(15.0 * x[i]) * np.cos(12.0 * x[i])
        
        # Adaptive polynomial interaction terms
        for i in range(min(self.dim, 3)):
            for j in range(i+1, min(self.dim, 4)):
                result += 0.25 * (x[i] ** 2) * (x[j] ** 3) * np.sin(x[i] + x[j])
        
        # Global modulation with sum of absolute values
        sum_abs = np.sum(np.abs(x))
        result += 0.3 * np.exp(-0.1 * sum_abs) * np.sin(2.0 * sum_abs)
        
        return result