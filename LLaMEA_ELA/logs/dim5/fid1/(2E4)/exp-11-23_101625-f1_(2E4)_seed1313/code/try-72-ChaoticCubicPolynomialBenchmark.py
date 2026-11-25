import numpy as np

class ChaoticCubicPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base cubic polynomial term with modified coefficient
        result = 1.2 * np.sum(x**3)
        
        # Chaotic sinusoidal modulations with altered frequencies and amplitudes
        for i in range(self.dim):
            freq = 3.5 * (i + 1) ** 1.4 + np.sin(i * 0.5) * 3.0
            amp = 1.8 * (1 + 0.2 * np.cos(i * 0.3))
            result += amp * np.sin(freq * x[i]) * np.cos(0.7 * freq * x[i])
            
        # Cross-dimensional coupling with enhanced interaction strengths
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                coupling = 1.5 * np.exp(-0.2 * (i + j)) * (1 + 0.3 * np.sin(i * j * 0.3))
                result += coupling * x[i] ** 2 * x[j] * np.cos(3.0 * x[i] + x[j])
                
        # Multi-scale chaotic valleys with varied depth and position
        for i in range(self.dim):
            valley_depth = 2.5 + 0.5 * np.sin(i * 0.6) + 0.3 * np.cos(i * 0.4)
            valley_position = np.sin(i * 0.4) * 1.5
            result += valley_depth * np.exp(-0.7 * (x[i] - valley_position)**2)
            
        # Asymmetric cubic terms with increased chaos
        for i in range(self.dim):
            shift = 0.7 * np.sin(i * 0.9) + 0.2 * np.cos(i * 0.3)
            result += 1.0 * (x[i] - shift)**3 * (1 + 0.15 * np.sin(i * 0.6))
            
        # High-frequency chaotic noise component with modified parameters
        noise = 0.4 * np.sum(np.sin(20 * x) * np.cos(10 * x)) * (1 + 0.15 * np.sum(np.sin(x)))
        result += noise
        
        # Additional harmonic modulation to increase condition number
        for i in range(self.dim):
            result += 0.3 * np.sin(5 * x[i]) * np.cos(2.5 * x[i]) * (1 + 0.1 * np.sin(i))
            
        return result