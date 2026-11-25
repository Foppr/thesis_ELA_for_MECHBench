import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Sinusoidal periodic components with varying frequencies and amplitudes
        sin_component = np.sum(np.sin(2 * np.pi * x_scaled) * np.cos(4 * np.pi * x_scaled**2))
        
        # Radial basis function terms with multi-scale influence
        radial_terms = np.sum(np.exp(-np.sum((x_scaled[:, None] - x_scaled[None, :])**2, axis=0) / (2 * 0.5**2)))
        
        # Quadratic cross-dimensional interactions with varying coupling strengths
        quadratic_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                quadratic_coupling += (x_scaled[i] - x_scaled[j])**2 * (i + j) / (self.dim**2)
        
        # Hyperbolic tangent modulation with dynamic scaling factor
        tanh_mod = np.sum(np.tanh(3 * x_scaled) * np.sin(0.5 * self.dim * x_scaled))
        
        # Multi-modal exponential decay terms with localized peaks
        exp_decay = np.sum(np.exp(-np.abs(x_scaled)) * np.cos(10 * x_scaled**2))
        
        # Adaptive noise-like perturbations based on dimensionality
        noise_pert = 0.1 * np.sum(np.sin(self.dim * x_scaled) * np.cos(self.dim * x_scaled**3))
        
        # Combine all components with carefully tuned weights
        return 2.5 * sin_component + 1.8 * radial_terms + 0.7 * quadratic_coupling + 0.6 * tanh_mod + 0.4 * exp_decay + 0.3 * noise_pert