import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Chaotic gradient component with enhanced sinusoidal modulation
        grad_component = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            # Modified chaotic frequency with higher variability
            freq = 15 + 8 * np.sin(i * np.pi / 3)
            grad_component += (xi**3) * np.sin(freq * xi) * np.exp(-0.3 * xi**2)
        
        # Enhanced polynomial correlation with modified weights
        poly_corr = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            poly_corr += (1.2 * xi**4 + 0.9 * xi**3 + 0.6 * xi**2 + 0.4 * xi)
        
        # Adaptive dimensionality scaling with stronger cross-term interactions
        adaptive_scale = 1.0 + 0.7 * np.sin(self.dim * np.pi / 5)
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_terms += (x_scaled[i] * x_scaled[j]) / (1 + 0.2 * abs(x_scaled[i] - x_scaled[j]))
        
        # Enhanced sinusoidal perturbation with increased frequency and amplitude
        perturb = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            perturb += np.sin(30 * xi) * np.cos(20 * xi) * (1 + 0.5 * np.sin(i))
        
        # Final combined function with updated dynamic weighting
        return adaptive_scale * (grad_component + 0.7 * poly_corr + 0.5 * cross_terms + 0.3 * perturb)