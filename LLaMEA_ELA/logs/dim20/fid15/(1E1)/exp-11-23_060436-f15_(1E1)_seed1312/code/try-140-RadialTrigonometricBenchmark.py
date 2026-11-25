import numpy as np

class RadialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with multiple concentric peaks
        r = np.sqrt(np.sum(x**2))
        radial = 10 * np.exp(-0.1 * r) * np.sin(2 * r) + 5 * np.exp(-0.05 * r) * np.cos(3 * r)
        
        # Trigonometric component with varying frequencies and amplitudes
        trig = 0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(i * 0.5)
            amp = 1.0 + 0.3 * np.cos(i * 0.3)
            trig += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
            
        # Cross-dimensional interaction with interference patterns
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                interaction += np.sin(dist) * np.cos(0.5 * dist) / (dist + 0.1)
                
        # Symmetric multi-modal component with controlled peak locations
        symmetric = 0
        peaks = [1.0, -1.0, 2.0, -2.0]
        for i in range(self.dim):
            min_val = float('inf')
            for p in peaks:
                val = (x[i] - p)**2 + 0.5 * np.sin(3 * x[i])
                if val < min_val:
                    min_val = val
            symmetric += min_val
            
        # Asymmetric noise component with chaotic modulation
        noise = 0
        for i in range(self.dim):
            chaos = np.sin(x[i] * (1.0 + 0.1 * np.sin(i))) * np.cos(x[i] * (1.0 + 0.1 * np.cos(i)))
            noise += chaos * (1.0 + 0.2 * np.sin(0.5 * i))
            
        # Combined function with weighted components
        return (radial * 0.3 +
                trig * 0.4 +
                interaction * 0.25 +
                symmetric * 0.2 +
                noise * 0.15)