import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with dynamic conditioning
        result = np.sum(x**2) * 0.3
        
        # Chaotic sine-cosine components with logistic map modulation
        for i in range(self.dim):
            freq = 3.0 + 1.5 * np.sin(2 * i * np.pi / self.dim)
            amp = 2.0 + 0.8 * np.cos(i * np.pi / self.dim)
            chaos_factor = 0.5 + 0.5 * np.sin(10 * x[i] + i) * np.cos(7 * x[i] - i)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i]) * chaos_factor
        
        # Dynamic radial basis functions with time-varying centers and widths
        for i in range(min(10, self.dim)):
            center = 4.0 * np.sin(i * np.pi / self.dim) * np.cos(i * np.pi / (self.dim + 1))
            width = 1.2 + 0.3 * np.sin(i * np.pi / (self.dim + 2))
            dist = np.sum((x - center)**2)
            result += 1.5 * np.exp(-dist / (2 * width**2)) * np.cos(4 * dist) * np.sin(2 * dist)
        
        # Cross-dimensional coupling with exponential decay and interaction terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(x[i] * x[j]) * np.exp(-0.1 * abs(x[i] - x[j]))
                result += 0.5 * coupling * (1 + 0.3 * np.sin(i + j) * np.cos(i - j))
        
        # Asymmetric gradient field with varying steepness and chaotic modulation
        for i in range(self.dim):
            steepness = 1.0 + 0.5 * np.sin(i * np.pi / self.dim)
            result += steepness * (x[i]**4 - 2 * x[i]**2 + 0.5 * np.sin(15 * x[i]))
        
        # Multi-scale periodic components with chaotic phase shifts
        for i in range(self.dim):
            scale = 2.0 + 1.5 * np.cos(i * np.pi / self.dim)
            result += 0.2 * np.sin(scale * x[i]) * np.cos(3 * scale * x[i]) * np.tan(2 * scale * x[i])
        
        # Boundary penalty with chaotic scaling
        boundary_penalty = 0.0
        for i in range(self.dim):
            if abs(x[i]) > 4.8:
                penalty_scale = 15.0 + 5.0 * np.sin(i * np.pi / self.dim)
                boundary_penalty += penalty_scale * (abs(x[i]) - 4.8)**3
        result += boundary_penalty
        
        # Global scaling factor with chaotic modulation
        global_factor = 2.0 + 0.8 * np.sin(np.sum(x) * np.pi / self.dim)
        result *= global_factor
        
        return result