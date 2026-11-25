import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters for each dimension
        self.chaos_params = [0.5 + 0.3 * np.sin(0.4 * i + 1.0) for i in range(dim)]
        self.coupling_strengths = [0.8 + 0.2 * np.cos(0.6 * i + 0.5) for i in range(dim)]
        self.frequency_modulators = [1.0 + 0.5 * np.sin(0.3 * i + 0.7) for i in range(dim)]
        self.harmonic_amps = [0.6 + 0.2 * np.cos(0.5 * i + 0.3) for i in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Add chaotic gradient components with dimension-specific modulation
        for i in range(self.dim):
            xi = x[i]
            chaos_param = self.chaos_params[i]
            # Chaotic sine-cosine gradient structure with exponential scaling
            grad_component = np.sin(chaos_param * xi) * np.cos(chaos_param * xi)
            result += grad_component * (1.0 + 0.3 * np.sin(xi**2))
            
        # Add adaptive coupling terms between dimensions
        for i in range(self.dim):
            xi = x[i]
            coupling_strength = self.coupling_strengths[i]
            # Coupled harmonic interference with phase shifts
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling
                xj = x[j]
                coupling_term = coupling_strength * np.sin(xi + xj) * np.cos(xi - xj)
                result += coupling_term
                
        # Add multi-scale harmonic interference with frequency modulation
        for i in range(self.dim):
            xi = x[i]
            freq_mod = self.frequency_modulators[i]
            amp = self.harmonic_amps[i]
            # Multi-frequency harmonic components with varying amplitudes and phases
            for k in range(1, 6):
                freq = k * freq_mod
                phase_shift = 0.2 * np.sin(k * xi + 0.5)
                result += amp * np.sin(freq * xi + phase_shift) * np.cos(freq * xi + phase_shift)
                
        # Add saddle-point dominance with asymmetric curvature
        for i in range(self.dim):
            xi = x[i]
            # Asymmetric quadratic with chaotic modulation
            asymmetry = 0.1 * np.sin(0.5 * i + 0.3)
            result += (xi**2) * (1.0 + asymmetry * np.cos(xi))
            
        # Add dimensionality-dependent scaling and chaos control
        dim_factor = 1.0 + 0.2 * np.sin(0.3 * self.dim + 0.4)
        result *= dim_factor
        
        # Add final chaotic modulation with global resonance effect
        resonance = 0.05 * np.sum(np.sin(8.0 * x) * np.cos(4.0 * x))
        result += resonance
        
        return result