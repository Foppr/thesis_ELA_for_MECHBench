import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = 0.5 * np.sum(x**2)
        
        # Fractal-like multimodal components with self-similarity and chaotic coupling
        for i in range(self.dim):
            freq = 3 ** (i % 5 + 1)
            result += 0.4 * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.3) * np.log(1 + abs(x[i]))
            
        # Nested fractal valleys with adaptive depths and chaotic scaling
        for i in range(self.dim):
            val = x[i]**2 + 0.05 * np.sin(100 * x[i])
            result += 0.5 * np.sin(15 * np.log(val)) * np.cos(7 * np.log(val)) * np.exp(-0.05 * abs(x[i]))
            
        # Multi-scale ridge patterns with dynamic spacing and chaotic modulation
        for i in range(self.dim):
            ridge_scale = 3 ** (i % 4 + 1)
            result += 0.3 * np.sin(ridge_scale * x[i]) * np.cos(ridge_scale * x[i] * 0.8) * np.exp(-0.15 * abs(x[i])) * np.sin(5 * x[i])
            
        # Interference terms between dimensions with dynamic coupling and chaotic interaction
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                coupling = 0.2 * (i + j + 1) ** -1.2 * np.sin(5 * i * j)
                result += coupling * np.sin(3**i * x[i]) * np.cos(3**j * x[j]) * np.log(1 + abs(x[i] - x[j])) * np.exp(-0.01 * (x[i]**2 + x[j]**2))
                
        # Asymmetric fractal valleys with dynamic depth and chaotic modulation
        for i in range(self.dim):
            asym_valley = (x[i]**4 + 0.3 * x[i]**3 + 0.1 * x[i]**2) * np.exp(-0.15 * abs(x[i])) * np.sin(10 * x[i])
            result += 0.4 * asym_valley
            
        # High-frequency fractal oscillations with dynamic amplitude and chaotic decay
        for i in range(self.dim):
            freq = 15 * (i + 1) * np.cos(i)
            result += 0.15 * np.sin(freq * x[i]) * np.exp(-0.03 * freq) * np.cos(20 * x[i])
            
        # Chaotic saddle points and irregular terrain features
        for i in range(self.dim):
            result += 0.2 * np.sin(50 * x[i]) * np.cos(25 * x[i]) * np.exp(-0.02 * abs(x[i])) * np.tanh(x[i]**2)
            
        # Dynamic scaling and multi-resolution interference
        for i in range(self.dim):
            result += 0.1 * np.sin(2**i * x[i] * np.cos(i)) * np.cos(2**(i+1) * x[i] * np.sin(i)) * np.log(1 + abs(x[i]))
            
        return result