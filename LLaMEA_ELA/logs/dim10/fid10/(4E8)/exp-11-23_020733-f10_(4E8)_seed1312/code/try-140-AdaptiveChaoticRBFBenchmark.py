import numpy as np

class AdaptiveChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = 0.1 * np.sum(x**2)
        
        # Gaussian radial basis functions with chaotic center placement
        for i in range(min(8, self.dim)):
            center = 3.0 * np.sin(i * np.pi / (self.dim + 2)) * np.cos(i * np.pi / (self.dim + 3))
            width = 1.5 + 0.5 * np.sin(i * np.pi / (self.dim + 4))
            exponent = -np.sum((x - center)**2) / (2 * width**2)
            result += 2.0 * np.exp(exponent) * np.sin(4 * x[i]) * np.cos(3 * x[i])
        
        # Sine-cosine chaotic modulation with dynamic frequencies
        for i in range(self.dim):
            freq1 = 1.5 + 0.8 * np.sin(i * np.pi / self.dim)
            freq2 = 2.0 + 0.6 * np.cos(i * np.pi / (self.dim + 1))
            chaos_mod = 1.0 + 0.3 * np.sin(5 * x[i] + i * np.pi / 3) * np.cos(4 * x[i] - i)
            result += 1.5 * np.sin(freq1 * x[i]) * np.cos(freq2 * x[i]) * chaos_mod
        
        # Adaptive polynomial scaling with chaotic weights
        poly_weights = []
        for i in range(self.dim):
            weight = 1.0 + 0.4 * np.sin(i * np.pi / (self.dim + 5))
            poly_weights.append(weight)
        
        for i in range(self.dim):
            result += poly_weights[i] * (x[i]**4 - 2 * x[i]**3 + x[i]**2)
        
        # Cross-dimensional coupling with chaotic interaction strengths
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                coupling_strength = 0.5 + 0.3 * np.sin(i * j * np.pi / (self.dim + 2))
                interaction = coupling_strength * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                result += interaction
        
        # Boundary penalty with variable scaling factors
        boundary_penalty = 0.0
        for i in range(self.dim):
            if abs(x[i]) > 4.0:
                scale_factor = 15.0 + 3.0 * np.sin(i * np.pi / (self.dim + 2))
                boundary_penalty += scale_factor * (abs(x[i]) - 4.0)**3
        result += boundary_penalty
        
        # Multi-scale chaotic modulation with varying amplitudes
        for i in range(self.dim):
            amp = 0.8 + 0.4 * np.sin(i * np.pi / self.dim)
            mod_freq = 3.0 + 2.0 * np.cos(i * np.pi / (self.dim + 1))
            result += amp * np.sin(mod_freq * x[i]) * np.tan(0.5 * x[i])
        
        return result