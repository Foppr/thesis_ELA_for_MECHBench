import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with dynamic conditioning
        result = 0.2 * np.sum(x**2)
        
        # Trigonometric chaos with logistic map modulation
        for i in range(self.dim):
            freq = 2.0 + 1.0 * np.sin(i * np.pi / self.dim)
            amp = 1.5 + 0.5 * np.cos(i * np.pi / (self.dim + 1))
            chaos_factor = 0.3 + 0.7 * np.sin(5 * x[i] + i * np.pi / 4) * np.cos(3 * x[i] - i)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i]) * chaos_factor
        
        # Adaptive radial basis functions with dynamic centers and widths
        for i in range(min(8, self.dim)):
            center = 3.0 * np.sin(i * np.pi / (self.dim + 2)) * np.cos(i * np.pi / (self.dim + 3))
            width = 1.0 + 0.4 * np.sin(i * np.pi / (self.dim + 4))
            dist = np.sum((x - center)**2)
            result += 2.0 * np.exp(-dist / (2 * width**2)) * np.sin(3 * dist) * np.cos(2 * dist)
        
        # Cross-dimensional exponential coupling with interaction terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.exp(-0.5 * abs(x[i] - x[j])) * np.sin(x[i] * x[j])
                result += 0.8 * coupling * (1 + 0.2 * np.sin(i + j) * np.cos(i - j))
        
        # Asymmetric gradient field with varying steepness and chaotic modulation
        for i in range(self.dim):
            steepness = 1.5 + 0.5 * np.sin(i * np.pi / self.dim)
            result += steepness * (x[i]**3 - 3 * x[i]**2 + 2 * x[i] + 0.5 * np.sin(12 * x[i]))
        
        # Multi-scale periodic components with chaotic phase shifts
        for i in range(self.dim):
            scale = 1.5 + 1.0 * np.cos(i * np.pi / self.dim)
            result += 0.3 * np.sin(scale * x[i]) * np.cos(2 * scale * x[i]) * np.tan(scale * x[i])
        
        # Boundary penalty with chaotic scaling
        boundary_penalty = 0.0
        for i in range(self.dim):
            if abs(x[i]) > 4.7:
                penalty_scale = 10.0 + 3.0 * np.sin(i * np.pi / (self.dim + 1))
                boundary_penalty += penalty_scale * (abs(x[i]) - 4.7)**2
        result += boundary_penalty
        
        # Global scaling factor with chaotic modulation
        global_factor = 1.5 + 0.6 * np.sin(np.sum(x) * np.pi / self.dim)
        result *= global_factor
        
        return result