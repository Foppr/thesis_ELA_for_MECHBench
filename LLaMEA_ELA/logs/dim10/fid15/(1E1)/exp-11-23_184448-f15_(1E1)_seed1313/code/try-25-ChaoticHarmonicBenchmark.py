import numpy as np

class ChaoticHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Base quadratic term
        base_term = np.sum(x**2)
        
        # Chaotic harmonic oscillations with exponential decay
        harmonic_term = 0.0
        for i in range(self.dim):
            # Adaptive frequency and amplitude based on dimension
            freq = 2.0 + 3.0 * np.sin(i * np.pi / self.dim)
            amp = 1.5 + 0.5 * np.cos(i * np.pi / (self.dim + 1))
            
            # Add chaotic modulation to frequency and amplitude
            chaos_mod = 0.3 * np.sin(x[i] * np.pi / 4.0)
            freq_mod = freq * (1.0 + 0.2 * chaos_mod)
            amp_mod = amp * (1.0 + 0.1 * np.cos(x[i] * np.pi / 3.0))
            
            # Exponentially decaying harmonic
            decay = np.exp(-0.1 * np.abs(x[i]))
            harmonic_term += amp_mod * np.sin(freq_mod * x[i]) * decay
        
        # Cross-dimensional coupling with chaotic interaction strengths
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic coupling strength
                coupling_strength = 0.5 + 0.3 * np.sin(i * j * np.pi / (self.dim + 1))
                coupling_term += coupling_strength * np.sin(x[i] * x[j]) * (x[i]**2 + x[j]**2)
        
        # Adaptive basin structure with chaotic centers
        basin_term = 0.0
        for i in range(self.dim):
            # Chaotic basin center positions
            center = 2.0 * np.sin(i * np.pi / (self.dim + 2))
            depth = 0.5 + 0.5 * np.cos(i * np.pi / self.dim)
            
            # Basin with exponential penalty
            distance = np.abs(x[i] - center)
            basin_term += depth * (distance**2) * np.exp(-0.2 * distance)
        
        # Multi-scale chaotic perturbation term
        perturbation_term = 0.0
        scales = [1.0, 0.5, 0.25]
        for scale in scales:
            for i in range(self.dim):
                perturbation_term += scale * np.sin(x[i] / scale) * np.cos(x[i] * scale)
        
        # Dimensionality-dependent scaling
        dim_scale = 1.0 + 0.3 * np.log(self.dim + 1)
        
        return dim_scale * (base_term + 0.4 * harmonic_term + 0.25 * coupling_term + 
                           0.3 * basin_term + 0.2 * perturbation_term)