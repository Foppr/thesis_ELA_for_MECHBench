import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Polynomial potential wells with chaotic modulation
        poly_potentials = []
        for i in range(self.dim):
            chaos_factor = np.sin(13 * x_norm[i]) * np.cos(7 * x_norm[i])
            poly_potentials.append((x_norm[i]**4 + 0.5 * x_norm[i]**2 + 
                                 0.1 * chaos_factor) * np.exp(-0.5 * x_norm[i]**2))
        
        # Trigonometric coupling with frequency mixing
        trig_coupling = 0.0
        for i in range(self.dim - 1):
            freq_mix = np.sin(3 * x_norm[i]) * np.cos(5 * x_norm[i+1]) + \
                      np.cos(2 * x_norm[i]) * np.sin(4 * x_norm[i+1])
            trig_coupling += freq_mix * np.exp(-0.1 * (x_norm[i] - x_norm[i+1])**2)
        
        # Exponential decay with dynamic scaling
        exp_decay = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.5 * np.sin(5 * x_norm[i]**3)
            exp_decay += np.exp(-scale * np.abs(x_norm[i])) * \
                        np.cos(2 * x_norm[i])**3
        
        # Chaotic gradient components with varying amplitudes
        chaotic_gradients = 0.0
        for i in range(self.dim):
            amp = 0.8 + 0.4 * np.sin(11 * x_norm[i])
            chaotic_gradients += amp * np.sin(17 * x_norm[i] + 
                                             np.cos(9 * x_norm[i]))**2
        
        # Multi-scale harmonic interference
        harmonic_interference = 0.0
        for i in range(self.dim):
            for k in range(1, 6):
                harmonic_interference += np.sin(k * x_norm[i] + 
                                              k**1.5 * np.cos(k * x_norm[i]))**2
        
        # Basin structure with irregular boundaries
        basin_structure = 0.0
        for i in range(self.dim):
            basin_structure += (x_norm[i]**2 + 0.3 * np.sin(10 * x_norm[i])**2 + 
                             0.1 * np.exp(-x_norm[i]**2))
        
        # Cross-dimensional chaotic interaction terms
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_terms += (np.sin(3 * x_norm[i] + 7 * x_norm[j]) * 
                              np.cos(5 * x_norm[i] - 2 * x_norm[j])) * \
                              np.exp(-0.3 * (x_norm[i]**2 + x_norm[j]**2))
        
        # Combine all components with dynamic weighting
        return (0.4 * np.sum(poly_potentials) + 0.3 * trig_coupling + 
                0.2 * exp_decay + 0.15 * chaotic_gradients + 
                0.1 * harmonic_interference + 0.05 * basin_structure + 
                0.05 * cross_terms)