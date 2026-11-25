import numpy as np

class PolynomialLogisticCouplingLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute logistic map parameters for chaotic behavior
        self.logistic_r = 3.8 + 0.2 * np.random.rand(dim)
        # Precompute polynomial potential centers and exponents
        self.potential_centers = np.random.uniform(-1, 1, dim)
        self.exponents = 2 + 3 * np.random.rand(dim)
        # Precompute coupling weights between dimensions
        self.coupling_weights = np.random.uniform(-0.5, 0.5, (dim, dim))
        # Precompute chaotic sequence for dynamic conditioning
        self.chaotic_seq = np.array([self._logistic_map(0.5, self.logistic_r[i]) for i in range(dim)])
        
    def _logistic_map(self, x, r):
        return r * x * (1 - x)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial potential component with varying exponents
        poly_sum = 0.0
        for i in range(self.dim):
            dist = np.sum((x_norm - self.potential_centers[i])**2)
            poly_sum += (dist**self.exponents[i]) * np.sin(3 * x_norm[i])
        
        # Logistic map component with dynamic scaling
        logistic_sum = 0.0
        for i in range(self.dim):
            x_chaos = self.chaotic_seq[i]
            logistic_sum += (x_chaos - 0.5) * np.cos(2 * x_norm[i]) * np.exp(-0.4 * x_norm[i]**2)
        
        # Coupling component with gradient-based interactions
        coupling_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_term = self.coupling_weights[i, j] * (x_norm[i] - x_norm[j])**2
                    coupling_sum += coupling_term * np.exp(-0.3 * coupling_term)
        
        # Multi-modal harmonic component with varying frequencies
        harm_sum = 0.0
        for i in range(self.dim):
            freq = 1 + 2 * np.sin(i * np.pi / self.dim)
            harm_sum += np.cos(freq * x_norm[i]) * np.exp(-0.1 * x_norm[i]**2)
        
        # Basin-forming pathway component with sigmoid barriers
        basin_sum = 0.0
        for i in range(self.dim):
            barrier = 1.0 + 0.5 * (1.0 / (1.0 + np.exp(-3 * x_norm[i])))
            basin_sum += barrier * (x_norm[i]**5 - x_norm[i]**3) * np.exp(-0.2 * x_norm[i]**2)
        
        # Combined landscape with adaptive scaling
        result = 0.3 * poly_sum + 0.2 * logistic_sum + 0.25 * coupling_sum + 0.15 * harm_sum + 0.1 * basin_sum
        
        # Dynamic conditioning factor based on logistic map sequence and input magnitude
        condition_factor = 1.0
        for i in range(self.dim):
            chaos_factor = self.chaotic_seq[i] * (1.0 + 0.2 * np.sin(x_norm[i]))
            condition_factor *= (1.0 + 0.4 * np.abs(x_norm[i]) + 0.08 * x_norm[i]**6 + 0.15 * chaos_factor)
        
        # Final transformation with global scaling and noise modulation
        noise = 0.01 * np.sum(np.cos(x_norm * 5))
        return result * condition_factor + noise + 0.03 * np.sum(x_norm**7)