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
            freq = 4 * (i + 1) ** 1.3 + np.sin(i * 0.6) * 2.5
            amp = 2.0 * (1 + 0.15 * np.cos(i * 0.4))
            result += amp * np.sin(freq * x[i]) * np.cos(0.6 * freq * x[i])
            
        # Cross-dimensional coupling with modified interaction strengths
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                coupling = 1.2 * np.exp(-0.15 * (i + j)) * (1 + 0.2 * np.sin(i * j * 0.4))
                result += coupling * x[i] ** 2 * x[j] * np.cos(2.5 * x[i] + x[j])
                
        # Multi-scale chaotic valleys with irregular depth
        for i in range(self.dim):
            valley_depth = 3.0 + 0.4 * np.sin(i * 0.7) + 0.2 * np.cos(i * 0.5)
            result += valley_depth * np.exp(-0.6 * (x[i] - np.sin(i * 0.3))**2)
            
        # Asymmetric cubic terms with chaotic shifts
        for i in range(self.dim):
            shift = 0.6 * np.sin(i * 0.8) + 0.15 * np.cos(i * 0.2)
            result += 0.8 * (x[i] - shift)**3 * (1 + 0.12 * np.sin(i * 0.5))
            
        # High-frequency chaotic noise component
        noise = 0.3 * np.sum(np.sin(18 * x) * np.cos(9 * x)) * (1 + 0.12 * np.sum(np.sin(x)))
        result += noise
        
        return result