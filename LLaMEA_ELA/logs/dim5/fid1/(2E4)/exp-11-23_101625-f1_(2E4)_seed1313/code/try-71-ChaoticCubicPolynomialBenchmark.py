import numpy as np

class ChaoticCubicPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base cubic polynomial term with adaptive scaling
        result = np.sum(x**3 * (1 + 0.1 * np.sin(np.arange(self.dim) * 0.5)))
        
        # Enhanced chaotic sinusoidal modulations with dynamic frequencies and amplitudes
        for i in range(self.dim):
            freq = 5.0 * (i + 1) ** 1.4 + np.sin(i * 0.7) * 3.0
            amp = 2.5 * (1 + 0.2 * np.cos(i * 0.5))
            result += amp * np.sin(freq * x[i]) * np.cos(0.7 * freq * x[i])
            
        # Increased cross-dimensional coupling with stronger interaction strengths
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                coupling = 2.0 * np.exp(-0.2 * (i + j)) * (1 + 0.3 * np.sin(i * j * 0.5))
                result += coupling * x[i] ** 2 * x[j] * np.cos(3.0 * x[i] + x[j])
                
        # Enhanced multi-scale chaotic valleys with variable depths and positions
        for i in range(self.dim):
            valley_depth = 4.0 + 0.5 * np.sin(i * 0.8) + 0.3 * np.cos(i * 0.6)
            position_shift = 0.8 * np.sin(i * 0.4)
            result += valley_depth * np.exp(-0.7 * (x[i] - position_shift)**2)
            
        # Modified asymmetric cubic terms with stronger chaotic shifts
        for i in range(self.dim):
            shift = 0.8 * np.sin(i * 0.9) + 0.2 * np.cos(i * 0.3)
            result += 1.2 * (x[i] - shift)**3 * (1 + 0.15 * np.sin(i * 0.6))
            
        # Additional high-frequency chaotic noise with increased complexity
        noise = 0.4 * np.sum(np.sin(20 * x) * np.cos(10 * x)) * (1 + 0.15 * np.sum(np.sin(x)))
        result += noise
        
        # Add a global conditioning factor to increase the condition number
        condition_factor = 1.0 + 0.3 * np.sum(np.abs(x)**1.5)
        result *= condition_factor
        
        return result