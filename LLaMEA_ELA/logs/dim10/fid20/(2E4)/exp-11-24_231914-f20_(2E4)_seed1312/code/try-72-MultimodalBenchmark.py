import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute parameters for hyperbolic interactions and multimodal structure
        self.hyperbolic_params = [1.2, 2.1, 0.8, 1.5, 2.7][:min(dim, 5)]
        self.multimodal_freqs = [3.0, 4.5, 2.2, 5.1, 3.8][:min(dim, 5)]
        self.correlation_decay = [0.95, 0.87, 0.92, 0.89, 0.91][:min(dim, 5)]
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        base = np.sum(x**2) / self.dim
        
        # Hyperbolic saddle-point structure with enhanced nonlinearity
        hyperbolic = 0.0
        for i in range(self.dim):
            param = self.hyperbolic_params[i % len(self.hyperbolic_params)]
            hyperbolic += (np.tanh(param * x[i]) * np.exp(-0.1 * x[i]**2) + 
                          0.5 * np.sinh(param * x[i]**2) * np.exp(-0.2 * x[i]))
        
        # Multimodal components with varying frequencies and amplitudes
        multimodal = 0.0
        for i in range(self.dim):
            freq = self.multimodal_freqs[i % len(self.multimodal_freqs)]
            multimodal += (1.8 * np.sin(freq * x[i]) * np.cos(0.5 * freq * x[i]**2) +
                          1.2 * np.sin(2 * freq * x[i]) * np.cos(freq * x[i]**3))
        
        # Correlation decay component with exponential weighting
        correlation = 0.0
        for i in range(self.dim - 1):
            decay = self.correlation_decay[i % len(self.correlation_decay)]
            correlation += (x[i] * x[i+1]) * np.exp(-decay * (x[i] - x[i+1])**2)
        
        # Global minimum shifting with sinusoidal modulation
        shift = 0.0
        for i in range(self.dim):
            shift += 0.6 * np.sin(3.0 * x[i]) * np.cos(2.0 * x[i]) * np.exp(-0.15 * np.abs(x[i]))
        
        # Asymmetric hyperbolic coupling with strong interaction terms
        coupling = 0.0
        for i in range(self.dim - 2):
            coupling += (0.8 * np.tanh(1.5 * x[i]) * np.cosh(2.0 * x[i+1]) * 
                        np.exp(-0.2 * x[i+2]**2) + 0.4 * np.sinh(1.2 * x[i]) * np.tanh(1.8 * x[i+1]))
        
        # Higher-order polynomial interactions with chaotic behavior
        high_order = 0.0
        for i in range(self.dim):
            high_order += (0.5 * x[i]**4 + 0.3 * x[i]**6) * np.exp(-0.1 * np.abs(x[i]))
        
        # Modified chaotic gradient field with stronger discontinuities
        chaotic = 0.0
        for i in range(self.dim):
            if x[i] < -2:
                chaotic += np.sin(10 * x[i]) * np.exp(-0.5 * x[i]**2)
            elif x[i] > 2:
                chaotic += np.cos(8 * x[i]) * np.exp(-0.3 * x[i]**2)
            else:
                chaotic += np.tan(4 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Combine all components with different weights to create complex landscape
        return base + 1.8 * hyperbolic + 1.5 * multimodal + 0.7 * correlation + \
               0.6 * shift + 0.8 * coupling + 0.5 * high_order + 1.2 * chaotic