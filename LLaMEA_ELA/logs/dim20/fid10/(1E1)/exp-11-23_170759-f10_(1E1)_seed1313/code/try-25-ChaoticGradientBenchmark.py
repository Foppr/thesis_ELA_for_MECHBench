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
        
        # Add exponentially decaying sinusoidal waves with modified frequencies
        for i in range(min(self.dim, 5)):
            freq = 3.0 ** (i + 1)  # Increased frequency base
            amp = 1.0 / (1.0 + 0.3 * i)
            result += amp * np.sin(freq * x[i]) * np.exp(-0.15 * abs(x[i]))
        
        # Add modified cubic valley structure with different coefficients
        if self.dim >= 2:
            result += 0.5 * ((x[0] - 1.5)**3 + (x[1] + 1.5)**3)  # Shifted and scaled
            
        # Add chaotic gradient components with varying scales
        for i in range(min(self.dim, 4)):
            scale = 3.0 ** (i + 1)  # Increased scale factor
            result += 0.25 * np.sin(scale * x[i]) * np.cos(scale * x[i]) * (1.0 + 0.15 * x[i]**2)
        
        # Add multi-scale harmonic modulation with altered parameters
        for i in range(self.dim):
            if i % 2 == 0:
                result += 0.2 * np.sin(4.0 * x[i] + 0.6 * i) * np.cos(8.0 * x[i] - 0.4 * i)
            else:
                result += 0.2 * np.cos(6.0 * x[i] - 0.5 * i) * np.sin(3.0 * x[i] + 0.7 * i)
        
        # Add adaptive conditioning based on coordinate values with increased complexity
        for i in range(self.dim):
            result += 0.15 * (x[i] ** 4) * (1.0 + 0.1 * np.abs(x[i]))
            
        # Add a "spiral" valley structure with modified parameters
        if self.dim >= 2:
            spiral_term = 0.3 * np.exp(-0.15 * (x[0]**2 + x[1]**2)) * np.sin(7.0 * np.arctan2(x[1], x[0]))
            result += spiral_term
            
        # Add a "rugged" component with multiple local minima
        for i in range(min(self.dim, 3)):
            result += 0.3 * np.abs(x[i]) * (1.0 + 0.4 * np.sin(12.0 * x[i]))
            
        # Add a global modulation based on the sum of coordinates with different parameters
        sum_x = np.sum(x)
        result += 0.15 * np.sin(0.6 * sum_x) * np.cos(0.4 * sum_x)
        
        # Add asymmetric exponential decay terms with modified coefficients
        for i in range(min(self.dim, 4)):
            if x[i] > 0:
                result += 0.15 * np.exp(-0.6 * x[i]) * (1.0 + 0.3 * i)
            else:
                result += 0.12 * np.exp(-0.4 * abs(x[i])) * (1.0 + 0.2 * i)
        
        return result