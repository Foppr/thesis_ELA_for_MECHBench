import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic tent map component for irregularity
        tent_component = 0
        for i in range(self.dim):
            # Tent map with parameter dependent on dimension
            r = 3.8 + 0.2 * np.sin(0.1 * self.dim)
            xi = x[i] if x[i] < 0.5 else 1 - x[i]
            tent_component += r * xi * (1 - xi)
        
        # Adaptive Gaussian peaks with dynamic centers and widths
        gaussian_component = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling
                center_i = np.sin(0.3 * x[i]) * 2.0
                center_j = np.cos(0.2 * x[j]) * 2.0
                width_i = 0.5 + 0.3 * np.abs(np.sin(0.4 * x[i]))
                width_j = 0.5 + 0.3 * np.abs(np.cos(0.4 * x[j]))
                dist = np.sqrt((x[i] - center_i)**2 + (x[j] - center_j)**2)
                gaussian_component += np.exp(-0.5 * (dist / (width_i + width_j))**2)
        
        # Fractional Brownian motion-like correlation with Hurst exponent modulation
        fbm_component = 0
        hurst = 0.3 + 0.4 * np.sin(0.1 * self.dim)
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Distance-based correlation with fractional scaling
                dist = np.abs(x[i] - x[j])
                corr = dist**(-2 * hurst)
                fbm_component += corr * (x[i]**2 + x[j]**2)
        
        # Asymmetric hyperbolic sine coupling with dynamic scaling
        asym_sinh = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                scale_factor = 1.0 + 0.5 * np.sin(0.2 * x[i])
                asym_sinh += np.sinh(x[i] * x[j]) * scale_factor
        
        # Exponential decay with multi-scale modulation
        exp_component = 0
        for i in range(self.dim):
            exp_component += np.exp(-0.5 * x[i]**2) * np.cos(0.1 * self.dim * x[i])
        
        # Global scaling and weighted sum
        scale_factor = 1.0 + 0.1 * np.cos(0.5 * self.dim)
        return scale_factor * (0.3 * tent_component + 0.25 * gaussian_component + 
                              0.2 * fbm_component + 0.15 * asym_sinh + 0.1 * exp_component)