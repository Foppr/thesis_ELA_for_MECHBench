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
            freq = 18 + 10 * np.sin(i * np.pi / 4)
            grad_component += (xi**3) * np.sin(freq * xi) * np.exp(-0.4 * xi**2)
        
        # Enhanced polynomial correlation with modified weights
        poly_corr = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            poly_corr += (1.5 * xi**4 + 1.1 * xi**3 + 0.8 * xi**2 + 0.5 * xi)
        
        # Adaptive dimensionality scaling with stronger cross-term interactions
        adaptive_scale = 1.0 + 0.9 * np.sin(self.dim * np.pi / 6)
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_terms += (x_scaled[i] * x_scaled[j]) / (1 + 0.3 * abs(x_scaled[i] - x_scaled[j]))
        
        # Enhanced sinusoidal perturbation with increased frequency and amplitude
        perturb = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            perturb += np.sin(35 * xi) * np.cos(25 * xi) * (1 + 0.6 * np.sin(i))
        
        # Final combined function with updated dynamic weighting
        return adaptive_scale * (grad_component + 0.8 * poly_corr + 0.6 * cross_terms + 0.4 * perturb)