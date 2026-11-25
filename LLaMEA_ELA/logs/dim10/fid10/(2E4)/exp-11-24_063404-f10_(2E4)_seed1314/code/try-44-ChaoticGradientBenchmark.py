import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Chaotic gradient component with sinusoidal modulation
        grad_component = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            # Sinusoidal modulation with chaotic frequency
            freq = 10 + 5 * np.sin(i * np.pi / 4)
            grad_component += (xi**3) * np.sin(freq * xi) * np.exp(-0.5 * xi**2)
        
        # Polynomial correlation with adaptive weights
        poly_corr = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            poly_corr += (xi**4 + 0.7 * xi**3 + 0.5 * xi**2 + 0.3 * xi)
        
        # Adaptive dimensionality scaling with cross-term interactions
        adaptive_scale = 1.0 + 0.5 * np.sin(self.dim * np.pi / 4)
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_terms += (x_scaled[i] * x_scaled[j]) / (1 + 0.1 * abs(x_scaled[i] - x_scaled[j]))
        
        # Sinusoidal perturbation with varying frequency and amplitude
        perturb = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            perturb += np.sin(25 * xi) * np.cos(15 * xi) * (1 + 0.3 * np.sin(i))
        
        # Final combined function with dynamic weighting
        return adaptive_scale * (grad_component + 0.6 * poly_corr + 0.4 * cross_terms + 0.2 * perturb)