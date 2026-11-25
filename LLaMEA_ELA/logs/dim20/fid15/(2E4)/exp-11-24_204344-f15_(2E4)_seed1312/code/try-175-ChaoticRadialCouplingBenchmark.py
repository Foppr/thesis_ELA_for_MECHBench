import numpy as np

class ChaoticRadialCouplingBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Radial polynomial chaos component with dynamic scaling
        r = np.sqrt(np.sum(x**2))
        radial = (r**4 + 0.5 * r**3 - 2.0 * r**2 + 1.5 * r + 0.8) * np.exp(-0.1 * r)
        
        # Symmetric polynomial landscape with multiple local minima
        poly = 0.0
        for i in range(self.dim):
            poly += (x[i]**6 - 3.0 * x[i]**4 + 2.0 * x[i]**2) * np.cos(0.5 * x[i])
        
        # Cross-dimensional coupling with varying interaction strengths
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 0.5 + 0.3 * np.sin(i * j * 0.7)
                cross += coupling_strength * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
        
        # Dynamic scaling based on dimension index
        dynamic_scale = 0.0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.2 * np.sin(i * 1.3)
            dynamic_scale += scale_factor * np.exp(-0.5 * (x[i] - 0.5)**2) * np.sin(3.0 * x[i])
        
        # Asymmetric harmonic components with time-varying frequencies
        harmonic = 0.0
        for i in range(self.dim):
            freq = 2.0 + 1.0 * np.sin(i * 0.8)
            amp = 1.5 + 0.5 * np.cos(i * 0.6)
            harmonic += amp * np.sin(freq * x[i] + np.sin(x[i])) * np.cos(freq * x[i])
        
        # Noise injection with chaotic amplitude modulation
        noise = 0.0
        for i in range(self.dim):
            noise_amp = 0.3 + 0.1 * np.sin(i * 2.1)
            noise += noise_amp * np.sin(x[i] * np.pi * (1 + 0.1 * np.sin(i)))
        
        # Fractional dimensionality interaction with irregular coupling
        frac_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                if i + j > 0:
                    frac_interaction += (x[i]**2 + x[j]**2) / (i + j) * np.exp(-0.3 * (x[i] - x[j])**2)
        
        # Final combination with weighted components
        return 0.6 * radial + 0.8 * poly + 0.7 * cross + 0.9 * dynamic_scale + \
               1.1 * harmonic + 0.5 * noise + 0.4 * frac_interaction