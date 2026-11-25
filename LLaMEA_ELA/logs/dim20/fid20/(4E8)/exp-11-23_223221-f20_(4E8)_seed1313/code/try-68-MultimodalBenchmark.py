import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Fractal sine-wave modulation with recursive structure
        for i in range(self.dim):
            # Base fractal component with increasing frequency
            base_freq = 2.0 + 0.5 * np.sin(i * np.pi / 4.0)
            result += np.sin(base_freq * x[i]) * np.cos(base_freq * x[i]**1.5) + \
                     0.3 * np.sin(4 * base_freq * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Polynomial coupling with fractal scaling
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                # Self-similar interaction with scale factor
                scale = 0.5 + 0.3 * np.sin(i * j * np.pi / 6.0)
                result += scale * (x[i]**2) * (x[j]**2.5) * np.exp(-0.2 * (x[i]**2 + x[j]**2))
        
        # Recursive noise structure with fractal dimension
        noise = 0.0
        for i in range(self.dim):
            # Multi-scale noise components
            noise += 0.1 * np.sin(8 * x[i]) * np.cos(5 * x[i]) + \
                    0.05 * np.sin(16 * x[i]) * np.cos(10 * x[i]) + \
                    0.02 * np.sin(32 * x[i]) * np.cos(20 * x[i])
        
        result += noise
        
        # Add fractal scaling factor
        fractal_scale = 1.0 + 0.2 * np.sin(np.sum(x**2) * np.pi / 25.0)
        result *= fractal_scale
        
        # Normalize by dimension
        return result / self.dim