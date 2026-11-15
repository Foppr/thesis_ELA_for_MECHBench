import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_global = np.zeros(dim)
    
    def f(self, x):
        x = np.array(x)
        
        # Normalize to [-5, 5]
        x = x / 5.0
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Add fractal-like periodic components with increasing frequency and amplitude
        for i in range(1, min(7, self.dim + 1)):
            freq = 2**i
            amp = 0.2 / (i**1.5)
            term = amp * np.sin(freq * np.pi * x) * np.cos(freq * np.pi * x)
            result += np.sum(term**2)
        
        # Recursive fractal structure using a modified Barnsley-like construction with chaotic feedback
        fractal_penalty = 0.0
        for i in range(self.dim):
            xi = x[i]
            scale = 0.4
            for depth in range(1, 6):
                xi = scale * np.sin(10 * xi) + 0.5
                fractal_penalty += np.sin(15 * xi) * np.exp(-depth / 4.0)
        
        # Add chaotic component using sine-Gordon-like terms with varying coupling
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += np.sin(25 * x[i]) * np.cos(20 * x[i]) * np.exp(-i / (self.dim * 2.0))
        
        # Add multiple nested minima with exponentially decaying depths and random phase shifts
        nested_penalty = 0.0
        for k in range(1, 10):
            level_scale = 1.0 / (2**k)
            loc = np.full(self.dim, level_scale)
            for i in range(self.dim):
                phase = np.sin(k * i * np.pi / self.dim) * 0.5
                loc[i] = level_scale * np.sin(k * i * np.pi / self.dim + phase)
            distance = np.sum((x - loc)**2)
            nested_penalty += np.exp(-distance / (2.0 * (k**1.8))) * np.cos(k * np.pi / 4.0)
        
        # Add cross-dimensional coupling with exponential decay
        coupling_penalty = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_penalty += np.exp(-((x[i] - x[j])**2) / (2.0 * (i + j + 1))) * np.sin(10 * (x[i] + x[j]))
        
        # Add noise-like irregularity with multi-scale perturbations
        irregularity = 0.0
        for scale in [0.1, 0.3, 0.7]:
            for i in range(self.dim):
                irregularity += np.sin(30 * x[i] / scale) * np.cos(25 * x[i] / scale) * scale
        
        result += fractal_penalty + chaotic_term + 0.5 * nested_penalty + coupling_penalty + irregularity
        
        return result