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
            freq = 2.0 + 3.0 * np.sin(0.4 * i + 1.0)
            phase = 0.5 * np.cos(0.6 * i)
            trig_component += np.sin(freq * x[i] + phase) * np.cos(freq * x[i] / 2.0 + phase)
        
        # Radial basis function with multiquadratic kernel and dynamic centers
        rbf_component = 0
        for i in range(self.dim):
            center = -4.0 + 8.0 * (i / (self.dim - 1) if self.dim > 1 else 0.5)
            variance = 0.5 + 0.5 * np.sin(0.7 * i + 0.3)
            rbf_component += 3.0 / (1.0 + ((x[i] - center) / variance)**2)
        
        # Multiquadratic kernel interactions between dimensions
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dx = x[i] - x[j]
                dy = np.sin(3.0 * dx) * np.cos(1.5 * dx)
                dist = np.sqrt(dx**2 + dy**2)
                interaction += 1.0 / (1.0 + dist**2)
        
        # Polynomial chaos expansion with chaotic coefficients
        poly_component = 0
        for i in range(self.dim):
            coeff = 0.5 + 0.5 * np.sin(1.2 * i + 0.4)
            poly_component += coeff * (x[i]**5 - 2.0 * x[i]**3 + x[i])
        
        # Dynamic conditioning factor with chaotic scaling
        condition_factor = 1.0 + 0.2 * np.log(self.dim + 1) * np.sin(0.3 * self.dim)
        
        # Combine all components
        return 2.5 * trig_component + 3.5 * rbf_component + 0.8 * interaction + 0.6 * poly_component + 28.0 * condition_factor