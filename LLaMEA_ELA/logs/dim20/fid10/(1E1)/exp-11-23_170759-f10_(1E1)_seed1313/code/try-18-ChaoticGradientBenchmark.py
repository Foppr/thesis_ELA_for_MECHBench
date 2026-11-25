import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Base quadratic term with chaotic perturbation
        result = 0.5 * np.sum(x**2)
        
        # Add chaotic gradient components using sine and cosine modulations
        for i in range(min(self.dim, 8)):
            # Create a chaotic effect with varying frequency and amplitude
            freq = 2.0 + 0.5 * np.sin(i * 0.7)
            amp = 1.0 + 0.3 * np.cos(i * 0.5)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5)
        
        # Embed saddle points with varying heights
        if self.dim >= 2:
            saddle_height = 0.8 + 0.4 * np.sin(x[0] * 0.3)
            result += saddle_height * (x[0]**2 - x[1]**2) * (1.0 + 0.2 * np.cos(x[0]))
        
        # Add periodic attractor wells with varying depths and positions
        for i in range(min(self.dim, 5)):
            well_depth = 0.6 + 0.4 * np.sin(i * 0.8)
            well_position = 2.0 * np.cos(i * 0.6)
            result += well_depth * np.exp(-0.5 * (x[i] - well_position)**2) * (1.0 + 0.3 * np.sin(x[i]))
        
        # Multi-scale harmonic modulation
        mod_freqs = [1.0, 2.0, 4.0, 8.0]
        for freq in mod_freqs:
            result += 0.15 * np.sum(np.sin(freq * x) + 0.3 * np.cos(freq * x))
        
        # Add a non-convex component with multiple local minima
        if self.dim >= 2:
            result += 0.3 * (x[0]**4 - 2*x[0]**2 + x[1]**4 - 2*x[1]**2) + \
                     0.2 * np.sin(5 * x[0]) * np.cos(5 * x[1])
        
        # Introduce a fractal-like structure using recursive sine components
        if self.dim >= 3:
            fractal_term = 0.2 * np.sin(x[0] * np.pi) * np.cos(x[1] * np.pi) * \
                          np.sin(x[2] * np.pi * 2) * (1.0 + 0.1 * x[0]**2)
            result += fractal_term
        
        # Add asymmetric gradient components
        asym_term = 0.1 * np.sum(np.abs(x)**1.5 * np.sign(x)) + \
                   0.05 * np.sum((x - 1.0)**3 * (x < 1.0)) + \
                   0.05 * np.sum((x + 1.0)**3 * (x > -1.0))
        result += asym_term
        
        # Add a "valley" shaped component with steep gradients
        if self.dim >= 2:
            valley = 0.4 * (x[0] - x[1])**2 + 0.2 * np.abs(x[0] + x[1])
            result += valley
            
        return result