import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Periodic trigonometric components with varying frequencies and phases
        trig_component = 0
        for i in range(self.dim):
            freq = 1.5 + 4.0 * np.sin(0.5 * i + 1.2)
            phase = 0.3 * np.cos(0.7 * i + 0.2)
            trig_component += np.sin(freq * x[i] + phase) * np.cos(freq * x[i] / 1.8 + phase)
        
        # Radial basis function with multiquadratic kernel and dynamic centers
        rbf_component = 0
        for i in range(self.dim):
            center = -4.5 + 9.0 * (i / (self.dim - 1) if self.dim > 1 else 0.5)
            variance = 0.3 + 0.7 * np.sin(0.8 * i + 0.4)
            rbf_component += 2.5 / (1.0 + ((x[i] - center) / variance)**2)
        
        # Multiquadratic kernel interactions between dimensions
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dx = x[i] - x[j]
                dy = np.sin(2.5 * dx) * np.cos(2.0 * dx)
                dist = np.sqrt(dx**2 + dy**2)
                interaction += 1.0 / (1.0 + dist**2)
        
        # Polynomial chaos expansion with chaotic coefficients
        poly_component = 0
        for i in range(self.dim):
            coeff = 0.3 + 0.7 * np.sin(1.0 * i + 0.5)
            poly_component += coeff * (x[i]**5 - 2.0 * x[i]**3 + x[i])
        
        # Dynamic conditioning factor with chaotic scaling
        condition_factor = 1.0 + 0.3 * np.log(self.dim + 1) * np.sin(0.4 * self.dim)
        
        # Combine all components
        return 3.0 * trig_component + 4.0 * rbf_component + 0.9 * interaction + 0.7 * poly_component + 30.0 * condition_factor