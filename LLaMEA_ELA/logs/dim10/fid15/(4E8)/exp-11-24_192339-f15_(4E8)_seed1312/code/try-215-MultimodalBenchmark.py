import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sinusoidal component with dynamic frequency modulation
        chaotic_component = 0
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(0.3 * x[i] + 0.7 * np.cos(0.4 * x[i]))
            chaotic_component += np.sin(freq * x[i]) * np.cos(0.2 * x[i]**2) * np.exp(-0.1 * np.abs(x[i]))
        
        # Dynamic radial basis function with quaternion-inspired coupling
        rbf_component = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                width = 1.0 + 0.5 * np.sin(0.5 * x[i] + 0.3 * x[j])
                # Quaternion-inspired asymmetric coupling
                quat_coupling = (x[i]**2 * x[j] + x[j]**2 * x[i]) * np.exp(-0.5 * (dist / width)**2)
                rbf_component += quat_coupling
        
        # Hyperbolic tangent-based cross-dimensional interaction
        tan_component = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                tan_mod = np.tanh(x[i] * x[j] + 0.5 * np.sin(x[i] + x[j]))
                tan_term = (x[i]**2 + x[j]) * tan_mod * np.exp(-0.2 * (x[i] - x[j])**2)
                tan_component += tan_term
        
        # Fractal-like asymmetric polynomial with dynamic scaling
        fractal_poly = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic scale factor based on chaotic modulation
                scale = 1.0 + 0.3 * np.sin(2.0 * x[i] + 0.7 * x[j]) * np.cos(1.5 * x[i])
                fractal_poly += (x[i]**3 - x[j]**2) * scale
        
        # Exponential decay with chaotic modulation
        exp_component = 0
        for i in range(self.dim):
            exp_component += np.exp(-0.3 * x[i]**2) * np.sin(0.15 * self.dim * x[i] + 0.2 * np.cos(x[i]))
        
        # Global scaling factor with chaotic influence
        scale_factor = 1.0 + 0.2 * np.sin(0.4 * self.dim + 0.6 * np.cos(0.3 * x[0] if self.dim > 0 else 0))
        
        # Combine all components with optimized weights for better discrimination
        return scale_factor * (0.3 * chaotic_component + 0.25 * rbf_component + 
                              0.2 * tan_component + 0.15 * fractal_poly + 0.1 * exp_component)