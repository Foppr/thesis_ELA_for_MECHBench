import numpy as np

class ChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Radial Basis Functions with chaotic center placements
        rbf_centers = np.array([np.sin(i * 2.718) for i in range(self.dim)])
        rbf_widths = 0.5 + 0.3 * np.sin(np.arange(self.dim) * 1.618)
        rbf_heights = 1.2 + 0.8 * np.cos(np.arange(self.dim) * 3.14159)
        
        rbf_sum = np.sum(rbf_heights * np.exp(-0.5 * ((x_scaled - rbf_centers) / rbf_widths)**2))
        
        # Chaotic sine-wave interactions with varying frequencies and amplitudes
        chaotic_wave = np.sum(np.sin(10.0 * x_scaled + np.sin(7.0 * x_scaled)) * 
                             np.cos(8.0 * x_scaled + np.cos(5.0 * x_scaled)) + 
                             0.6 * np.sin(15.0 * x_scaled**2 + np.sin(9.0 * x_scaled**2)) * 
                             np.cos(12.0 * x_scaled**2 + np.cos(8.0 * x_scaled**2)))
        
        # Gradient-based attraction wells with non-linear potential
        well_potential = np.sum((x_scaled**4 - 2.0 * x_scaled**2 + 0.5) * 
                              np.exp(-0.5 * x_scaled**2))
        
        # Cross-dimensional coupling with polynomial interaction terms
        cross_coupling = np.sum((x_scaled[:-1]**2 + x_scaled[1:]**2)**1.5 * 
                              np.sin(4.0 * (x_scaled[:-1] + x_scaled[1:])) + 
                              (x_scaled[:-2]**3 - x_scaled[2:]**3) * 
                              np.cos(3.0 * (x_scaled[:-2] - x_scaled[2:])))
        
        # Asymmetric harmonic modulation with time-varying phases
        asym_harmonic = np.sum(np.sin(6.0 * x_scaled + 0.5 * np.sin(3.0 * x_scaled)) * 
                             np.cos(4.0 * x_scaled + 0.3 * np.cos(2.0 * x_scaled)) + 
                             0.7 * np.sin(11.0 * x_scaled**2 + 0.4 * np.sin(5.0 * x_scaled**2)) * 
                             np.cos(9.0 * x_scaled**2 + 0.6 * np.cos(4.0 * x_scaled**2)))
        
        # Combine all components with adaptive weights
        return 0.4 * rbf_sum + 0.3 * chaotic_wave + 0.15 * well_potential + \
               0.1 * cross_coupling + 0.05 * asym_harmonic + 2.1