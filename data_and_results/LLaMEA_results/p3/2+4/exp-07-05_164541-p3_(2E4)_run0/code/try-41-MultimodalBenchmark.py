import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Logarithmic spiral component with angular frequency modulation
        spiral = np.sum(np.exp(-0.1 * np.sum(x**2, axis=0)) * np.cos(3 * np.arctan2(x[1], x[0]) + 0.5 * np.sum(x**2)))
        
        # Spherical harmonics with varying degree and order
        harmonics = np.sum((x[0]**2 + x[1]**2)**2 * np.sin(4 * np.arctan2(x[1], x[0])) * np.cos(2 * np.arctan2(x[1], x[0])))
        
        # Multi-scale Gaussian peaks with varying amplitudes and widths
        peaks = 0
        for i in range(1, 6):
            peaks += i * np.exp(-0.5 * np.sum(((x - i * 0.5) / (0.5 * i))**2, axis=0))
        
        # Cross-dimensional coupling with geometric progression and phase shifts
        coupling = np.sum(np.sin(np.pi * x) * np.cos(2 * np.pi * x) * np.sin(3 * np.pi * x) * np.cos(4 * np.pi * x))
        
        # Chaotic modulation using logistic map iterations
        chaotic = 0
        r = 3.9
        for _ in range(10):
            chaotic = r * chaotic * (1 - chaotic)
        chaotic = np.sum(chaotic * np.sin(np.pi * x) * np.cos(2 * np.pi * x))
        
        # Combine all terms with optimized weights and add a global offset
        return 0.3 * spiral + 0.25 * harmonics + 0.2 * peaks + 0.15 * coupling + 0.1 * chaotic + 2.1