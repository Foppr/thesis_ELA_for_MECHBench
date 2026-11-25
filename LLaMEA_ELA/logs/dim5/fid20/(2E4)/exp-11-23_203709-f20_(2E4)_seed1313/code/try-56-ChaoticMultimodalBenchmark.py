import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal oscillation component with varying frequencies and amplitudes
        sin_component = 0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(0.5 * i)
            amp = 1.5 + 0.5 * np.cos(0.3 * i)
            sin_component += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] / 2.0)
        
        # Adaptive radial basis function with dynamic variance and center positions
        rbf_component = 0
        for i in range(self.dim):
            center = -4.0 + 8.0 * (i / (self.dim - 1) if self.dim > 1 else 0.5)
            variance = 0.5 + 0.5 * np.sin(0.7 * i)
            rbf_component += 3.0 * np.exp(-0.5 * ((x[i] - center) / variance)**2)
        
        # Directional gradient coupling with multi-scale directional sensitivity
        grad_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dx = x[i] - x[j]
                dy = np.sin(3.0 * dx) * np.cos(2.0 * dx)
                grad_coupling += 1.8 * (dx**2 + dy**2) / (1.0 + np.abs(dx) + np.abs(dy))
        
        # Polynomial modulation with chaotic coefficient variations
        poly_mod = 0
        for i in range(self.dim):
            coeff = 0.5 + 0.5 * np.sin(1.3 * i)
            poly_mod += coeff * x[i]**4 - 2.0 * x[i]**3 + 1.5 * x[i]**2
        
        # Dimensionality-dependent conditioning factor
        condition_factor = 1.0 + 0.2 * np.log(self.dim + 1)
        
        # Combine components with dynamic weights
        return 2.5 * sin_component + 3.5 * rbf_component + 0.4 * grad_coupling + 0.6 * poly_mod + 35.0 * condition_factor