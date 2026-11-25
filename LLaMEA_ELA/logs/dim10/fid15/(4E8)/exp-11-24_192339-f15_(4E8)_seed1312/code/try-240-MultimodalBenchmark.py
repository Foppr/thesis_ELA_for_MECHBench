import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic sine-modulated Gaussian peaks with dynamic positioning
        peaks = 0
        for i in range(self.dim):
            # Chaotic modulation of peak positions and heights with higher frequency components
            peak_pos = 2.0 * np.sin(0.8 * x[i]) + 1.5 * np.cos(0.6 * x[i]) + 0.5 * np.sin(1.2 * x[i])
            peak_height = 1.5 + 0.7 * np.sin(0.9 * x[i]) + 0.3 * np.cos(1.1 * x[i])
            sigma = 0.6 + 0.4 * np.cos(0.5 * x[i]) + 0.2 * np.sin(0.8 * x[i])
            peaks += peak_height * np.exp(-0.5 * ((x[i] - peak_pos) / sigma)**2)
        
        # Dynamic directional anisotropy with time-varying elliptical contours
        aniso = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Time-varying elliptical distortion based on higher frequency sine-cosine modulations
                axis_i = 1.2 + 0.4 * np.sin(0.7 * x[i]) + 0.3 * np.cos(0.9 * x[i])
                axis_j = 1.3 + 0.5 * np.cos(0.6 * x[j]) + 0.2 * np.sin(0.8 * x[j])
                aniso += (x[i]**2 / axis_i**2 + x[j]**2 / axis_j**2) * np.exp(-0.15 * (x[i] + x[j])**2)
        
        # Enhanced fractal-based correlation structure with multi-scale logarithmic interactions
        fractal_corr = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Multi-scale distance with enhanced fractal scaling and coupling
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                fractal_factor = np.log(dist + 1.0) * (1.0 + 0.3 * np.sin(2.5 * dist) + 0.1 * np.cos(3.0 * dist))
                fractal_corr += fractal_factor * np.exp(-0.08 * (x[i] - x[j])**2)
        
        # Cross-dimensional sine coupling with adaptive frequencies and multi-scale interactions
        cross_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                freq = 1.2 + 0.6 * np.sin(0.4 * x[i]) * np.cos(0.3 * x[j]) + 0.2 * np.sin(0.7 * x[i] + 0.5 * x[j])
                cross_coupling += np.sin(freq * (x[i] + x[j])) * np.exp(-0.12 * (x[i] - x[j])**2)
        
        # Asymmetric power landscape with enhanced multi-scale modulation
        power_landscape = 0
        for i in range(self.dim):
            scale_factor = 1.2 + 0.4 * np.sin(0.5 * x[i]) + 0.3 * np.cos(0.6 * x[i]) + 0.1 * np.sin(1.0 * x[i])
            power_landscape += (np.abs(x[i])**2.5) * scale_factor * np.exp(-0.1 * x[i]**2)
        
        # Enhanced global conditioning with adaptive dimension-dependent scaling
        cond_factor = 1.0 + 0.4 * np.sin(0.6 * self.dim) + 0.3 * np.cos(0.4 * self.dim) + 0.2 * np.sin(0.8 * self.dim)
        
        # Combine all components with optimized weights for better fitness
        return cond_factor * (0.35 * peaks + 0.2 * aniso + 0.25 * fractal_corr + 
                             0.15 * cross_coupling + 0.05 * power_landscape)