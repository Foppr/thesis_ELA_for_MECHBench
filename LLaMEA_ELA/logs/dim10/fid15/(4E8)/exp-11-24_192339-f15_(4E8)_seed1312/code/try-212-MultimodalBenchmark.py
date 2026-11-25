import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos expansion component with adaptive exponents
        chaos = 0
        for i in range(self.dim):
            # Adaptive exponent based on position
            exp_factor = 2.0 + 1.5 * np.sin(0.4 * x[i])
            chaos += (x[i]**exp_factor) * np.cos(0.3 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Radial basis functions with adaptive widths and quaternion-inspired coupling
        rbf = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                # Adaptive width based on distance
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                adaptive_width = 1.0 + 0.5 * np.sin(0.2 * (x[i] + x[j]))
                # Quaternion-inspired coupling with imaginary components
                quat_coupling = np.cos(0.2 * x[i]) * np.sin(0.2 * x[j]) - np.sin(0.2 * x[i]) * np.cos(0.2 * x[j])
                rbf += quat_coupling * np.exp(-0.5 * (dist / adaptive_width)**2)
        
        # Cross-dimensional interaction with hyperbolic sine and cosine coupling
        cross_dim = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Sine-cosine based coupling
                coupling = np.sin(0.5 * x[i]) * np.cos(0.5 * x[j]) + np.cos(0.5 * x[i]) * np.sin(0.5 * x[j])
                cross_dim += coupling * (x[i]**2 + x[j]**2) * np.exp(-0.1 * (x[i] - x[j])**2)
        
        # Asymmetric polynomial with dynamic conditioning
        asym_poly = 0
        for i in range(self.dim):
            # Dynamic condition number based on position
            cond_num = 1.0 + 0.3 * np.sin(0.6 * x[i])
            asym_poly += (x[i]**3 + 0.5 * x[i]**2) * np.tanh(x[i]) * cond_num
        
        # Fractal-like structure with recursive polynomial interactions
        fractal = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Recursive interaction with varying coupling strength
                coupling_strength = 0.5 + 0.3 * np.sin(0.3 * (x[i] + x[j]))
                fractal += coupling_strength * (x[i]**2 * x[j] + x[i] * x[j]**2) * np.exp(-0.15 * (x[i] - x[j])**2)
        
        # Global scaling with dimension-dependent factor
        scale_factor = 1.0 + 0.4 * np.sin(self.dim * 0.2) + 0.2 * np.cos(self.dim * 0.1)
        
        # Combine all components with optimized weights
        return scale_factor * (0.3 * chaos + 0.25 * rbf + 0.2 * cross_dim + 
                              0.15 * asym_poly + 0.1 * fractal)