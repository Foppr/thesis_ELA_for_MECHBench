import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with dynamic conditioning
        result = 0.1 * np.sum(x**2)
        
        # Enhanced trigonometric chaos with logistic map modulation
        for i in range(self.dim):
            freq = 2.0 + 1.0 * np.sin(i * np.pi / self.dim)
            amp = 1.2 + 0.6 * np.cos(i * np.pi / (self.dim + 1))  # Slightly reduced amplitude
            chaos_factor = 0.3 + 0.7 * np.sin(6 * x[i] + i * np.pi / 4) * np.cos(3 * x[i] - i)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i]) * chaos_factor
        
        # Modified radial basis functions with dynamic centers and widths
        for i in range(min(6, self.dim)):
            center = 2.0 * np.sin(i * np.pi / (self.dim + 4)) * np.cos(i * np.pi / (self.dim + 3))
            width = 1.0 + 0.4 * np.sin(i * np.pi / (self.dim + 6))
            dist = np.sum((x - center)**2)
            result += 3.0 * np.exp(-dist / (2 * width**2)) * np.sin(3 * dist) * np.cos(2 * dist)
        
        # Cross-dimensional exponential coupling with modified interaction terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.exp(-0.5 * abs(x[i] - x[j])) * np.sin(2.0 * x[i] * x[j])  # Increased coupling strength
                result += 2.0 * coupling * (1 + 0.2 * np.sin(i + j) * np.cos(i - j))  # Slightly increased weight
        
        # Asymmetric gradient field with varying steepness and chaotic modulation
        for i in range(self.dim):
            steepness = 2.0 + 0.3 * np.sin(i * np.pi / self.dim)
            result += steepness * (x[i]**3 - 2.0 * x[i]**2 + 1.5 * x[i] + 0.5 * np.sin(8 * x[i]))
        
        # Multi-scale periodic components with chaotic phase shifts
        for i in range(self.dim):
            scale = 2.0 + 0.8 * np.cos(i * np.pi / self.dim)
            result += 0.5 * np.sin(scale * x[i]) * np.cos(3.0 * scale * x[i]) * np.tan(2.0 * scale * x[i])
        
        # Boundary penalty with modified scaling
        boundary_penalty = 0.0
        for i in range(self.dim):
            if abs(x[i]) > 4.5:
                penalty_scale = 12.0 + 2.0 * np.sin(i * np.pi / (self.dim + 3))  # Increased penalty scale
                boundary_penalty += penalty_scale * (abs(x[i]) - 4.5)**2
        result += boundary_penalty
        
        # Global scaling factor with chaotic modulation
        global_factor = 2.0 + 0.4 * np.sin(np.sum(x) * np.pi / self.dim)
        result *= global_factor
        
        return result