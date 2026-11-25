import numpy as np

class ChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic tent map component with parameter dependence
        tent_map = 0.0
        a = 1.5
        for i in range(self.dim - 1):
            if x_norm[i] < 0.5:
                tent_map += a * x_norm[i]
            else:
                tent_map += a * (1 - x_norm[i])
        
        # Radial basis function valleys with adaptive centers and widths
        rbf_valleys = 0.0
        for i in range(self.dim):
            center = 0.3 * np.sin(2 * np.pi * i / self.dim)
            width = 0.5 + 0.3 * np.cos(3 * np.pi * i / self.dim)
            rbf_valleys += np.exp(-0.5 * ((x_norm[i] - center) / width)**2)
        
        # Cross-dimensional coupling with sine-wave interference
        coupling = 0.0
        for i in range(self.dim - 1):
            coupling += np.sin(5 * (x_norm[i] + x_norm[i+1])) * np.cos(3 * (x_norm[i] - x_norm[i+1]))
        
        # Multi-scale harmonic oscillations with frequency modulation
        harmonic = 0.0
        for i in range(self.dim):
            freq = 2**(i % 4)
            harmonic += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i])
        
        # Asymmetric Gaussian peaks with directional bias
        asym_peaks = 0.0
        for i in range(self.dim):
            peak_center = 0.4 * np.sin(2 * np.pi * i / self.dim)
            peak_width = 0.3 + 0.2 * np.cos(2 * np.pi * i / self.dim)
            asym_peaks += np.exp(-0.5 * ((x_norm[i] - peak_center) / peak_width)**2) * (1 + 0.3 * x_norm[i])
        
        # Dimension-dependent conditioning factor with exponential decay
        condition_factor = 1.0 + 0.8 * np.exp(-0.1 * self.dim)
        
        # Combine all terms
        return condition_factor * (tent_map + rbf_valleys + coupling + harmonic + asym_peaks)