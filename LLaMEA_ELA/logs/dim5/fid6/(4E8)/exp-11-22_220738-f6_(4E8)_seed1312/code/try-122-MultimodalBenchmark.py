import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.oscillator_freq = 2.0 * np.pi
        self.fractal_dim = 1.3 + np.random.rand() * 0.4
        self.gating_strength = 1.5 + np.random.rand() * 1.0
        
    def f(self, x):
        # Clip input to bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum harmonic oscillator potential
        quantum_potential = np.sum((x**2) * np.sin(self.oscillator_freq * x)**2)
        
        # Fractional Brownian motion-like gradient component
        fbm_component = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                fbm_component += (dist ** self.fractal_dim) * np.sin(dist)
        
        # Neural gating mechanism with memory-like effects
        gating = 0.0
        for i in range(self.dim):
            gate_val = 1.0 / (1.0 + np.exp(-self.gating_strength * x[i]))
            gating += gate_val * np.cos(0.5 * x[i]) * np.sin(0.3 * x[i])
        
        # Fractal ridge structure with varying scaling
        fractal_ridge = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.5 * np.sin(i * 0.7)
            fractal_ridge += scale * np.sin(x[i] * 3.0) * np.cos(x[i] * 2.0)
        
        # Asymmetric multi-peak interaction
        multi_peak = 0.0
        for i in range(self.dim):
            peak_val = (x[i] - 1.5)**4 + (x[i] + 1.5)**4 + 0.5 * np.sin(3.0 * x[i])
            multi_peak += peak_val
        
        # Combine all components
        result = quantum_potential + 0.3 * fbm_component + 0.2 * gating + 0.1 * fractal_ridge + 0.4 * multi_peak
        
        # Add a global scaling factor based on dimensionality
        result *= (1.0 + 0.1 * self.dim)
        
        return result