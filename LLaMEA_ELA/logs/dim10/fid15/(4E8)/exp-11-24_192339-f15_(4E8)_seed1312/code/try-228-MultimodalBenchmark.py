import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine-modulated Gaussian peaks
        peaks = 0
        for i in range(self.dim):
            # Chaotic modulation of peak positions and heights
            peak_pos = 2.0 * np.sin(0.5 * x[i]) + 1.0 * np.cos(0.3 * x[i])
            peak_height = 1.0 + 0.5 * np.sin(0.7 * x[i])
            sigma = 0.5 + 0.3 * np.cos(0.4 * x[i])
            peaks += peak_height * np.exp(-0.5 * ((x[i] - peak_pos) / sigma)**2)
        
        # Directional anisotropy with elliptical contours
        aniso = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Elliptical distortion based on sine-modulated axes
                axis_i = 1.0 + 0.3 * np.sin(0.6 * x[i])
                axis_j = 1.0 + 0.4 * np.cos(0.5 * x[j])
                aniso += (x[i]**2 / axis_i**2 + x[j]**2 / axis_j**2) * np.exp(-0.1 * (x[i] + x[j])**2)
        
        # Fractal-based correlation structure
        fractal_corr = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Logarithmic distance with fractal scaling
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                fractal_factor = np.log(dist + 1.0) * (1.0 + 0.2 * np.sin(2.0 * dist))
                fractal_corr += fractal_factor * np.exp(-0.05 * (x[i] - x[j])**2)
        
        # Cross-dimensional sine coupling with varying frequencies
        cross_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                freq = 1.0 + 0.5 * np.sin(0.3 * x[i]) * np.cos(0.2 * x[j])
                cross_coupling += np.sin(freq * (x[i] + x[j])) * np.exp(-0.1 * (x[i] - x[j])**2)
        
        # Asymmetric power landscape with multi-scale modulation
        power_landscape = 0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.3 * np.sin(0.4 * x[i])
            power_landscape += (np.abs(x[i])**2.2) * scale_factor * np.exp(-0.08 * x[i]**2)
        
        # Global conditioning with dimension-dependent scaling
        cond_factor = 1.0 + 0.3 * np.sin(0.5 * self.dim) + 0.2 * np.cos(0.3 * self.dim)
        
        # Combine all components with optimized weights
        return cond_factor * (0.3 * peaks + 0.25 * aniso + 0.2 * fractal_corr + 
                             0.15 * cross_coupling + 0.1 * power_landscape)