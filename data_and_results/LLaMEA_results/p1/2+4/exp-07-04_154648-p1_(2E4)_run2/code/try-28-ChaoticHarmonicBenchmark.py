import numpy as np

class ChaoticHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute logistic map for dynamic shifts
        self.logistic_r = 3.95
        self.logistic_x = 0.5
        self.shifts = np.array([self._next_logistic() for _ in range(dim)])
    
    def _next_logistic(self):
        self.logistic_x = self.logistic_r * self.logistic_x * (1 - self.logistic_x)
        return self.logistic_x
    
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Spherical harmonics component with chaotic shifts
        harmonic = 0.0
        for i in range(self.dim):
            shift = self.shifts[i]
            harmonic += (x_norm[i] - shift)**2 * np.sin(10 * np.pi * x_norm[i])
        
        # Gaussian ridges with varying widths and heights
        gaussian = 0.0
        for i in range(self.dim):
            ridge_width = 0.1 + 0.4 * np.sin(i * 0.5)
            ridge_height = 0.5 + 0.5 * np.cos(i * 0.3)
            gaussian += ridge_height * np.exp(-0.5 * ((x_norm[i] - 0.3)**2) / (ridge_width**2))
        
        # Logistic map driven chaotic modulation
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(20 * np.pi * x_norm[i]) * np.cos(15 * np.pi * x_norm[i])
        
        # Fractal-like polynomial with exponentially increasing powers
        fractal = 0.0
        for i in range(self.dim):
            power = 2 + int(i * 0.7) % 5
            fractal += 0.1 * np.abs(x_norm[i])**power
        
        # Combine all components with dynamic weights
        total = 0.5 * np.sum(x_norm**2) + 0.3 * harmonic + 0.2 * gaussian + 0.4 * chaotic + 0.1 * fractal
        
        # Add a small random perturbation for additional complexity
        total += 0.01 * np.random.random()
        
        return total