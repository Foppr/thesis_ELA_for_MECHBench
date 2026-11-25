import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced sinusoidal oscillation with chaotic frequency modulation
        sin_component = 0
        for i in range(self.dim):
            freq = 1.0 + 4.0 * np.sin(0.3 * i + 1.0) * np.cos(0.2 * i + 0.5)
            amp = 1.0 + 0.8 * np.sin(0.4 * i + 0.7)
            sin_component += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] / 3.0)
        
        # Modified radial basis function with chaotic center placement and variance
        rbf_component = 0
        for i in range(self.dim):
            center = -4.5 + 9.0 * (i / (self.dim - 1) if self.dim > 1 else 0.5)
            variance = 0.3 + 0.7 * np.sin(0.6 * i + 1.2)
            rbf_component += 2.5 * np.exp(-0.5 * ((x[i] - center) / variance)**2)
        
        # Enhanced gradient coupling with multi-scale directional sensitivity and chaotic weights
        grad_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dx = x[i] - x[j]
                dy = np.sin(4.0 * dx) * np.cos(3.0 * dx)
                weight = 1.0 + 0.5 * np.sin(0.8 * (i + j))
                grad_coupling += weight * (dx**2 + dy**2) / (1.0 + np.abs(dx) + np.abs(dy))
        
        # Polynomial modulation with chaotic coefficient variations and additional terms
        poly_mod = 0
        for i in range(self.dim):
            coeff1 = 0.3 + 0.7 * np.sin(1.5 * i + 0.8)
            coeff2 = 0.2 + 0.6 * np.cos(1.2 * i + 0.4)
            poly_mod += coeff1 * x[i]**4 - coeff2 * x[i]**3 + 1.2 * x[i]**2
        
        # Enhanced conditioning factor with chaotic scaling
        condition_factor = 1.0 + 0.5 * np.log(self.dim + 1) * np.sin(0.5 * self.dim)
        
        # Additional chaotic modulation term
        chaos_mod = 0
        for i in range(self.dim):
            chaos_mod += np.sin(2.0 * x[i] + 1.0) * np.cos(1.5 * x[i] + 0.5) * np.tan(0.3 * x[i])
        
        # Combine components with modified weights
        return 3.0 * sin_component + 4.0 * rbf_component + 0.5 * grad_coupling + 0.7 * poly_mod + 40.0 * condition_factor + 2.0 * chaos_mod