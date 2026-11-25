import numpy as np

class ChaoticPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters for each dimension
        self.chebyshev_coeffs = np.array([0.5, -0.3, 0.2, -0.1, 0.05])
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic tent map component with parameter modulation
        f1 = 0.0
        for i in range(self.dim):
            # Tent map with time-varying parameter based on dimension and position
            a = 1.8 + 0.2 * np.sin(0.3 * i + 0.1 * np.sum(x))
            if x[i] < a:
                tent_val = x[i] / a
            else:
                tent_val = (1 - x[i]) / (1 - a)
            f1 += tent_val**2 * np.exp(-0.1 * x[i]**2)
            
        # Polynomial chaos expansion with adaptive weights
        f2 = 0.0
        for i in range(self.dim):
            # Use Chebyshev polynomials with dimension-specific coefficients
            T_n = np.cos(i * np.arccos(np.clip(x[i], -1, 1)))
            weight = self.chebyshev_coeffs[i % len(self.chebyshev_coeffs)]
            f2 += weight * T_n * np.exp(-0.05 * x[i]**2)
            
        # Adaptive gradient modulation with dimension coupling
        f3 = 0.0
        for i in range(self.dim):
            # Gradient scaling based on neighborhood
            grad_scale = 1.0 + 0.5 * np.sin(0.4 * i + 0.2 * np.sum(x**2))
            f3 += grad_scale * x[i]**3 * np.exp(-0.1 * x[i]**2)
            
        # Cross-dimensional polynomial coupling with chaotic interaction
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic interaction strength based on both dimensions
                interaction_strength = 0.3 + 0.2 * np.sin(0.5 * (x[i] + x[j]))
                f4 += interaction_strength * (x[i]**2 + x[j]**2) * np.exp(-0.02 * (x[i]**2 + x[j]**2))
                
        # Multi-scale chaotic oscillations
        f5 = 0.0
        for i in range(self.dim):
            freq = 3.0 + 1.5 * np.sin(0.2 * i)
            amp = 1.0 + 0.5 * np.cos(0.3 * i)
            f5 += amp * np.sin(freq * x[i]) * np.exp(-0.2 * x[i]**2)
            
        # Basin boundary complexity with exponential repulsion
        f6 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 3.0:
                dist = np.abs(x[i]) - 3.0
                penalty = 1.5 * dist**2.5 * np.exp(-0.15 * dist)
                f6 += penalty
                
        # Fractal-like self-similarity with recursive polynomial terms
        f7 = 0.0
        for i in range(self.dim):
            scale = 0.4 + 0.3 * np.sin(0.4 * i + 0.1 * np.sum(x**2))
            poly_term = x[i]**5 - 2*x[i]**3 + x[i]
            f7 += scale * poly_term * np.exp(-0.1 * x[i]**2)
            
        # Time-varying conditioning with chaotic modulation
        f8 = 0.0
        r = np.sqrt(np.sum(x**2))
        for i in range(self.dim):
            cond_factor = 1.0 + 0.7 * np.sin(0.3 * r + 0.2 * i)
            f8 += cond_factor * x[i]**4
            
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8