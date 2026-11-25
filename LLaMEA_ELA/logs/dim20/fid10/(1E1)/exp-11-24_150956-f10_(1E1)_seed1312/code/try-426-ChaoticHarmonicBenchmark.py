import numpy as np

class ChaoticHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute logistic map sequence for chaotic behavior
        self.logistic_r = 3.95
        self.logistic_x = 0.5
        self.logistic_seq = []
        for i in range(dim * 10):
            self.logistic_x = self.logistic_r * self.logistic_x * (1 - self.logistic_x)
            self.logistic_seq.append(self.logistic_x)
        self.logistic_seq = np.array(self.logistic_seq[:dim])
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Chaotic component using logistic map
        chaotic = np.sum(np.sin(20.0 * self.logistic_seq * x_scaled) * 
                        np.cos(15.0 * self.logistic_seq * x_scaled))
        
        # Spherical harmonics component with varying degrees
        sph_harms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                if i < len(x_scaled) and j < len(x_scaled):
                    dist = np.sqrt((x_scaled[i] - x_scaled[j])**2 + 0.01)
                    sph_harms += np.sin(5.0 * dist) / (dist + 0.1) * np.cos(3.0 * (x_scaled[i] + x_scaled[j]))
        
        # Asymmetric bell curves with varying widths and offsets
        asym_bells = np.sum(0.8 * np.exp(-2.0 * (x_scaled - 0.5)**2) * 
                          (1.0 + 0.3 * np.sin(10.0 * x_scaled)) +
                          0.4 * np.exp(-3.0 * (x_scaled + 0.3)**2) * 
                          (1.0 + 0.5 * np.cos(8.0 * x_scaled)) +
                          0.6 * np.exp(-1.5 * (x_scaled - 0.8)**2) * 
                          (1.0 + 0.4 * np.sin(12.0 * x_scaled)))
        
        # Cross-dimensional coupling with polynomial interaction
        poly_coupling = 0.0
        for i in range(self.dim - 2):
            if i < len(x_scaled) - 2:
                poly_coupling += (x_scaled[i]**2 + x_scaled[i+1]**2 + x_scaled[i+2]**2) * \
                               np.sin(4.0 * (x_scaled[i] + x_scaled[i+1] + x_scaled[i+2]))
        
        # Multi-scale sinusoidal interference
        multi_scale = np.sum(np.sin(25.0 * x_scaled**2) * np.cos(20.0 * x_scaled**2) +
                           0.7 * np.sin(35.0 * x_scaled**3) * np.cos(30.0 * x_scaled**3) +
                           0.5 * np.sin(45.0 * x_scaled**4) * np.cos(40.0 * x_scaled**4))
        
        # Combine all components with adaptive weights
        return 0.25 * chaotic + 0.3 * sph_harms + 0.2 * asym_bells + 0.15 * poly_coupling + 0.1 * multi_scale + 2.1