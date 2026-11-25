import numpy as np

class ChaoticCubicPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base cubic polynomial term
        result = np.sum(x**3)
        
        # Chaotic sinusoidal modulations with varying frequencies and amplitudes
        for i in range(self.dim):
            freq = 3 * (i + 1) ** 1.5 + np.sin(i * 0.7) * 2.0
            amp = 1.5 * (1 + 0.2 * np.cos(i * 0.5))
            result += amp * np.sin(freq * x[i]) * np.cos(0.5 * freq * x[i])
            
        # Cross-dimensional coupling with chaotic interaction strengths
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                coupling = 0.8 * np.exp(-0.1 * (i + j)) * (1 + 0.3 * np.sin(i * j * 0.5))
                result += coupling * x[i] ** 2 * x[j] * np.cos(2 * x[i] + x[j])
                
        # Multi-scale chaotic valleys with irregular depth
        for i in range(self.dim):
            valley_depth = 2.0 + 0.5 * np.sin(i * 0.8) + 0.3 * np.cos(i * 0.6)
            result += valley_depth * np.exp(-0.5 * (x[i] - np.sin(i * 0.4))**2)
            
        # Asymmetric cubic terms with chaotic shifts
        for i in range(self.dim):
            shift = 0.5 * np.sin(i * 0.9) + 0.2 * np.cos(i * 0.3)
            result += 0.7 * (x[i] - shift)**3 * (1 + 0.1 * np.sin(i * 0.6))
            
        # High-frequency chaotic noise component
        noise = 0.25 * np.sum(np.sin(15 * x) * np.cos(8 * x)) * (1 + 0.1 * np.sum(np.sin(x)))
        result += noise
        
        return result