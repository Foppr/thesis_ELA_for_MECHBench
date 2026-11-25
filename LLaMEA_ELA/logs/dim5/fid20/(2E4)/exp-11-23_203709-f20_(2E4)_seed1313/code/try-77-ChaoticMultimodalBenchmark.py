import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic trigonometric components with dynamic frequencies and phases
        trig_component = 0
        for i in range(self.dim):
            freq = 1.5 + 4.0 * np.sin(0.5 * i + 1.2)
            phase = 0.3 * np.cos(0.7 * i + 0.5)
            trig_component += np.sin(freq * x[i] + phase) * np.cos(freq * x[i] / 1.8 + phase) * np.exp(-0.1 * abs(x[i]))
        
        # Adaptive radial basis function with dynamic centers and variable widths
        rbf_component = 0
        for i in range(self.dim):
            center = -4.5 + 9.0 * (i / (self.dim - 1) if self.dim > 1 else 0.5)
            variance = 0.3 + 0.7 * np.sin(0.8 * i + 0.4)
            rbf_component += 2.5 / (1.0 + ((x[i] - center) / variance)**2.5)
        
        # Enhanced multiquadratic kernel interactions with chaotic coupling
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dx = x[i] - x[j]
                dy = np.sin(2.5 * dx) * np.cos(1.2 * dx)
                dist = np.sqrt(dx**2 + dy**2)
                interaction += 1.0 / (1.0 + dist**1.8)
        
        # Polynomial chaos expansion with chaotic coefficients and higher-order terms
        poly_component = 0
        for i in range(self.dim):
            coeff = 0.4 + 0.6 * np.sin(1.3 * i + 0.5)
            poly_component += coeff * (x[i]**6 - 2.5 * x[i]**4 + 2.0 * x[i]**2 - 0.5)
        
        # Dynamic conditioning factor with chaotic scaling and dimensionality adjustment
        condition_factor = 1.0 + 0.3 * np.log(self.dim + 1) * np.sin(0.4 * self.dim + 0.2)
        
        # Combine all components with optimized weights
        return 3.0 * trig_component + 4.0 * rbf_component + 0.9 * interaction + 0.7 * poly_component + 30.0 * condition_factor