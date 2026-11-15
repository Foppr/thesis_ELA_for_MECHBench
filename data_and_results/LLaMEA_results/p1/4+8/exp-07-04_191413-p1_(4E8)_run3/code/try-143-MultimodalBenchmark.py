import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial chaos component with mixed degrees
        poly_chaos = np.sum((x_norm**2 + x_norm**4 + x_norm**6) * np.exp(-0.5 * x_norm**2))
        
        # Radial basis function with varying widths and centers
        rbfs = 0.0
        centers = np.linspace(-1, 1, 7)
        widths = np.logspace(-2, 0, 7)
        for i, (c, w) in enumerate(zip(centers, widths)):
            rbfs += np.exp(-w * np.sum((x_norm - c)**2))
        
        # Dynamic sine-wave interactions with time-varying frequencies
        sine_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq = 2 * np.pi * (i + j + 1)
                sine_interaction += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[j])
        
        # Hybrid conditioning with exponential and logarithmic terms
        cond_term = np.sum(np.exp(x_norm**2) + np.log(1 + x_norm**2))
        
        # Multi-scale chaotic modulation using fractional powers
        chaotic_mod = 0.0
        for i in range(self.dim):
            chaotic_mod += np.sin(10 * np.pi * x_norm[i]**1.5) * np.cos(15 * np.pi * x_norm[i]**2.5)
        
        # Cross-dimensional coupling with varying coupling strengths
        coupling = 0.0
        for i in range(self.dim-1):
            coupling += (i + 1) * np.sin(np.pi * x_norm[i]) * np.cos(np.pi * x_norm[i+1])
        
        # Add a global scaling factor and combine all components
        return 0.5 * poly_chaos + 0.3 * rbfs + 0.2 * sine_interaction + 0.1 * cond_term + 0.15 * chaotic_mod + 0.05 * coupling