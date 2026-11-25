import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic sine-modulated Gaussian peaks with dynamic scaling
        peaks = 0
        for i in range(self.dim):
            # Enhanced chaotic modulation of peak positions and heights
            peak_pos = 2.0 * np.sin(0.5 * x[i]) + 1.0 * np.cos(0.3 * x[i]) + 0.5 * np.sin(0.8 * x[i])
            peak_height = 1.0 + 0.5 * np.sin(0.7 * x[i]) + 0.3 * np.cos(0.9 * x[i])
            sigma = 0.5 + 0.3 * np.cos(0.4 * x[i]) + 0.2 * np.sin(0.6 * x[i])
            peaks += peak_height * np.exp(-0.5 * ((x[i] - peak_pos) / sigma)**2)
        
        # Enhanced directional anisotropy with elliptical contours and dynamic axes
        aniso = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic elliptical distortion based on sine-modulated axes
                axis_i = 1.0 + 0.3 * np.sin(0.6 * x[i]) + 0.2 * np.cos(0.4 * x[i])
                axis_j = 1.0 + 0.4 * np.cos(0.5 * x[j]) + 0.1 * np.sin(0.7 * x[j])
                aniso += (x[i]**2 / axis_i**2 + x[j]**2 / axis_j**2) * np.exp(-0.1 * (x[i] + x[j])**2)
        
        # Enhanced fractal-based correlation structure with multi-scale interactions
        fractal_corr = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Multi-scale logarithmic distance with fractal scaling
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                fractal_factor = np.log(dist + 1.0) * (1.0 + 0.2 * np.sin(2.0 * dist) + 0.1 * np.cos(3.0 * dist))
                fractal_corr += fractal_factor * np.exp(-0.05 * (x[i] - x[j])**2)
        
        # Enhanced cross-dimensional sine coupling with variable frequencies and phase shifts
        cross_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                freq = 1.0 + 0.5 * np.sin(0.3 * x[i]) * np.cos(0.2 * x[j]) + 0.2 * np.sin(0.4 * (x[i] + x[j]))
                phase_shift = 0.1 * np.cos(0.5 * x[i]) * np.sin(0.3 * x[j])
                cross_coupling += np.sin(freq * (x[i] + x[j]) + phase_shift) * np.exp(-0.1 * (x[i] - x[j])**2)
        
        # Enhanced asymmetric power landscape with multi-scale modulation and dynamic exponents
        power_landscape = 0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.3 * np.sin(0.4 * x[i]) + 0.2 * np.cos(0.6 * x[i])
            exponent = 2.2 + 0.3 * np.sin(0.5 * x[i])
            power_landscape += (np.abs(x[i])**exponent) * scale_factor * np.exp(-0.08 * x[i]**2)
        
        # Enhanced global conditioning with dimension-dependent scaling and dynamic bias
        cond_factor = 1.0 + 0.3 * np.sin(0.5 * self.dim) + 0.2 * np.cos(0.3 * self.dim) + 0.1 * np.sin(0.7 * self.dim)
        
        # Combine all components with optimized weights for improved benchmark performance
        return cond_factor * (0.35 * peaks + 0.2 * aniso + 0.25 * fractal_corr + 
                             0.15 * cross_coupling + 0.05 * power_landscape)