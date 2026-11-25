import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic tent map-based interactions with varying parameters
        tent_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Tent map with chaotic coupling
                a = 1.7 + 0.2 * np.sin(0.5 * x[i])
                b = 1.4 + 0.1 * np.cos(0.4 * x[j])
                tent_val = np.abs(x[i] - x[j]) / (1.0 + np.exp(-a * (x[i] - x[j])**2))
                tent_interaction += tent_val * np.sin(b * (x[i] + x[j]))
        
        # Spectral Gaussian kernel with frequency-dependent widths
        spectral_gauss = 0
        for i in range(self.dim):
            # Multi-frequency Gaussian with dynamic width
            freq = 2.5 + 0.4 * np.sin(0.7 * x[i])
            width = 0.4 + 0.1 * np.cos(0.5 * x[i])
            center = 1.2 * np.sin(0.6 * x[i]) + 0.3 * np.cos(0.8 * x[i])
            spectral_gauss += np.exp(-0.5 * ((x[i] - center) / width)**2) * np.sin(freq * x[i])
        
        # Adaptive saddle-point valleys with dynamic curvature
        saddle_valleys = 0
        for i in range(self.dim):
            # Saddle point with adaptive coefficients
            a = 0.9 + 0.1 * np.sin(0.4 * x[i])
            b = 1.3 + 0.2 * np.cos(0.6 * x[i])
            saddle_valleys += (x[i]**2 - a) * (x[i]**2 - b)
        
        # Fractal-like oscillation with diminishing frequency
        fractal_osc = 0
        for i in range(self.dim):
            freq = 1.2 + 0.2 * np.sin(0.5 * x[i])
            amp = 1.0 / (1.0 + 0.3 * i)
            fractal_osc += amp * np.cos(freq * x[i]) * np.exp(-0.15 * x[i]**2)
        
        # Cross-dimensional coupling with exponential modulation
        cross_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Exponential coupling with coordinate-dependent modulation
                mod = np.exp(0.15 * (x[i] + x[j]))
                cross_coupling += mod * np.sin(x[i] * x[j]) * np.cos(0.6 * (x[i]**2 + x[j]**2))
        
        # Global conditioning with dimension-dependent scaling
        cond_factor = 1.0 + 0.4 * np.sin(0.5 * self.dim) + 0.15 * np.cos(0.7 * self.dim)
        
        # Combine all components with optimized weights
        return cond_factor * (0.22 * tent_interaction + 0.23 * spectral_gauss + 
                             0.18 * saddle_valleys + 0.22 * fractal_osc + 0.15 * cross_coupling)