import numpy as np

class ChaoticWaveBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = 0.5 * np.sum(x**2)
        
        # Multi-modal periodic wave interactions
        for i in range(self.dim):
            result += 2.0 * np.sin(10 * x[i]) * np.cos(8 * x[i]) * np.sin(6 * x[i]**2)
        
        # Exponential decay barriers near boundaries
        for i in range(self.dim):
            result += 3.0 * np.exp(-2.0 * (5.0 - np.abs(x[i]))**2) * (1 + 0.5 * np.sin(15 * x[i]))
        
        # Adaptive coupling with dynamic weights
        for i in range(self.dim):
            weight = 1.0 + 0.8 * np.cos(3 * x[i])
            result += weight * np.sin(12 * x[i]) * np.cos(9 * x[(i+1) % self.dim]) * np.tan(0.7 * (x[i] + x[(i+1) % self.dim]))
        
        # Fractal-like wave structure with recursive scaling
        for i in range(self.dim):
            result += 1.5 * np.sin(25 * x[i]) * np.cos(20 * x[i]) * np.sin(15 * x[i]**3) * (1 + 0.3 * np.abs(x[i]))
        
        # High-order polynomial with chaotic modulation
        for i in range(self.dim):
            result += 0.8 * x[i]**5 * np.sin(7 * x[i]) * np.cos(5 * x[i]) * (1 + 0.4 * np.abs(x[i]))
        
        # Cross-dimensional exponential coupling with varying strengths
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling
                coupling_strength = 0.5 + 0.5 * np.sin(2 * (x[i] + x[j]))
                result += coupling_strength * np.exp(-np.abs(x[i] - x[j]) / (1 + 0.3 * (np.abs(x[i]) + np.abs(x[j])))) * np.sin(10 * (x[i] + x[j]))
        
        # Additional multimodal term with varying frequencies
        for i in range(self.dim):
            freq = 20 + 10 * np.sin(x[i])
            result += 1.2 * np.sin(freq * x[i]) * np.cos(12 * x[i]**2) * np.tan(0.5 * x[i])
        
        # Boundary-sensitive penalty with logarithmic scaling
        boundary_penalty = 0
        for i in range(self.dim):
            boundary_penalty += 2.5 * (np.abs(x[i]) - 5.0)**2 / (1 + np.exp(-0.5 * np.abs(x[i])))
        result += boundary_penalty
        
        # Complex wave interference pattern with phase modulation
        sum_x = np.sum(x)
        result += 1.8 * np.sin(30 * sum_x) * np.cos(25 * sum_x) * np.tan(2.0 * sum_x) * (1 + 0.2 * np.abs(sum_x))
        
        # Recursive fractal-like structure with self-similarity
        for i in range(self.dim):
            result += 1.0 * np.sin(40 * x[i]) * np.cos(35 * x[i]) * np.sin(30 * x[i]**4) * (1 + 0.25 * x[i]**2)
        
        return result