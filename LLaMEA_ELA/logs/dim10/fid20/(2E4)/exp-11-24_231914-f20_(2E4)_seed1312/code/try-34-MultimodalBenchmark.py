import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like self-similar structure using nested trigonometric functions
        fractal = 0.0
        for i in range(self.dim):
            # Nested sinusoidal modulation with varying frequencies
            val = x[i]
            for freq in [2, 3, 5]:
                val = np.sin(freq * val)
            fractal += val ** 2
        
        # Sinusoidal modulation with varying amplitudes and frequencies
        modulated = 0.0
        for i in range(self.dim):
            # Use different frequency components for each dimension
            modulated += np.sin(10 * x[i]) * np.cos(7 * x[i]) * np.exp(-0.1 * abs(x[i]))
        
        # Gradient saturation effect: limit large gradients with hyperbolic tangent
        saturation = 0.0
        for i in range(self.dim):
            saturation += np.tanh(x[i]) ** 2
        
        # Multi-scale oscillatory structure with overlapping local minima
        oscillatory = 0.0
        for i in range(self.dim):
            # Combine multiple frequencies to create complex terrain
            oscillatory += (np.sin(15 * x[i]) + 0.5 * np.sin(30 * x[i]) + 
                           0.2 * np.sin(60 * x[i])) ** 2
        
        # Cross-term interactions with exponential decay
        cross_interaction = 0.0
        for i in range(self.dim - 1):
            cross_interaction += np.exp(-0.5 * (i + 1)) * np.sin(x[i] * x[i+1])
        
        # Combine all components to form the final landscape
        return 0.3 * fractal + 0.25 * modulated + 0.15 * saturation + 0.2 * oscillatory + 0.1 * cross_interaction