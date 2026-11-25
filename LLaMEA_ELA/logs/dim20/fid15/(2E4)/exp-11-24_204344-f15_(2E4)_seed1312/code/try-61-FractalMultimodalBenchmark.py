import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Base quadratic term
        quadratic = 0.5 * np.sum(x**2) / self.dim
        
        # Fractal-like component using recursive trigonometric combinations
        fractal = 0.0
        for i in range(self.dim):
            val = x[i]
            # Build fractal pattern through nested trigonometric functions
            for depth in range(1, 6):
                val = np.sin(2**depth * val) + 0.5 * np.cos(3**depth * val)
            fractal += val**2
        
        # Power-law scaling with multiple frequency components
        power_law = 0.0
        for i in range(self.dim):
            freqs = [1, 2, 3, 5, 7]
            scale = 1.0 / (1.0 + np.abs(x[i]))
            for f in freqs:
                power_law += (scale**f) * np.sin(f * x[i]) * np.cos(f * x[i] * 0.5)
        
        # Multi-scale interaction terms with exponential decay
        multiscale = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):  # Limited range for computational efficiency
                dist = np.abs(x[i] - x[j])
                multiscale += np.exp(-dist**2) * np.sin(10 * dist) * np.cos(5 * dist)
        
        # Self-similar ridge structure with varying amplitudes
        ridge = 0.0
        for i in range(self.dim):
            amp = 1.0 + 0.3 * np.sin(i * 0.7)
            ridge += amp * np.sin(8 * x[i]) * np.cos(4 * x[i]) * np.exp(-0.2 * x[i]**2)
        
        # Cross-dimensional coupling with polynomial interactions
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += (x[i]**2 + x[j]**2)**1.5 * np.sin(x[i] * x[j]) * np.cos(0.5 * x[i] * x[j])
        
        # Noise-like perturbations with chaotic behavior
        noise = 0.0
        for i in range(self.dim):
            noise += 0.1 * np.sin(20 * x[i] + np.sin(10 * x[i])) * np.cos(15 * x[i])
        
        # Final scaling and combination
        return quadratic + 0.8 * fractal + 0.3 * power_law + 0.5 * multiscale + 0.4 * ridge + 0.2 * coupling + noise