import numpy as np

class ChaoticCubicPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base cubic polynomial term
        result = np.sum(x**3)
        
        # Fractal-like chaotic sinusoidal modulations with power-law frequency scaling
        for i in range(self.dim):
            freq = 2.0 * (i + 1) ** 2.0 + 1.5 * np.sin(i * 0.8) * np.cos(i * 0.3)
            amp = 2.0 * (1 + 0.3 * np.sin(i * 0.4)) * (1 + 0.2 * np.cos(i * 0.6))
            result += amp * np.sin(freq * x[i]) * np.cos(0.7 * freq * x[i])
            
        # Exponentially decaying cross-dimensional coupling with fractal interaction
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                coupling = 1.2 * np.exp(-0.2 * (i + j)) * (1 + 0.4 * np.sin(i * j * 0.3) * np.cos(i * j * 0.7))
                result += coupling * x[i] ** 2 * x[j] ** 1.5 * np.cos(1.5 * x[i] + 0.5 * x[j])
                
        # Multi-scale fractal valleys with chaotic depth and position
        for i in range(self.dim):
            valley_depth = 3.0 + 0.8 * np.sin(i * 0.9) + 0.4 * np.cos(i * 0.5)
            valley_position = np.sin(i * 0.7) + 0.3 * np.cos(i * 0.4)
            result += valley_depth * np.exp(-0.3 * (x[i] - valley_position)**2)
            
        # Asymmetric cubic terms with fractal shifts and scaling
        for i in range(self.dim):
            shift = 0.8 * np.sin(i * 1.1) + 0.3 * np.cos(i * 0.5)
            scale = 1.2 + 0.2 * np.sin(i * 0.9)
            result += 0.9 * (x[i] - shift)**3 * scale * (1 + 0.15 * np.sin(i * 0.7))
            
        # High-frequency chaotic noise with fractal dimensionality
        noise = 0.3 * np.sum(np.sin(20 * x) * np.cos(12 * x)) * (1 + 0.2 * np.sum(np.sin(2 * x)))
        result += noise
        
        # Add a global fractal scaling factor that increases complexity with dimension
        result *= (1.0 + 0.1 * np.log(self.dim + 1))
        
        return result