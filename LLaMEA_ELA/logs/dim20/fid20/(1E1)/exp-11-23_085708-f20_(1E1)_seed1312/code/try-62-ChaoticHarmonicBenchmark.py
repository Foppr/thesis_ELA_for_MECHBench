import numpy as np

class ChaoticHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Scale to [-5, 5]
        x_scaled = x / 5.0
        
        # Fractal-like harmonic component with multi-scale frequencies
        fractal_term = 0.0
        for i in range(self.dim):
            # Use chaotic-like frequency modulation
            freq = 2 ** (i % 3 + 1) * (1 + 0.1 * np.sin(x[i]))
            fractal_term += (np.sin(freq * x[i]) + 
                           0.5 * np.cos(freq * x[i] * 1.5) + 
                           0.2 * np.sin(freq * x[i] * 3))
        
        # Chaotic gradient modulation with logistic map inspired component
        chaotic_mod = 1.0
        for i in range(self.dim):
            # Logistic map inspired chaotic behavior
            logistic_val = 4.0 * (x[i] / 5.0) * (1 - x[i] / 5.0)
            chaotic_mod *= (1 + 0.3 * np.sin(logistic_val * 10) + 
                          0.2 * np.cos(logistic_val * 7))
        
        # Multi-scale cross-terms with self-similar patterns
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited interaction for scalability
                # Self-similar harmonic interactions
                cross_term += (np.sin(x[i] * x[j] * 0.5) * 
                             np.cos(x[i] * x[j] * 0.3) * 
                             np.sin(0.1 * (x[i] + x[j])) *
                             (i + j + 1) * 0.1)
        
        # Multi-scale periodic component with irregular frequencies
        periodic_term = 0.0
        for i in range(self.dim):
            # Use different periods based on dimension index
            period = 2 * np.pi * (i % 5 + 1)
            periodic_term += np.sin(x[i] / period) * np.cos(x[i] / (period * 0.7))
        
        # Adaptive curvature modulation with fractal-like behavior
        curvature_mod = 1.0
        for i in range(self.dim):
            # Fractal-inspired curvature adjustment
            curvature_mod *= (1 + 0.2 * np.sin(x[i] * 0.5) * 
                            np.cos(x[i] * 0.3) * 
                            np.sin(x[i] * 0.1))
        
        # Combined landscape with irregular valleys and sharp transitions
        result = (fractal_term * chaotic_mod + 
                 cross_term * curvature_mod + 
                 periodic_term * 0.5 +
                 0.1 * np.sum(x**4) +  # Add quartic term for global shaping
                 2.0)  # Offset to ensure positive fitness
        
        return result