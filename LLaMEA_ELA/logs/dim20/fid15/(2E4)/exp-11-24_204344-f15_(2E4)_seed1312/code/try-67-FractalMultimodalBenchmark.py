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
            # Build fractal pattern through nested trigonometric functions with altered frequencies
            for depth in range(1, 5):
                val = np.sin(3**depth * val) + 0.4 * np.cos(2**depth * val)
            fractal += val**2
        
        # Power-law scaling with multiple frequency components
        power_law = 0.0
        for i in range(self.dim):
            freqs = [1, 3, 5, 7, 11]
            scale = 1.0 / (1.0 + np.abs(x[i]))
            for f in freqs:
                power_law += (scale**(f+1)) * np.sin(f * x[i]) * np.cos(f * x[i] * 0.3)
        
        # Multi-scale interaction terms with exponential decay
        multiscale = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Slightly reduced interaction range
                dist = np.abs(x[i] - x[j])
                multiscale += np.exp(-dist**2) * np.sin(15 * dist) * np.cos(3 * dist)
        
        # Self-similar ridge structure with varying amplitudes
        ridge = 0.0
        for i in range(self.dim):
            amp = 1.0 + 0.4 * np.sin(i * 0.9)
            ridge += amp * np.sin(10 * x[i]) * np.cos(5 * x[i]) * np.exp(-0.3 * x[i]**2)
        
        # Cross-dimensional coupling with polynomial interactions
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += (x[i]**2 + x[j]**2)**1.7 * np.sin(x[i] * x[j]) * np.cos(0.3 * x[i] * x[j])
        
        # Noise-like perturbations with chaotic behavior
        noise = 0.0
        for i in range(self.dim):
            noise += 0.15 * np.sin(25 * x[i] + np.sin(12 * x[i])) * np.cos(18 * x[i])
        
        # Final scaling and combination
        return quadratic + 0.9 * fractal + 0.35 * power_law + 0.6 * multiscale + 0.45 * ridge + 0.25 * coupling + noise