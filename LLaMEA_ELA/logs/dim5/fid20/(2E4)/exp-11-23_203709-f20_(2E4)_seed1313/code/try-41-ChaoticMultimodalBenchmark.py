import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Trigonometric chaotic component with multiple frequencies and amplitudes
        chaotic = 0
        for i in range(self.dim):
            chaotic += (2.5 * np.sin(5.2 * x[i]) * np.cos(3.8 * x[i]) + 
                       1.8 * np.sin(7.9 * x[i]) * np.cos(4.1 * x[i]) + 
                       0.9 * np.sin(9.3 * x[i]) * np.cos(2.7 * x[i]))
        
        # Radial basis function components with varying centers and widths
        rbf = 0
        centers = np.linspace(-4, 4, min(5, self.dim))
        for i in range(self.dim):
            center = centers[i % len(centers)] if len(centers) > 0 else 0
            rbf += 3.1 * np.exp(-0.5 * ((x[i] - center) / 1.2)**2) + \
                   2.4 * np.exp(-0.3 * ((x[i] - center) / 1.8)**2)
        
        # Cross-dimensional interaction terms with sinusoidal coupling
        cross_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited interaction scope
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                cross_interaction += 1.5 * np.sin(6.3 * dist) * np.cos(4.7 * dist) / (dist**2.1 + 0.05)
        
        # Polynomial modulation with higher-order terms and chaotic scaling
        poly_mod = 0
        for i in range(self.dim):
            poly_mod += 0.8 * x[i]**6 - 1.2 * x[i]**5 + 0.9 * x[i]**4 - 0.3 * x[i]**3
        
        # Combine all components with appropriate scaling factors
        return 1.2 * chaotic + 2.8 * rbf + 0.25 * cross_interaction + 0.6 * poly_mod + 35.0 * self.dim