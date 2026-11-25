import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos expansion component with Hermite polynomials
        chaos_component = 0
        for i in range(self.dim):
            # Use Hermite polynomial of degree 3
            h3 = 2 * x[i]**3 - 3 * x[i]
            chaos_component += 1.2 * h3 * np.sin(1.5 * x[i]) * np.cos(0.8 * x[i])
        
        # Radial basis function with dynamic centers and variances
        rbf_component = 0
        for i in range(self.dim):
            center = -4.0 + 8.0 * (i / (self.dim - 1) if self.dim > 1 else 0.5)
            variance = 0.3 + 0.7 * np.sin(0.6 * i)
            rbf_component += 2.5 * np.exp(-0.5 * ((x[i] - center) / variance)**2)
        
        # Cross-dimensional coupling with multi-scale interaction terms
        cross_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dx = x[i] - x[j]
                dy = np.sin(2.0 * dx) * np.cos(1.5 * dx)
                cross_coupling += 1.5 * (dx**2 + dy**2) / (1.0 + np.abs(dx) + np.abs(dy))
        
        # Multi-scale sinusoidal modulation with frequency adaptation
        sin_mod = 0
        for i in range(self.dim):
            freq = 1.0 + 2.0 * np.sin(0.5 * i)
            amp = 0.8 + 0.4 * np.cos(0.3 * i)
            sin_mod += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] / 3.0)
        
        # Dimensionality-dependent conditioning factor
        condition_factor = 1.0 + 0.3 * np.log(self.dim + 1)
        
        # Combine components with dynamic weights
        return 3.0 * chaos_component + 2.0 * rbf_component + 0.5 * cross_coupling + 0.7 * sin_mod + 40.0 * condition_factor