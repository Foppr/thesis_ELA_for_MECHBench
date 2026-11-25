import numpy as np

class ChaoticWaveBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = 0.3 * np.sum(x**2)
        
        # Enhanced multi-modal periodic wave interactions
        for i in range(self.dim):
            result += 1.5 * np.sin(12 * x[i]) * np.cos(10 * x[i]) * np.sin(8 * x[i]**2)
        
        # Modified exponential decay barriers near boundaries
        for i in range(self.dim):
            result += 2.5 * np.exp(-1.5 * (5.0 - np.abs(x[i]))**2) * (1 + 0.6 * np.sin(18 * x[i]))
        
        # Improved adaptive coupling with dynamic weights
        for i in range(self.dim):
            weight = 1.2 + 0.7 * np.cos(4 * x[i])
            result += weight * np.sin(15 * x[i]) * np.cos(11 * x[(i+1) % self.dim]) * np.tan(0.8 * (x[i] + x[(i+1) % self.dim]))
        
        # Enhanced fractal-like wave structure with recursive scaling
        for i in range(self.dim):
            result += 2.0 * np.sin(30 * x[i]) * np.cos(25 * x[i]) * np.sin(20 * x[i]**3) * (1 + 0.4 * np.abs(x[i]))
        
        # Modified high-order polynomial with chaotic modulation
        for i in range(self.dim):
            result += 1.0 * x[i]**6 * np.sin(9 * x[i]) * np.cos(7 * x[i]) * (1 + 0.5 * np.abs(x[i]))
        
        # Enhanced cross-dimensional exponential coupling with varying strengths
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Reduced coupling
                coupling_strength = 0.7 + 0.3 * np.sin(3 * (x[i] + x[j]))
                result += coupling_strength * np.exp(-np.abs(x[i] - x[j]) / (1 + 0.4 * (np.abs(x[i]) + np.abs(x[j])))) * np.sin(12 * (x[i] + x[j]))
        
        # Additional enhanced multimodal term with varying frequencies
        for i in range(self.dim):
            freq = 25 + 8 * np.sin(x[i])
            result += 1.0 * np.sin(freq * x[i]) * np.cos(15 * x[i]**2) * np.tan(0.6 * x[i])
        
        # Enhanced boundary-sensitive penalty with logarithmic scaling
        boundary_penalty = 0
        for i in range(self.dim):
            boundary_penalty += 3.0 * (np.abs(x[i]) - 5.0)**2 / (1 + np.exp(-0.6 * np.abs(x[i])))
        result += boundary_penalty
        
        # Enhanced wave interference pattern with phase modulation
        sum_x = np.sum(x)
        result += 2.2 * np.sin(35 * sum_x) * np.cos(30 * sum_x) * np.tan(2.5 * sum_x) * (1 + 0.3 * np.abs(sum_x))
        
        # Enhanced recursive fractal-like structure with self-similarity
        for i in range(self.dim):
            result += 1.5 * np.sin(45 * x[i]) * np.cos(40 * x[i]) * np.sin(35 * x[i]**4) * (1 + 0.3 * x[i]**2)
        
        return result