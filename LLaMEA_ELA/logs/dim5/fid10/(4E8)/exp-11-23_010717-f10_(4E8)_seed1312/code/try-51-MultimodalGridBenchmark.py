import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin
        global_min = 0.0
        
        # Enhanced sinusoidal terms creating complex multimodal structure
        sin_terms = 0.0
        for i in range(self.dim):
            sin_terms += np.sin(5.0 * x[i]) * np.cos(3.0 * x[i]) + 0.5 * np.sin(2.0 * x[i])**3
        
        # Fractal-like basin terms with varying exponents
        basin_terms = 0.0
        for i in range(self.dim):
            basin_terms += 0.3 * np.abs(x[i])**1.7 + 0.2 * np.abs(x[i])**2.3
        
        # Cross-dimensional interaction terms with higher-order coupling
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_terms += 0.3 * np.sin(0.8 * x[i]) * np.cos(0.5 * x[j]) * (x[i]**2 + x[j]**2)**1.5
        
        # Additional noise scaling and perturbation terms
        noise_terms = 0.0
        for i in range(self.dim):
            noise_terms += 0.1 * np.sin(10.0 * x[i]) * np.cos(7.0 * x[i])
        
        # Distance-based penalty to encourage convergence with chaotic scaling
        distance_penalty = 0.02 * np.sum(x**2) + 0.005 * np.sum(np.abs(x)**3)
        
        # Modified cross-term interactions for enhanced challenge
        modified_cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                modified_cross += 0.15 * (x[i] * x[j])**2.5 + 0.1 * np.sin(0.3 * x[i] + 0.4 * x[j])
        
        # Perturb global minimum slightly to increase challenge
        perturbation = 0.002 * np.sum(x**7) + 0.001 * np.sum(np.abs(x)**5)
        
        return sin_terms + basin_terms + cross_terms + noise_terms + distance_penalty + modified_cross + perturbation