import numpy as np

class QuantumHarmonicBasinBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.oscillator_freq = 12.0
        self.quantum_tunneling_strength = 2.5
        self.fractal_scaling = 4.3
        self.basin_complexity_factor = 1.8
        self.chaotic_coupling = 0.7
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = np.clip(x / 5.0, -1, 1)
        
        # Create nested harmonic oscillators with quantum tunneling effects
        oscillator_terms = np.zeros(self.dim)
        for i in range(self.dim):
            freq = self.oscillator_freq * (2 ** (i % 7))
            # Multiple harmonic components with varying amplitudes and phases
            oscillator_terms[i] = (
                0.8 * np.sin(freq * x_norm[i]) +
                0.4 * np.sin(2 * freq * x_norm[i]) +
                0.2 * np.sin(3 * freq * x_norm[i]) +
                0.1 * np.sin(5 * freq * x_norm[i])
            )
            
            # Add quantum tunneling effects with chaotic modulation
            tunneling_effect = self.quantum_tunneling_strength * np.exp(-abs(x_norm[i]) ** 1.8) * \
                              np.cos(freq * x_norm[i] * 0.5)
            oscillator_terms[i] += tunneling_effect
            
        # Create dynamic basin complexity with nested fractal structure
        basin_terms = np.zeros(self.dim)
        for i in range(self.dim):
            # Nested basins with different scaling factors
            scales = [1.0, 0.5, 0.25, 0.125]
            strengths = [1.5, 1.2, 0.8, 0.5]
            
            basin_sum = 0
            for scale, strength in zip(scales, strengths):
                scaled_x = x_norm[i] * scale
                # Fractal basin structure with chaotic coupling
                basin_sum += strength * np.exp(-scaled_x**2) * np.sin(self.fractal_scaling * scaled_x)
            
            basin_terms[i] = basin_sum
            
        # Combine oscillator and basin terms
        combined_terms = oscillator_terms + 0.6 * basin_terms
        
        # Add chaotic coupling between dimensions
        coupling_term = 0
        for i in range(self.dim - 1):
            coupling_strength = self.chaotic_coupling * (1.0 + 0.3 * np.sin(i * 0.7))
            coupling_term += coupling_strength * (x_norm[i] - x_norm[i+1])**4
            
        # Add adaptive penalty based on solution distribution
        penalty = 0.3 * self.dim * (np.std(x_norm)**2 + 0.2 * np.mean(np.abs(x_norm))) * \
                 (1.0 + 0.15 * np.sin(self.dim * 0.6))
        
        # Add quantum interference patterns with dynamic dimension scaling
        interference = 0.4 * np.sum(np.sin(self.dim * x_norm) * np.cos(2 * self.dim * x_norm))
        
        # Add basin complexity factor that scales with dimensionality
        basin_complexity = self.basin_complexity_factor * np.sum(np.sin(3.0 * x_norm)**2) * \
                          (1.0 + 0.2 * np.cos(self.dim * 0.9))
        
        # Final adaptive scaling factor with chaotic modulation
        adaptive_scale = 1.0 + 0.03 * np.log(self.dim + 1) + 0.015 * np.sin(self.dim * 0.7) + \
                        0.02 * np.cos(self.dim * 0.5)
        
        return adaptive_scale * (np.sum(combined_terms**5) + coupling_term + penalty + 
                               interference + basin_complexity)