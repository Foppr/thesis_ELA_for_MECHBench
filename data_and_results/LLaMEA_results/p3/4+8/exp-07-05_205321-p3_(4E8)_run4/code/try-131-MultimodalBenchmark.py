import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Fractal-like radial component with self-similar structure
        r = np.sqrt(np.sum(x_norm**2))
        fractal_radial = np.exp(-r**2.0) * (1.0 + 0.3 * np.sin(20 * r) + 0.2 * np.cos(15 * r) + 0.1 * np.sin(30 * r**2))
        
        # Quantum harmonic angular terms with dimensionally adaptive frequencies
        quantum_angular = 0.0
        for i in range(self.dim):
            freq = (i + 1) * 2.0
            quantum_angular += np.sin(freq * np.pi * x_norm[i]) * np.cos(freq * np.pi * x_norm[i]) * np.exp(-0.5 * (i / self.dim)**2)
        
        # Multi-scale periodicity with adaptive amplitude
        multi_periodic = 0.0
        scales = [2, 4, 6, 8]
        for scale in scales:
            multi_periodic += np.sum(np.sin(scale * np.pi * x_norm + 0.5 * scale) * np.cos(scale * np.pi * x_norm - 0.3 * scale))
        
        # Cross-dimensional coupling with exponential decay
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = np.exp(-0.1 * (i - j)**2)
                cross_coupling += coupling_strength * np.sin(5 * np.pi * x_norm[i]) * np.cos(4 * np.pi * x_norm[j])
        
        # Adaptive difficulty term based on dimensionality
        dim_adapt = 0.0
        for i in range(self.dim):
            dim_adapt += np.sin(10 * np.pi * x_norm[i]**3) * np.cos(9 * np.pi * x_norm[i]**2) * (1.0 + 0.1 * self.dim)
        
        # Combined function with dynamic weighting
        total = 0.4 * fractal_radial + 0.25 * quantum_angular + 0.2 * multi_periodic + 0.1 * cross_coupling + 0.05 * dim_adapt
        
        # Add a small noise term for increased robustness
        noise = 0.001 * np.random.rand()
        
        return total + noise + 1.0