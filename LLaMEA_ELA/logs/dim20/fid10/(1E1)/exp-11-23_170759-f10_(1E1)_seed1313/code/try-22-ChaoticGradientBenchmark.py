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
        
        # Add exponentially decaying sinusoidal waves with modified decay rates
        for i in range(min(self.dim, 5)):
            freq = 2.5 ** (i + 1)  # Increased frequency growth
            amp = 1.0 / (1.0 + 0.3 * i)
            result += amp * np.sin(freq * x[i]) * np.exp(-0.15 * abs(x[i]))  # Increased decay
        
        # Add cubic valley structure with altered coefficients
        if self.dim >= 2:
            result += 0.4 * ((x[0] - 1.2)**3 + (x[1] + 0.8)**3)  # Slight shift and scaling
            
        # Add chaotic gradient components with varying scales
        for i in range(min(self.dim, 4)):
            scale = 2.5 ** (i + 1)  # Increased scale growth
            result += 0.25 * np.sin(scale * x[i]) * np.cos(scale * x[i]) * (1.0 + 0.15 * x[i]**2)
        
        # Add multi-scale harmonic modulation
        for i in range(self.dim):
            if i % 2 == 0:
                result += 0.2 * np.sin(3.5 * x[i] + 0.6 * i) * np.cos(7.5 * x[i] - 0.35 * i)
            else:
                result += 0.2 * np.cos(5.5 * x[i] - 0.45 * i) * np.sin(2.5 * x[i] + 0.65 * i)
        
        # Add adaptive conditioning based on coordinate values
        for i in range(self.dim):
            result += 0.12 * (x[i] ** 4) * (1.0 + 0.06 * np.abs(x[i]))
            
        # Add a "spiral" valley structure with modified parameters
        if self.dim >= 2:
            spiral_term = 0.25 * np.exp(-0.15 * (x[0]**2 + x[1]**2)) * np.sin(6.0 * np.arctan2(x[1], x[0]))
            result += spiral_term
            
        # Add a "rugged" component with multiple local minima
        for i in range(min(self.dim, 3)):
            result += 0.3 * np.abs(x[i]) * (1.0 + 0.35 * np.sin(12.0 * x[i]))  # Increased frequency
            
        # Add a global modulation based on the sum of coordinates
        sum_x = np.sum(x)
        result += 0.12 * np.sin(0.6 * sum_x) * np.cos(0.35 * sum_x)
        
        # Add asymmetric exponential decay terms with modified parameters
        for i in range(min(self.dim, 4)):
            if x[i] > 0:
                result += 0.12 * np.exp(-0.6 * x[i]) * (1.0 + 0.25 * i)  # Increased decay rate
            else:
                result += 0.12 * np.exp(-0.35 * abs(x[i])) * (1.0 + 0.15 * i)  # Increased decay rate
        
        return result