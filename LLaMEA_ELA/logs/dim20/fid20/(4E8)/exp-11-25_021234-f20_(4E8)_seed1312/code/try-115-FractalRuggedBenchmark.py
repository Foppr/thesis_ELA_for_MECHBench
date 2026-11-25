import numpy as np

class FractalRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for global attraction
        f1 = 0.1 * np.sum(x**2)
        
        # Recursive sine modulation creating fractal-like structure
        f2 = 0.0
        for i in range(self.dim):
            level = 1
            temp_x = x[i]
            for _ in range(5):  # 5 levels of recursion
                temp_x = np.sin(temp_x * (2**level))
                level += 1
            f2 += temp_x ** 2
        
        # Adaptive penalty landscape based on distance from center
        f3 = 0.0
        center_dist = np.sqrt(np.sum(x**2))
        for i in range(self.dim):
            penalty = 10.0 * (1.0 + np.sin(5.0 * x[i]) * np.cos(3.0 * x[i]))
            f3 += penalty * np.exp(-0.1 * (x[i] - center_dist)**2)
        
        # Multi-scale chaotic oscillations
        f4 = 0.0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.5 * np.sin(0.2 * i * np.sum(x))
            freq = 2.0 + 1.5 * np.cos(0.3 * i)
            f4 += scale_factor * np.sin(freq * x[i]) * np.exp(-0.05 * x[i]**2)
        
        # Discontinuous regions with step functions
        f5 = 0.0
        for i in range(self.dim):
            step = np.floor(3.0 * np.sin(x[i]))
            f5 += step * np.exp(-0.2 * x[i]**2)
        
        # Logarithmic barrier effects near boundaries
        f6 = 0.0
        for i in range(self.dim):
            barrier = np.log(1.0 + np.abs(x[i]) / 5.0)
            f6 += barrier * np.sin(2.0 * x[i])
        
        # Saddle point interactions with varying coupling strengths
        f7 = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                if j < self.dim:
                    strength = 0.5 + 0.3 * np.sin(0.1 * (i + j))
                    f7 += strength * np.sin(x[i]) * np.cos(x[j])
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7