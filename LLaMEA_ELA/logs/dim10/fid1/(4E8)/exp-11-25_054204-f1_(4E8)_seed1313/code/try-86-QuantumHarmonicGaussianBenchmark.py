import numpy as np

class QuantumHarmonicGaussianBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate quantum-like harmonic frequencies
        self.frequencies = np.arange(1, dim + 1) * np.pi / (dim + 1)
        # Precompute Gaussian cluster centers with fractal scaling
        self.clusters = []
        for i in range(dim):
            self.clusters.append(np.sin(i * np.pi / (dim + 1)) * 4.0)
        self.clusters = np.array(self.clusters)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum harmonic oscillation component
        f1 = 0.5 * np.sum((x**2) * np.sin(self.frequencies)**2)
        
        # Adaptive Gaussian cluster attraction
        f2 = 0.0
        for i in range(self.dim):
            center = self.clusters[i]
            sigma = 0.5 + 0.5 * np.cos(i * np.pi / (self.dim + 1))
            f2 -= 0.3 * np.exp(-0.5 * ((x[i] - center) / sigma)**2)
        
        # Fractal-like scaling with dimension-dependent modulation
        fractal_scale = 1.0 + 0.3 * np.sin(np.log(self.dim + 1))
        f3 = 0.2 * np.sum((x**4) * np.cos(fractal_scale * x))
        
        # Cross-dimensional coupling with quantum phase interference
        cross_term = 0.0
        for i in range(self.dim - 1):
            phase = np.sin(x[i] + x[i+1]) * (i + 1)
            cross_term += np.cos(phase) * np.sin(x[i] * x[i+1])
        f4 = 0.15 * cross_term
        
        # Multi-scale harmonic modulation
        f5 = 0.25 * np.sum(np.sin(2.0 * x) * np.cos(3.0 * x) * np.sin(5.0 * x))
        
        # Adaptive polynomial with quantum-like tunneling effect
        f6 = 0.1 * np.sum(x**5 * np.exp(-x**2 / 10.0))
        
        # Self-similar fractal structure with dimension scaling
        fractal_structure = 0.0
        for i in range(self.dim):
            fractal_structure += np.sin(x[i] * (i + 1)) * np.cos(x[i] * (i + 1)**2)
        f7 = 0.1 * fractal_structure
        
        # Combined dimensionality scaling factor
        scale_factor = 1.0 + 0.1 * np.log(self.dim + 1)
        
        return scale_factor * (f1 + f2 + f3 + f4 + f5 + f6 + f7)