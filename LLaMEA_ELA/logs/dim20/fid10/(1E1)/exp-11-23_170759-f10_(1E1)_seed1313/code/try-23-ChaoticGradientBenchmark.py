import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Scale input to [-5, 5] domain if needed
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Base quadratic term with adaptive conditioning
        for i in range(self.dim):
            result += 0.1 * (x[i] ** 2) * (1.0 + 0.1 * i)
        
        # Add exponentially decaying sinusoidal waves
        for i in range(min(self.dim, 5)):
            freq = 2.0 ** (i + 1)
            amp = 1.0 / (1.0 + 0.2 * i)
            result += amp * np.sin(freq * x[i]) * np.exp(-0.1 * abs(x[i]))
        
        # Add cubic valley structure
        if self.dim >= 2:
            result += 0.3 * ((x[0] - 1.0)**3 + (x[1] + 1.0)**3)
            
        # Add chaotic gradient components with varying scales
        for i in range(min(self.dim, 4)):
            scale = 2.0 ** (i + 1)
            result += 0.2 * np.sin(scale * x[i]) * np.cos(scale * x[i]) * (1.0 + 0.1 * x[i]**2)
        
        # Add multi-scale harmonic modulation
        for i in range(self.dim):
            if i % 2 == 0:
                result += 0.15 * np.sin(3.0 * x[i] + 0.5 * i) * np.cos(7.0 * x[i] - 0.3 * i)
            else:
                result += 0.15 * np.cos(5.0 * x[i] - 0.4 * i) * np.sin(2.0 * x[i] + 0.6 * i)
        
        # Add adaptive conditioning based on coordinate values
        for i in range(self.dim):
            result += 0.1 * (x[i] ** 4) * (1.0 + 0.05 * np.abs(x[i]))
            
        # Add a "spiral" valley structure
        if self.dim >= 2:
            spiral_term = 0.2 * np.exp(-0.1 * (x[0]**2 + x[1]**2)) * np.sin(5.0 * np.arctan2(x[1], x[0]))
            result += spiral_term
            
        # Add a "rugged" component with multiple local minima
        for i in range(min(self.dim, 3)):
            result += 0.25 * np.abs(x[i]) * (1.0 + 0.3 * np.sin(10.0 * x[i]))
            
        # Add a global modulation based on the sum of coordinates
        sum_x = np.sum(x)
        result += 0.1 * np.sin(0.5 * sum_x) * np.cos(0.3 * sum_x)
        
        # Add asymmetric exponential decay terms
        for i in range(min(self.dim, 4)):
            if x[i] > 0:
                result += 0.1 * np.exp(-0.5 * x[i]) * (1.0 + 0.2 * i)
            else:
                result += 0.1 * np.exp(-0.3 * abs(x[i])) * (1.0 + 0.1 * i)
        
        return result