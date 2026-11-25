import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Add enhanced trigonometric chaos with higher frequencies and more complex interactions
        for i in range(self.dim):
            freq1 = 3 ** (i % 5 + 2)
            freq2 = 2 ** (i % 3 + 1)
            amp = 1.5 + 0.8 * np.sin(i * 0.7) * np.cos(i * 0.3)
            result += amp * np.sin(freq1 * x[i]) * np.cos(freq2 * x[i] * 0.5) * np.exp(-0.03 * x[i]**2)
            
        # Add enhanced radial symmetry with multiple peaks and valleys
        r = np.sqrt(np.sum(x**2))
        result += 0.5 * np.sin(15 * r) * np.cos(8 * r) * np.exp(-0.08 * r**2)
        
        # Add stronger cross-dimensional coupling with chaotic interaction
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = np.sin(x[i] * x[j]) * np.cos(x[i] + x[j]) * np.sin((x[i] - x[j])**2)
                result += 0.1 * interaction * (1 + 0.3 * np.sin(i + j) * np.cos(i * j))
                
        # Add enhanced polynomial barriers with varying degrees and coupling
        for i in range(self.dim):
            result += 0.2 * (x[i]**6 - 3*x[i]**4 + 3*x[i]**2 - 1) * np.exp(-0.07 * abs(x[i]))
            
        # Add global minimum structure with multiple local minima and enhanced chaos
        for i in range(self.dim):
            result += 0.3 * np.exp(-0.5 * ((x[i] - 1.5) / 0.4)**2) * np.sin(12 * x[i]) * np.cos(6 * x[i])
            
        # Add additional chaotic noise term
        noise = 0.05 * np.sum(np.sin(x * 7) * np.cos(x * 3))
        result += noise
        
        return result