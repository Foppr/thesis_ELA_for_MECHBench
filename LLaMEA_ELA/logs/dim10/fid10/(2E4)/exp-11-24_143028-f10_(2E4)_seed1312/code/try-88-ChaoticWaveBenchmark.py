import numpy as np

class ChaoticWaveBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = 0.2 * np.sum(x**2)
        
        # Enhanced multi-modal periodic wave interactions
        for i in range(self.dim):
            result += 1.8 * np.sin(15 * x[i]) * np.cos(12 * x[i]) * np.sin(10 * x[i]**2)
        
        # Modified exponential decay barriers near boundaries
        for i in range(self.dim):
            result += 3.0 * np.exp(-2.0 * (5.0 - np.abs(x[i]))**2) * (1 + 0.7 * np.sin(20 * x[i]))
        
        # Improved adaptive coupling with dynamic weights
        for i in range(self.dim):
            weight = 1.5 + 0.8 * np.cos(5 * x[i])
            result += weight * np.sin(18 * x[i]) * np.cos(13 * x[(i+1) % self.dim]) * np.tan(1.0 * (x[i] + x[(i+1) % self.dim]))
        
        # Enhanced fractal-like wave structure with recursive scaling
        for i in range(self.dim):
            result += 2.5 * np.sin(35 * x[i]) * np.cos(30 * x[i]) * np.sin(25 * x[i]**3) * (1 + 0.5 * np.abs(x[i]))
        
        # Modified high-order polynomial with chaotic modulation
        for i in range(self.dim):
            result += 1.2 * x[i]**7 * np.sin(10 * x[i]) * np.cos(8 * x[i]) * (1 + 0.6 * np.abs(x[i]))
        
        # Enhanced cross-dimensional exponential coupling with varying strengths
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Increased coupling range
                coupling_strength = 0.8 + 0.4 * np.sin(4 * (x[i] + x[j]))
                result += coupling_strength * np.exp(-np.abs(x[i] - x[j]) / (1 + 0.5 * (np.abs(x[i]) + np.abs(x[j])))) * np.sin(15 * (x[i] + x[j]))
        
        # Additional enhanced multimodal term with varying frequencies
        for i in range(self.dim):
            freq = 30 + 10 * np.sin(x[i])
            result += 1.2 * np.sin(freq * x[i]) * np.cos(18 * x[i]**2) * np.tan(0.7 * x[i])
        
        # Enhanced boundary-sensitive penalty with logarithmic scaling
        boundary_penalty = 0
        for i in range(self.dim):
            boundary_penalty += 3.5 * (np.abs(x[i]) - 5.0)**2 / (1 + np.exp(-0.7 * np.abs(x[i])))
        result += boundary_penalty
        
        # Enhanced wave interference pattern with phase modulation
        sum_x = np.sum(x)
        result += 2.5 * np.sin(40 * sum_x) * np.cos(35 * sum_x) * np.tan(3.0 * sum_x) * (1 + 0.4 * np.abs(sum_x))
        
        # Enhanced recursive fractal-like structure with self-similarity
        for i in range(self.dim):
            result += 1.8 * np.sin(50 * x[i]) * np.cos(45 * x[i]) * np.sin(40 * x[i]**4) * (1 + 0.4 * x[i]**2)
        
        return result