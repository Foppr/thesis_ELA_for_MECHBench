import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Add multiple global minima with dynamic chaotic modulation
        for i in range(self.dim):
            result += 1.2 * np.exp(-0.02 * x[i]**2) * np.sin(8 * x[i])**4
            
        # Add fractal-like recursive structure with varying frequencies
        for i in range(self.dim):
            freq = 3.0 + 0.5 * np.sin(i * 0.7)
            result += 0.8 * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5) * np.exp(-0.1 * i)
            
        # Add adaptive oscillation with dimension-dependent amplitude
        for i in range(self.dim):
            amp = 0.6 + 0.2 * np.sin(i * 0.3)
            result += amp * np.sin(4 * x[i] + np.cos(x[i]))**2
            
        # Add dynamic cross-dimensional coupling with exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.exp(-0.05 * (i+j)) * np.sin(x[i] * x[j])
                result += 0.4 * coupling * (1 + 0.3 * np.sin(2 * (x[i] - x[j])))
                
        # Add energy-based penalty with dimensionality scaling
        energy = np.sum(np.abs(x)**3.2)
        result += 0.15 * energy * (1 + 0.05 * self.dim)
        
        # Add a multi-scale chaotic component with varying frequencies and amplitudes
        for i in range(self.dim):
            scale = 1.0 + 0.1 * np.sin(i * 0.5)
            result += 0.3 * scale * np.sin(10 * x[i] + np.sin(3 * x[i])) * np.cos(7 * x[i] + np.cos(2 * x[i]))
            
        # Add a complex interaction term with trigonometric coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.25 * np.sin(x[i] * np.cos(x[j])) * np.cos(x[j] * np.sin(x[i]))
                
        # Add a global scaling factor with logarithmic growth
        result *= (1.0 + 0.08 * np.log(1 + self.dim))
        
        return result