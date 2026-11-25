import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Time-varying fractal potential with chaotic modulation
        fractal_potential = 0
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(0.3 * x[i] + self.dim * 0.1)
            amp = 1.0 + 0.5 * np.cos(0.4 * x[i] + self.dim * 0.2)
            phase = 0.5 * np.sin(0.6 * x[i] + 0.3 * self.dim)
            fractal_potential += amp * np.sin(freq * x[i] + phase) * np.exp(-0.1 * x[i]**2)
        
        # Dynamic coupling with adaptive weights
        coupling = 0
        for i in range(self.dim):
            weight = 1.0 + 0.3 * np.sin(0.5 * x[i] + self.dim * 0.25)
            for j in range(i+1, min(i+3, self.dim)):
                coupling += weight * (x[i]**2 + x[j]**2) * np.exp(-0.2 * (x[i] - x[j])**2)
        
        # Multi-scale oscillatory components with varying frequencies
        oscillatory = 0
        for i in range(self.dim):
            freq1 = 1.0 + 0.5 * np.sin(0.2 * x[i])
            freq2 = 2.0 + 1.0 * np.cos(0.3 * x[i])
            freq3 = 3.0 + 1.5 * np.sin(0.4 * x[i])
            oscillatory += np.sin(freq1 * x[i]) * np.cos(freq2 * x[i]**2) * np.sin(freq3 * x[i]**3)
        
        # Adaptive conditioning with chaotic scaling
        condition = 1.5 + 0.8 * np.sin(self.dim * 0.3 + 0.4 * np.cos(x[0] if self.dim > 0 else 0))
        
        # Asymmetric multimodal structure with exponential modulation
        asymmetric = 0
        for i in range(self.dim):
            term1 = np.exp(-0.5 * (x[i] - 2.0)**2) * np.sin(3.0 * x[i])
            term2 = np.exp(-0.5 * (x[i] + 2.0)**2) * np.cos(2.5 * x[i])
            term3 = np.exp(-0.3 * x[i]**2) * np.sin(4.0 * x[i]**2)
            asymmetric += term1 + term2 + term3
        
        # Combine all components with optimized weights
        return condition * (0.3 * fractal_potential + 0.25 * coupling + 
                           0.25 * oscillatory + 0.2 * asymmetric)