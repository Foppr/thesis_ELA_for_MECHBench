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
            freq = 4.0 * (i + 1) ** 1.6 + np.sin(i * 0.6) * 3.5
            amp = 2.0 * (1 + 0.25 * np.cos(i * 0.35))
            result += amp * np.sin(freq * x[i]) * np.cos(0.8 * freq * x[i])
            
        # Cross-dimensional coupling with enhanced interaction strengths
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                coupling = 2.0 * np.exp(-0.25 * (i + j)) * (1 + 0.4 * np.sin(i * j * 0.35))
                result += coupling * x[i] ** 2 * x[j] * np.cos(3.5 * x[i] + x[j])
                
        # Multi-scale chaotic valleys with varied depth and position
        for i in range(self.dim):
            valley_depth = 3.0 + 0.6 * np.sin(i * 0.65) + 0.4 * np.cos(i * 0.45)
            valley_position = np.sin(i * 0.45) * 1.8
            result += valley_depth * np.exp(-0.8 * (x[i] - valley_position)**2)
            
        # Asymmetric cubic terms with increased chaos
        for i in range(self.dim):
            shift = 0.8 * np.sin(i * 0.95) + 0.25 * np.cos(i * 0.35)
            result += 1.2 * (x[i] - shift)**3 * (1 + 0.2 * np.sin(i * 0.65))
            
        # High-frequency chaotic noise component with modified parameters
        noise = 0.5 * np.sum(np.sin(25 * x) * np.cos(12 * x)) * (1 + 0.2 * np.sum(np.sin(x)))
        result += noise
        
        # Additional harmonic modulation to increase condition number
        for i in range(self.dim):
            result += 0.4 * np.sin(6 * x[i]) * np.cos(3 * x[i]) * (1 + 0.15 * np.sin(i))
            
        # Novel exponential valley structures with enhanced complexity
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                valley_depth = 1.8 + 0.3 * np.sin(i * 0.7) * np.cos(j * 0.5)
                valley_position = 0.5 * (np.sin(i * 0.5) + np.cos(j * 0.4))
                result += valley_depth * np.exp(-1.2 * (x[i] - valley_position)**2) * np.exp(-0.5 * (x[j] - valley_position)**2)
                
        # Increased coupling between distant dimensions
        for i in range(self.dim):
            for j in range(max(0, i-3), i):
                coupling = 1.2 * np.exp(-0.3 * abs(i - j)) * (1 + 0.25 * np.sin(i * j * 0.4))
                result += coupling * x[i] ** 1.5 * x[j] ** 1.5 * np.cos(2.0 * x[i] + 1.5 * x[j])
                
        # Additional chaotic interference terms
        for i in range(self.dim):
            result += 0.25 * np.sin(8 * x[i]) * np.cos(4 * x[i]) * (1 + 0.1 * np.cos(i * 0.8))
            
        return result