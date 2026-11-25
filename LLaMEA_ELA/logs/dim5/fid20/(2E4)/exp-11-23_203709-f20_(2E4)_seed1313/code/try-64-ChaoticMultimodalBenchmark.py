import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine wave component with varying frequencies and amplitudes
        sin_component = 0
        for i in range(self.dim):
            freq = 1.0 + 4.0 * np.sin(0.3 * i + 1.0)
            amp = 2.0 + np.cos(0.5 * i)
            sin_component += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] / 3.0)
        
        # Adaptive radial basis function with dynamic variance and center positions
        rbf_component = 0
        for i in range(self.dim):
            center = -4.5 + 9.0 * (i / (self.dim - 1) if self.dim > 1 else 0.5)
            variance = 0.3 + 0.7 * np.sin(0.8 * i + 0.5)
            rbf_component += 2.5 * np.exp(-0.5 * ((x[i] - center) / variance)**2)
        
        # Directional gradient coupling with multi-scale directional sensitivity
        grad_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dx = x[i] - x[j]
                dy = np.sin(4.0 * dx) * np.cos(2.5 * dx)
                grad_coupling += 2.0 * (dx**2 + dy**2) / (1.0 + np.abs(dx) + np.abs(dy))
        
        # Enhanced polynomial modulation with chaotic coefficient variations
        poly_mod = 0
        for i in range(self.dim):
            coeff = 0.3 + 0.7 * np.sin(1.5 * i + 0.2)
            poly_mod += coeff * x[i]**4 - 1.8 * x[i]**3 + 1.2 * x[i]**2
        
        # Dimensionality-dependent conditioning factor with chaotic scaling
        condition_factor = 1.0 + 0.15 * np.log(self.dim + 1) * np.sin(0.4 * self.dim)
        
        # Combine components with adjusted weights for better balance
        return 3.0 * sin_component + 4.0 * rbf_component + 0.5 * grad_coupling + 0.7 * poly_mod + 32.0 * condition_factor