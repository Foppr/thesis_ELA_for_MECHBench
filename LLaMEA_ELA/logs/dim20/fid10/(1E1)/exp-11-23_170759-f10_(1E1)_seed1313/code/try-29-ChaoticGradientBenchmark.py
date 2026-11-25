import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Scale input to [-5, 5] domain if needed
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Base quadratic term with enhanced conditioning
        for i in range(self.dim):
            result += 0.15 * (x[i] ** 2) * (1.0 + 0.2 * i)
        
        # Add exponentially decaying sinusoidal waves with increased frequency diversity
        for i in range(min(self.dim, 6)):
            freq = 4.0 ** (i + 1)  # Increased frequency base
            amp = 1.5 / (1.0 + 0.5 * i)  # Modified amplitude decay
            result += amp * np.sin(freq * x[i]) * np.exp(-0.3 * abs(x[i]))
        
        # Add cubic valley structure with enhanced complexity
        if self.dim >= 2:
            result += 0.7 * ((x[0] - 1.0)**3 + (x[1] + 2.0)**3)  # Shifted and scaled
            
        # Add chaotic gradient components with increased scale diversity
        for i in range(min(self.dim, 5)):
            scale = 4.0 ** (i + 1)  # Increased scale factor
            result += 0.35 * np.sin(scale * x[i]) * np.cos(scale * x[i]) * (1.0 + 0.25 * x[i]**2)
        
        # Add multi-scale harmonic modulation with enhanced parameter diversity
        for i in range(self.dim):
            if i % 2 == 0:
                result += 0.3 * np.sin(5.0 * x[i] + 0.8 * i) * np.cos(9.0 * x[i] - 0.6 * i)
            else:
                result += 0.3 * np.cos(7.0 * x[i] - 0.7 * i) * np.sin(4.0 * x[i] + 0.9 * i)
        
        # Add adaptive conditioning based on coordinate values with enhanced complexity
        for i in range(self.dim):
            result += 0.25 * (x[i] ** 4) * (1.0 + 0.2 * np.abs(x[i]))
            
        # Add a "spiral" valley structure with modified parameters and increased complexity
        if self.dim >= 2:
            spiral_term = 0.4 * np.exp(-0.25 * (x[0]**2 + x[1]**2)) * np.sin(10.0 * np.arctan2(x[1], x[0]))
            result += spiral_term
            
        # Add a "rugged" component with increased local minima density
        for i in range(min(self.dim, 4)):
            result += 0.4 * np.abs(x[i]) * (1.0 + 0.6 * np.sin(16.0 * x[i]))
            
        # Add a global modulation based on the sum of coordinates with enhanced parameters
        sum_x = np.sum(x)
        result += 0.25 * np.sin(0.8 * sum_x) * np.cos(0.6 * sum_x)
        
        # Add asymmetric exponential decay terms with modified coefficients and increased diversity
        for i in range(min(self.dim, 5)):
            if x[i] > 0:
                result += 0.2 * np.exp(-0.8 * x[i]) * (1.0 + 0.4 * i)
            else:
                result += 0.18 * np.exp(-0.6 * abs(x[i])) * (1.0 + 0.3 * i)
        
        # Add a novel cross-term interaction to increase conditioning
        if self.dim >= 3:
            for i in range(2):
                for j in range(i+1, min(self.dim, 3)):
                    result += 0.15 * np.sin(2.0 * x[i]) * np.cos(2.0 * x[j]) * (1.0 + 0.1 * abs(x[i] - x[j]))
        
        # Add a novel "wavelet-like" component for enhanced multimodality
        for i in range(self.dim):
            result += 0.12 * np.sin(12.0 * x[i]) * np.cos(18.0 * x[i]) * np.exp(-0.1 * abs(x[i]))
        
        return result