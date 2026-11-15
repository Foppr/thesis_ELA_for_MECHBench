import numpy as np

class FractalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        result = np.sum(x**2)
        
        # Quaternion-inspired coupling terms for non-separability
        quaternion_coupling = 0.0
        for i in range(0, self.dim - 3, 4):
            if i + 3 < self.dim:
                a, b, c, d = x[i], x[i+1], x[i+2], x[i+3]
                quaternion_coupling += (a*b + c*d)**2 + (a*d - b*c)**2
        
        # Exponential decay oscillations with varying frequencies
        exp_osc = 0.0
        for i in range(self.dim):
            exp_osc += np.exp(-0.1 * np.abs(x[i])) * np.sin(2.0 * np.pi * x[i] * (i + 1))
        
        # Fractal-like self-similar peaks using recursive sine-cosine combinations
        fractal_peaks = 0.0
        for i in range(self.dim):
            fractal_peaks += np.sin(np.pi * x[i] * np.sin(np.pi * x[i]))**2
        
        # Chaotic perturbation using logistic map-like behavior
        chaotic_pert = 0.0
        r = 3.9
        for i in range(self.dim):
            chaotic_pert += np.sin(r * x[i] * np.sin(x[i]))**2
        
        # High-dimensional saddle point interactions
        saddle = 0.0
        for i in range(0, self.dim - 1, 2):
            if i + 1 < self.dim:
                saddle += (x[i]**2 - x[i+1]**2)**2
        
        # Multi-scale multimodal component with varying amplitudes
        multi_scale = 0.0
        for i in range(self.dim):
            multi_scale += np.sin(5.0 * x[i]) * np.cos(3.0 * x[i]) * np.exp(-0.05 * x[i]**2)
        
        # Combine all terms
        result = result + 0.5 * quaternion_coupling + 0.3 * exp_osc + 0.4 * fractal_peaks + 0.2 * chaotic_pert + 0.3 * saddle + 0.25 * multi_scale
        
        return result