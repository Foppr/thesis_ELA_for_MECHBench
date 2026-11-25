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
            # Modified chaotic frequency with higher variability and non-linearity
            freq = 25 + 15 * np.sin(i * np.pi / 3) + 7 * np.cos(i * np.pi / 2.5)
            grad_component += (xi**3) * np.sin(freq * xi) * np.exp(-0.5 * xi**2)
        
        # Enhanced polynomial correlation with modified weights and added interaction terms
        poly_corr = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            poly_corr += (1.8 * xi**4 + 1.3 * xi**3 + 0.9 * xi**2 + 0.6 * xi)
        
        # Adaptive dimensionality scaling with stronger cross-term interactions and dynamic coupling
        adaptive_scale = 1.0 + 1.1 * np.sin(self.dim * np.pi / 5) * np.cos(self.dim * np.pi / 7)
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Enhanced interaction with distance-dependent weighting
                dist = abs(x_scaled[i] - x_scaled[j])
                weight = 1.0 / (1 + 0.4 * dist**2)
                cross_terms += (x_scaled[i] * x_scaled[j]) * weight
        
        # Enhanced sinusoidal perturbation with increased frequency, amplitude, and dimensionality dependence
        perturb = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            perturb += np.sin(40 * xi) * np.cos(30 * xi) * (1 + 0.7 * np.sin(i * np.pi / 2.5))
        
        # Novel dynamic weighting scheme based on input magnitude and dimensionality
        magnitude = np.sum(np.abs(x_scaled)) / self.dim
        weight_factor = 1.0 + 0.5 * np.sin(magnitude * np.pi)
        
        # Final combined function with updated dynamic weighting and improved conditioning
        return adaptive_scale * weight_factor * (grad_component + 0.9 * poly_corr + 0.7 * cross_terms + 0.5 * perturb)