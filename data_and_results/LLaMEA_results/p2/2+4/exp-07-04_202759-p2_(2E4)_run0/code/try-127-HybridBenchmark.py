import numpy as np

class HybridBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with multiple oscillatory modes
        radial = np.sum(np.sin(5.0 * x) * np.cos(3.0 * x) * np.exp(-0.1 * x**2))
        
        # Multi-modal sinusoidal component with varying frequencies
        modal = 0
        for i in range(self.dim):
            freq = 10.0 + 5.0 * np.sin(0.5 * i)
            modal += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7) * np.exp(-0.05 * x[i]**2)
        
        # Cross-dimensional interaction terms with coupling strength
        cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 1.0 + 0.5 * np.sin(2.0 * (x[i] + x[j]))
                cross += coupling * np.sin(3.0 * (x[i] - x[j])) * np.cos(2.0 * (x[i] - x[j]))
        
        # Fractal-like self-similarity through recursive scaling
        fractal = 0
        for i in range(self.dim):
            scale = 1.0 + 0.3 * np.sin(7.0 * x[i])
            fractal += scale * np.sin(10.0 * x[i]) * np.cos(8.0 * x[i]) * np.exp(-0.2 * x[i]**2)
        
        # Memory-dependent term using previous dimensions
        memory = 0
        for i in range(self.dim):
            if i > 0:
                memory += np.sin(0.8 * x[i]) * np.cos(0.8 * x[i]) * (1.0 + 0.2 * np.sin(x[i-1]))
        
        # Combine all components with dynamic weights
        return 0.4 * radial + 0.3 * modal + 0.2 * cross + 0.07 * fractal + 0.03 * memory