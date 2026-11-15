import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for fractal-like behavior
        self.fractal_consts = np.array([np.sqrt(i + 1) for i in range(dim)])
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic with asymmetric scaling
        result = 0.0
        for i in range(self.dim):
            if x[i] >= 0:
                result += 0.5 * (x[i] - 1.0)**2 + 0.1 * x[i]**4
            else:
                result += 0.7 * (x[i] + 1.0)**2 + 0.15 * x[i]**6
        
        # Nested sinusoidal modulation with varying frequencies
        for i in range(self.dim):
            freq = 2.0 + 0.5 * np.sin(x[i])
            result += 0.3 * np.sin(freq * x[i]) * np.cos(1.5 * x[i]) + 0.2 * np.sin(3.0 * x[i])
        
        # Asymmetric interaction terms with fractal-like scaling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                scale = self.fractal_consts[i] * self.fractal_consts[j]
                result += scale * (np.exp(0.1 * (x[i] - x[j])**2) - 1.0)
        
        # Fractal-like curvature with exponential scaling
        fractal_curvature = 0.0
        for i in range(self.dim):
            fractal_curvature += np.exp(0.2 * np.abs(x[i])) * np.sin(5.0 * x[i])
        result += 0.1 * fractal_curvature
        
        # Chaotic noise component with varying amplitude
        chaotic_noise = 0.0
        for i in range(self.dim):
            chaotic_noise += 0.05 * np.sin(10.0 * x[i] + np.cos(7.0 * x[i]))
        result += chaotic_noise
        
        # Shifted global minimum with additional polynomial offset
        shift = 0.2
        result += 0.01 * np.sum((x - shift)**2) + 0.005 * np.sum((x - shift)**4)
        
        return result