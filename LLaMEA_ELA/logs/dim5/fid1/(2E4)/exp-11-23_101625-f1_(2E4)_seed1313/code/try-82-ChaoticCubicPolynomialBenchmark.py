import numpy as np

class ChaoticCubicPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base cubic polynomial term with modified coefficient
        result = 1.5 * np.sum(x**3)
        
        # Chaotic sinusoidal modulations with altered frequencies and amplitudes
        for i in range(self.dim):
            freq = 5.0 * (i + 1) ** 1.4 + np.sin(i * 0.7) * 3.0
            amp = 2.5 * (1 + 0.3 * np.cos(i * 0.4))
            result += amp * np.sin(freq * x[i]) * np.cos(0.9 * freq * x[i])
            
        # Cross-dimensional coupling with enhanced interaction strengths
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                coupling = 2.2 * np.exp(-0.3 * (i + j)) * (1 + 0.4 * np.sin(i * j * 0.4))
                result += coupling * x[i] ** 2 * x[j] * np.cos(4.0 * x[i] + x[j])
                
        # Multi-scale chaotic valleys with varied depth and position
        for i in range(self.dim):
            valley_depth = 3.2 + 0.7 * np.sin(i * 0.7) + 0.4 * np.cos(i * 0.5)
            valley_position = np.sin(i * 0.5) * 2.0
            result += valley_depth * np.exp(-0.8 * (x[i] - valley_position)**2)
            
        # Asymmetric cubic terms with increased chaos
        for i in range(self.dim):
            shift = 1.0 * np.sin(i * 1.0) + 0.3 * np.cos(i * 0.4)
            result += 1.3 * (x[i] - shift)**3 * (1 + 0.25 * np.sin(i * 0.7))
            
        # High-frequency chaotic noise component with modified parameters
        noise = 0.6 * np.sum(np.sin(25 * x) * np.cos(13 * x)) * (1 + 0.2 * np.sum(np.sin(x)))
        result += noise
        
        # Additional harmonic modulation to increase condition number
        for i in range(self.dim):
            result += 0.4 * np.sin(6.0 * x[i]) * np.cos(3.0 * x[i]) * (1 + 0.15 * np.sin(i))
            
        # Novel chaotic valley structure with fractal-like characteristics
        for i in range(self.dim):
            for j in range(i+1, min(i+2, self.dim)):
                fractal_term = 0.8 * np.sin(7.0 * x[i] + 3.0 * x[j]) * np.cos(4.5 * x[i] - 2.0 * x[j])
                result += fractal_term * (1 + 0.1 * np.sin(i * j))
                
        # Multi-scale harmonic interference with varying phase shifts
        for i in range(self.dim):
            result += 0.3 * np.sum(np.sin((i+1) * 8.0 * x[i] + 2.0 * np.sin(i))) * (1 + 0.05 * np.cos(i))
            
        return result