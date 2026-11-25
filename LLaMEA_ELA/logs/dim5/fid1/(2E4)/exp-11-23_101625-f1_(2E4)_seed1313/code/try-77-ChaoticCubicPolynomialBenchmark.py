import numpy as np

class ChaoticCubicPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base cubic polynomial term with modified coefficient
        result = 1.3 * np.sum(x**3)
        
        # Chaotic sinusoidal modulations with altered frequencies and amplitudes
        for i in range(self.dim):
            freq = 4.0 * (i + 1) ** 1.3 + np.sin(i * 0.6) * 2.5
            amp = 2.0 * (1 + 0.25 * np.cos(i * 0.35))
            result += amp * np.sin(freq * x[i]) * np.cos(0.8 * freq * x[i])
            
        # Cross-dimensional coupling with enhanced interaction strengths
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                coupling = 1.8 * np.exp(-0.25 * (i + j)) * (1 + 0.35 * np.sin(i * j * 0.35))
                result += coupling * x[i] ** 2 * x[j] * np.cos(3.5 * x[i] + x[j])
                
        # Multi-scale chaotic valleys with varied depth and position
        for i in range(self.dim):
            valley_depth = 2.8 + 0.6 * np.sin(i * 0.65) + 0.35 * np.cos(i * 0.45)
            valley_position = np.sin(i * 0.45) * 1.6
            result += valley_depth * np.exp(-0.75 * (x[i] - valley_position)**2)
            
        # Asymmetric cubic terms with increased chaos
        for i in range(self.dim):
            shift = 0.8 * np.sin(i * 0.95) + 0.25 * np.cos(i * 0.35)
            result += 1.1 * (x[i] - shift)**3 * (1 + 0.2 * np.sin(i * 0.65))
            
        # High-frequency chaotic noise component with modified parameters
        noise = 0.45 * np.sum(np.sin(22 * x) * np.cos(11 * x)) * (1 + 0.18 * np.sum(np.sin(x)))
        result += noise
        
        # Additional harmonic modulation to increase condition number
        for i in range(self.dim):
            result += 0.35 * np.sin(5.5 * x[i]) * np.cos(2.7 * x[i]) * (1 + 0.12 * np.sin(i))
            
        return result