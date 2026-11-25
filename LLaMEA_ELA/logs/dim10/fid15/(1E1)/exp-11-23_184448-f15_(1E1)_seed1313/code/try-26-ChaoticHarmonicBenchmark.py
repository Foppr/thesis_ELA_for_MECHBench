import numpy as np

class ChaoticHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Base quadratic term
        base_term = np.sum(x**2)
        
        # Chaotic harmonic oscillations with modified coefficients
        harmonic_term = 0.0
        for i in range(self.dim):
            # Adaptive frequency and amplitude with slight modifications
            freq = 1.5 + 2.5 * np.sin(i * np.pi / self.dim)
            amp = 1.2 + 0.8 * np.cos(i * np.pi / (self.dim + 1))
            
            # Add chaotic modulation to frequency and amplitude
            chaos_mod = 0.4 * np.sin(x[i] * np.pi / 5.0)
            freq_mod = freq * (1.0 + 0.15 * chaos_mod)
            amp_mod = amp * (1.0 + 0.08 * np.cos(x[i] * np.pi / 2.5))
            
            # Exponentially decaying harmonic
            decay = np.exp(-0.15 * np.abs(x[i]))
            harmonic_term += amp_mod * np.sin(freq_mod * x[i]) * decay
        
        # Cross-dimensional coupling with modified strengths
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Modified chaotic coupling strength
                coupling_strength = 0.3 + 0.4 * np.sin(i * j * np.pi / (self.dim + 2))
                coupling_term += coupling_strength * np.sin(x[i] * x[j]) * (x[i]**2 + x[j]**2)
        
        # Adaptive basin structure with shifted centers
        basin_term = 0.0
        for i in range(self.dim):
            # Shifted chaotic basin center positions
            center = 1.5 * np.sin(i * np.pi / (self.dim + 3)) + 0.5
            depth = 0.4 + 0.6 * np.cos(i * np.pi / self.dim)
            
            # Basin with exponential penalty
            distance = np.abs(x[i] - center)
            basin_term += depth * (distance**2) * np.exp(-0.15 * distance)
        
        # Multi-scale chaotic perturbation term with modified scales
        perturbation_term = 0.0
        scales = [1.2, 0.6, 0.3]
        for scale in scales:
            for i in range(self.dim):
                perturbation_term += scale * np.sin(x[i] / scale) * np.cos(x[i] * scale)
        
        # Dimensionality-dependent scaling with slight modification
        dim_scale = 1.0 + 0.25 * np.log(self.dim + 1)
        
        return dim_scale * (base_term + 0.35 * harmonic_term + 0.3 * coupling_term + 
                           0.25 * basin_term + 0.15 * perturbation_term)